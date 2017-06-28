from main_include import *

trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))
dates = ['2017-05-11','2017-06-01','2017-06-08','2017-06-16']

ax1 = TableAxis({
  "Name": "4_1_Topic_Deciles",
  "Version" : "1",
  "SourcePath": "decile",
  "Elements": [
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "Decile 10"], "Condition": "10" },
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "Decile 9"], "Condition": "9" },
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "Decile 8"], "Condition": "8" },
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "Decile 7"], "Condition": "7" },
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "Decile 6"], "Condition": "6" },
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "Decile 5"], "Condition": "5" },
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "Decile 4"], "Condition": "4" },
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "Decile 3"], "Condition": "3" },
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "Decile 2"], "Condition": "2" },
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "Decile 1"], "Condition": "1" },
    { "ElementText": ["Distribution of Topics per Customer (Deciles)", "All"], "Condition": "all" }
  ]
})

ax2 = TableAxis({
  "Name": "4_1_Topic_Decile_Columns",
  "Version" : "1",
  "Elements": [
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Number of customers with topics"], "Condition": "4.1.topicsPerCustomerDecilesBefore|*|customerCount" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Number of customer-topic-pairs (CTP)"], "Condition": "4.1.topicsPerCustomerDecilesBefore|*|CTPCount" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Percentage of CTP"], "Condition": "4.1.topicsPerCustomerDecilesBefore|*|CTPPercentage" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Cumulative %"], "Condition": "4.1.topicsPerCustomerDecilesBefore|*|CTPPercentage" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Mean topics per customer"], "Condition": "4.1.topicsPerCustomerDecilesBefore|*|meanTopicsPerCustomer" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Std dev of topics per customer"], "Condition": "4.1.topicsPerCustomerDecilesBefore|*|stdDevTopicsPerCustomer" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Min topics per customer"], "Condition": "4.1.topicsPerCustomerDecilesBefore|*|minTopicsPerCustomer" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Max topics per customer"], "Condition": "4.1.topicsPerCustomerDecilesBefore|*|maxTopicsPerCustomer" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Number of customers with topics"], "Condition": "4.1.topicsPerCustomerDecilesAfter|*|customerCount" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Number of customer-topic-pairs (CTP)"], "Condition": "4.1.topicsPerCustomerDecilesAfter|*|CTPCount" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Percentage of CTP"], "Condition": "4.1.topicsPerCustomerDecilesAfter|*|CTPPercentage" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Cumulative %"], "Condition": "4.1.topicsPerCustomerDecilesAfter|*|CTPPercentage" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Mean topics per customer"], "Condition": "4.1.topicsPerCustomerDecilesAfter|*|meanTopicsPerCustomer" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Std dev of topics per customer"], "Condition": "4.1.topicsPerCustomerDecilesAfter|*|stdDevTopicsPerCustomer" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Min topics per customer"], "Condition": "4.1.topicsPerCustomerDecilesAfter|*|minTopicsPerCustomer" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Max topics per customer"], "Condition": "4.1.topicsPerCustomerDecilesAfter|*|maxTopicsPerCustomer" }
  ]
})

tab41 = Table()
tab41.pivotSparkOutput(ax1, ax2, trendJson)
from crosstabs.renderers import HTMLRenderer
tab41.TableTitles = ["Table 4.1", ("Distribution of Topics per Customer Decile (All Customers)", 2)]

options = { "startRow": 2, "startCol": 2, "worksheetName": "Req4 Customer Dynamics"}
renderTable(tab41, options)