from main_include import *

trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))
dates = ['2017-05-11','2017-06-01','2017-06-08','2017-06-16']
inputJson = [ [json.load(open(varDefPath + "trend_" + d + ".json")), 
        json.load(open(varDefPath + "profileReport-" + d + ".json", "r"))] for d in dates]


ax1_53 = TableAxis({
  "Name": "5_3_TopicsGenerated",
  "Version" : "1",
  "SourcePath": "statistic",
  "Elements": [
    { "ElementText": ["Topics Generated", "Number of customer-topic pairs", "Count"], "Condition": "CTPs" },
    { "ElementText": ["Topics Generated", "Number of distinct topics", "Count"], "Condition": "distinctTopics" },
    { "ElementText": ["Topics Generated", "New topics not seen in most recent data refresh", "Count"], "Condition": "newTopics" },
    { "ElementText": ["Topics Generated", "Existing topics not seen in most recent data", "Count"], "Condition": "disappearedTopics" }
   
  ]
})

ax2_53 = TableAxis({
    "Name": "5_3_TopicsGenerated_columns",
    "Version" : "1",
    "Elements": [
      { "ElementText": ["Refresh Period (Start - End)", "Before Interest Affinity" ], "Condition": "5.3.topicsGenerated|*|before" },
      { "ElementText": ["Refresh Period (Start - End)", "After Interest Affinity"], "Condition": "5.3.topicsGenerated|*|after" },

    ]
  }

)

tab53 = Table()
tab53.pivotSparkOutput(ax1_53, ax2_53, trendJson)
tab53.TableTitles = ["Table 5.3", "Topics generated (All Customers)"]

options = { "startRow": 34, "startCol": 2, "worksheetName": "Req5 Topic Dynamics"}
renderTable(tab53, options)