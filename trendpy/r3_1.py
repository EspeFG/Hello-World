from main_include import *

trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))
dates = ['2017-05-11','2017-06-01','2017-06-08','2017-06-16']
inputJson = [ [json.load(open(varDefPath + "trend_" + d + ".json")), 
        json.load(open(varDefPath + "profileReport-" + d + ".json", "r"))] for d in dates]


axSum = TableAxis({
  "Name": "Customer Landscape",
  "Version" : "1",
  "Elements": [
    { "ElementText": ["&nbsp;","&nbsp;","&nbsp;"], "Condition": "2.1.weeklyView|*|date",
      "Operation": "lambda x: sorted(x)[0] + ' to ' + sorted(x)[-1]", "CellFormatting" : {"font": {"bold": "False"}, "alignment": {"horizontal":"right"}} },
    { "ElementText": ["Customers", "All Customers", "Count"], "Condition": "3.customers|*|[statistic,value]|allCustomers" },
    { "ElementText": ["Customers", "Active Customers", "Count"], "Condition": "3.customers|*|[statistic,value]|activeCustomers" },
    { "ElementText": ["Actions", "Total number of actions", "Count"], "Condition": "3.actions|*|[statistic,value]|totalActions" },
    { "ElementText": ["Actions", "Customers with actions", "Count"], "Condition": "3.actions|*|[statistic,value]|customersWithActions" },
    { "ElementText": ["Actions", "Mean actions per customer", "Mean"], "Condition": "3.actions|*|[statistic,value]|meanActionsPerCustomer" },
    { "ElementText": ["Actions", "Std.dev Actions per customer", "Std Dev"], "Condition": "3.actions|*|[statistic,value]|stdDevActionsPerCustomer" },
    { "ElementText": ["Topic Generating Actions", "Total number of topic generating actions", "Count"], "Condition": "3.topicGeneratingActions|*|[statistic,value]|totalActions" },
    { "ElementText": ["Topic Generating Actions", "Customers with topic generating actions", "Count"], "Condition": "3.topicGeneratingActions|*|[statistic,value]|customersWithActions" },
    { "ElementText": ["Topic Generating Actions", "Mean topic generating actions per customer", "Mean"], "Condition": "3.topicGeneratingActions|*|[statistic,value]|meanActionsPerCustomer" },
    { "ElementText": ["Topic Generating Actions", "Std dev topic generating actions per customer", "Std Dev"], "Condition": "3.topicGeneratingActions|*|[statistic,value]|stdDevActionsPerCustomer" }        
    ]
})

tab = Table()
tab.TableTitles = ["Table 3", "Landscape (All Customers)"]
for j in inputJson:
    tab.addElasticSearchColumn(j, axSum, "Refresh Period")

options = { "startRow": 2, "startCol": 2, "worksheetName": "Req3 Customer Landscape"}
renderTable(tab, options)