from main_include import *

trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))
dates = ['2017-05-11','2017-06-01','2017-06-08','2017-06-16']
inputJson = [ [json.load(open(varDefPath + "trend_" + d + ".json")), 
        json.load(open(varDefPath + "profileReport-" + d + ".json", "r"))] for d in dates]

ax1_52 = TableAxis({
  "Name": "Customer_per_topicCountBandsAfter",
  "Version" : "1",
  "Elements": [
    { "ElementText": ["dummy"], "Condition": "2.1.weeklyView|*|date",
      "Operation": "lambda x: '%s to %s' % tuple([s for i, s in enumerate(sorted(x)) if i==0 or i==len(x)-1])", 
      "CellFormatting" : {"hide": "True", "font": {"bold": "False"}, "alignment": {"horizontal":"right"}} },
    { "ElementGroup": {
      "SourceElements": "5.2a.customersPerTopicBandedAfter|*|band",
      "Operations": [
        {"Type": "Sort", "SortBy": "lambda x: int(x.ElementText[0].split(' ')[0].replace('01+','01').replace('1+','100000000'))"}
      ] } }
  ]
}

)
ax2_52 = {
    "Name": "5_2_CustomerperTopicCountRanges_Columns",
    "Version" : "1",
    "Elements": [
      { "ElementText": ["Refresh Period", "[!2.1.weeklyView|*|date]", "Before Interest Affinity", "Number of distinct topics"], "Condition": "5.2a.customersPerTopicBandedBefore|*|count", "CellFormatting" : {"maxspan": "2" } },
      { "ElementText": ["Refresh Period", "[!2.1.weeklyView|*|date]", "Before Interest Affinity", "Percentage of Topics"], "Condition": "5.2a.customersPerTopicBandedBefore|*|percentage", "CellFormatting" : {"maxspan": "2" } },
      { "ElementText": ["Refresh Period", "[!2.1.weeklyView|*|date]", "After Interest Affinity", "Number of distinct topics"], "Condition": "5.2a.customersPerTopicBandedAfter|*|count", "CellFormatting" : {"maxspan": "2" } },
      { "ElementText": ["Refresh Period", "[!2.1.weeklyView|*|date]", "After Interest Affinity", "Percentage of Topics"], "Condition": "5.2a.customersPerTopicBandedAfter|*|percentage", "CellFormatting" : {"maxspan": "2" } }
    ]
  }

tablesToStack = []
for j in inputJson[2:]:
    tab = Table()
    colAx = TableAxis(ax2_52)
    tab.pivotSparkOutput(ax1_52, colAx, j[0])
    tablesToStack.append(tab)
    
newTab = stackColumns(tablesToStack)
newTab.postProcessElements()
options = { "startRow": 19, "startCol": 2, "worksheetName": "Req5 Topic Dynamics"}
renderTable(newTab, options)