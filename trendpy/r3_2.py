from crosstabs.tableManipulations import stackColumns
from crosstabs.table import Table
from main_include import *


trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))
dates = ['2017-05-11','2017-06-01','2017-06-08','2017-06-16']
inputJson = [ [json.load(open(varDefPath + "trend_" + d + ".json")), 
        json.load(open(varDefPath + "profileReport-" + d + ".json", "r"))] for d in dates]

ax3_1 = TableAxis({
  "Name": "Landscape View",
  "Version" : "1",
  "Elements": [
    { "ElementText": ["dummy"], "Condition": "2.1.weeklyView|*|date",
      "Operation": "lambda x: '%s to %s' % tuple([s for i, s in enumerate(sorted(x)) if i==0 or i==len(x)-1])", 
      "CellFormatting" : {"hide": "True", "font": {"bold": "False"}, "alignment": {"horizontal":"right"}} },
    { "ElementText": ["Topics", "Total Number of customer-topic pairs", "Count"], "Condition": "3.topics|*|statistic|totalPairs" },
    { "ElementText": ["Topics", "Customers with topics", "Count"], "Condition": "3.topics|*|statistic|totalCustomers" },
    { "ElementText": ["Topics", "Mean topics per customer", "Mean"], "Condition": "3.topics|*|statistic|meanTopicsPerCustomer" },
    { "ElementText": ["Topics", "Standard deviation topics per customer", "Std Dev"], "Condition": "3.topics|*|statistic|stdDevTopicsPerCustomer" },
    { "ElementText": ["Topics", "Min topics per customer", "Min"], "Condition": "3.topics|*|statistic|minTopicsPerCustomer" },
    { "ElementText": ["Topics", "Max topics per customer", "Max"], "Condition": "3.topics|*|statistic|maxTopicsPerCustomer" },
    { "ElementText": ["O2 Audiences", "Total Number of customer-topic pairs (Audiences)", "Count"], "Condition": "3.o2Audiences|*|statistic|totalPairs" },
    { "ElementText": ["O2 Audiences", "Customers with O2 Audience topics", "Count"], "Condition": "3.o2Audiences|*|statistic|totalCustomers" },
    { "ElementText": ["O2 Audiences", "Mean audiences per customer", "Mean"], "Condition": "3.o2Audiences|*|statistic|meanAudiencesPerCustomer" },
    { "ElementText": ["O2 Audiences", "Standard deviation audiences per customer", "Std Dev"], "Condition": "3.o2Audiences|*|statistic|stdDevAudiencesPerCustomer" },
    { "ElementText": ["O2 Audiences", "Min audiences per customer", "Min"], "Condition": "3.o2Audiences|*|statistic|minAudiencesPerCustomer" },
    { "ElementText": ["O2 Audiences", "Max audiences per customer", "Max"], "Condition": "3.o2Audiences|*|statistic|maxAudiencesPerCustomer" }            
        ]
})

coldef = {
    "Name": "Landscape View",
    "Version" : "1",
    "Elements": [
      { "ElementText": ["Refresh Period", "[!2.1.weeklyView|*|date]", "Before Interest Affinity"], "Condition": "statistic,before", "CellFormatting" : {"maxspan": "2" } },
      { "ElementText": ["Refresh Period", "[!2.1.weeklyView|*|date]", "After Interest Affinity"], "Condition": "statistic,after", "CellFormatting" : {"maxspan": "2" } }
    ]
}

tablesToStack = []
for j in inputJson:
    tab = Table()
    colAx = TableAxis(coldef)
    tab.pivotSparkOutput(ax3_1, colAx, j[0])
    tablesToStack.append(tab)
    
newTab = stackColumns(tablesToStack)
newTab.setElementSpans()
newTab.postProcessElements()

options = { "startRow": 18, "startCol": 2, "worksheetName": "Req 3 Customer Landscape"}
renderTable(tab, options)