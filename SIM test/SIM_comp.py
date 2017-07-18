from PriorityOffers import PriorityOffers
from collections import defaultdict
from PriorityOffers import *
def main_df(df):
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
    #l = (classif_.web, classif_.calls, classif_.priority)
    #return l
    

def classif_ (__self__):
    '''Classifies the rows by the name column and separates them into different dataframes'''
    classif_.web = df[df['name'].str.contains("siteVisit")]
    classif_.calls = df[df['name'].str.contains("VOICE")]
    classif_.priority = df[df['name'].str.contains("tefPMAccept")]
    l = (classif_.web, classif_.calls, classif_.priority)
    return l

def clean_dfs (df_type):
    if df_type["durationInSeconds"].isnull:
        return df_df_type.drop(['durationInSeconds', 'direction'],axis=1)
    else:
        return Calls

def PM_comp(priority, MyPM):
    '''Compares the actions O2PM versus my recorded actions for PM. '''
    topicContext = { "hadoopPath" : "/signal_control/artefacts/",
                 "localPath" : expanduser("~/research-projects/ihq_research/topic_update/artefacts/topic_files/"), 
                 "allPMOffersOutputDirectory" : "/topic_update/all_priority_moments/"}
    alloc = Allocations(topicContext)
    po = PriorityOffers(topicContext)
    new_pm = po.getOffersByIds(po.newOfferIds(alloc.localPMAllocations))
    allOffers = po.offers()
    for keys,values in allOffers.items():
        if keys in set([int(x) for x in priority["value"].tolist()]):
            print(keys)
            print(values)
    
    return (priority.drop(['durationInSeconds', 'direction'],axis=1), pd.read_excel(MyPM))

def web_comp(O2web, myweb):
    '''Compares the O2web actions versus my recorded actions for web'''
    website = pd.read_excel(myweb)
    website.columns = ["date", "value"]
    website.groupby(lambda x: website['date'][x].month)
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
    return df_all[df_all.o2Flag.isnull()]

def call_comp(calls, myCalls):
    '''Compares the actions O2web versus my recorded actions for web'''
    call_actions = pd.read_excel(myCalls)
    o2calls =[]
    for i in calls.value:
        o2calls.append(i)
    return call_actions.loc[~call_actions['business'].isin(o2calls)]
    
    
