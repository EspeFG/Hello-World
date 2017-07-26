import os
from os.path import expanduser
import sys
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
from flask import request
import pandas as pd

app = Flask(__name__)
sys.path.append(expanduser("~/research-projects/ihq_research/topic_update/"))
sys.path.append(expanduser("~/research-projects/ihq_research/Actions"))
from hadoop_access import *
from Allocations import Allocations
from PriorityOffers import *
from SIM_comp import *


topicContext = { "hadoopPath" : "/signal_control/artefacts/",
                 "localPath" : expanduser("~/research-projects/ihq_research/topic_update/artefacts/topic_files/"),
                 "allPMOffersOutputDirectory" : "/topic_update/all_priority_moments/"}
alloc = Allocations(topicContext)

upload_folder_name = 'uploads'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
upload_path = os.path.join(APP_ROOT, "upload_folder_name")

if not os.path.isdir(upload_path):
    os.mkdir(upload_path)

app.config['UPLOAD_FOLDER'] = upload_path

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['xlsx', 'xlsm', 'csv'])


@app.route('/', methods= ['GET', 'POST'])
def hello_world():
    return render_template('index.html')

def main_df():
    df = getHadoopCSV("/output/standard/qaAggRawActions_12-07-2017_single.csv/part-00000-9a433f42-ef67-4808-98b6-a1e24cda0e58.csv", maxRows=0)
    '''Takes the dataframe, renames the columns and changes date column to dd%-mm%-YY% '''
    df.columns = ["Id", "name", "value", "date", "direction", "Count","durationInSeconds"]
    print("renaming successful")
    df["date"] = pd.to_datetime(df["date"])
    print("datetime fixed")
    return df

def splitDf(df):
    '''Classifies the rows by the name column and separates them into different dataframes'''
    return (
        df[df['name'].str.contains("siteVisit")],
        df[df['name'].str.contains("VOICE")],
        df[df['name'].str.contains("tefPMAccept")]
    )

def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return render_template('index.html')
    else:
        return "No file found or file type is not supported"

#A page that takes your actions for website visits, calls and priority moments and returns an html
#
#
@app.route("/calls_check", methods= ['GET', 'POST'])
def calls_check():

    ret = []

    # Get the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):

        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        #po, alloc = Allocations.getCurrentAllocations(topicContext)
    df = main_df()
    mycalls = pd.read_excel(file)
    calls = df[df['name'].str.contains("VOICE")]
    o2calls =[]
    for i in calls.value:
        o2calls.append(i)
    #return call_actions.loc[~call_actions['business'].isin(o2calls)].to_html()
    return render_template('view2.html',tables=[mycalls.loc[~mycalls['business'].isin(o2calls)].to_html(), mycalls.to_html(), calls.to_html()],
                           titles = (['Missing actions from O2', 'My actions', 'My O2 Actions']))

@app.route("/website_check", methods= ['GET', 'POST'])
def website_check():
    # Get the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):

        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        #po, alloc = Allocations.getCurrentAllocations(topicContext)
    website = pd.read_excel(file)
    website.columns = ["date", "value"]
    website.groupby(lambda x: website['date'][x].month)
    df = main_df()
    O2web = df[df['name'].str.contains("siteVisit")]
    neweb = O2web.drop(['durationInSeconds', 'direction'],axis=1)
    web1 = neweb.copy()
    web1['date'] = web1.date.apply(lambda x:x.strftime('%m-%Y'))
    website_visits1 = website.copy()
    website_visits1['date'] = website.date.apply(lambda x:x.strftime('%m-%Y'))
    web1 = web1.groupby(['date','value'], as_index=False)['Count'].sum()
    web1['o2Flag'] = True
    website_visits1['count'] = 1
    website_visits1 = website_visits1.groupby(['date','value'], as_index=False).count()
    website_visits1['myFlag'] = True
    df_all = web1.merge(website_visits1, on=['date','value'], how='outer')
    #return df_all[df_all.o2Flag.isnull()].to_html()
    return render_template('view3.html',tables=[df_all[df_all.o2Flag.isnull()].to_html(), df_all.to_html()],
                           titles = (['Visits missing in O2 files', 'All Visits']))

@app.route("/priority_check", methods= ['GET', 'POST'])
def priority_check():

    l = []

    # Get the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):

        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        #po, alloc = Allocations.getCurrentAllocations(topicContext)
        df = main_df()
        priority = df.loc[df['name'] == 'tefPMAccept']
        priority.sort_values("date")
        po = PriorityOffers(topicContext)
        new_pm = po.getOffersByIds(po.newOfferIds(alloc.localPMAllocations))
        for keys,values in new_pm.items():
            if keys in set([int(x) for x in priority["value"].tolist()]):
                l.append(values["name"])
    return render_template('view.html',tables=[l , priority.to_html(), pd.read_excel(file).to_html() ],
             titles = ['Actions not present in O2 files', 'My actions in O2 files', 'My actions'])
    #return render_template('view.html',tables=[mycalls.to_html(), calls.to_html()],
                         #  titles = ['My table', 'Another table'])

@app.route('/sim')


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# Route that will process the file upload
@app.route('/upload', methods=['GET'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return render_template('index.html')
    else:
        return "No file found or file type is not supported"


if __name__ == "__main__":
    app.run(debug=True)