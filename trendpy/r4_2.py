from main_include import *

trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))
dates = ['2017-05-11','2017-06-01','2017-06-08','2017-06-16']
inputJson = [ [json.load(open(varDefPath + "trend_" + d + ".json")), 
        json.load(open(varDefPath + "profileReport-" + d + ".json", "r"))] for d in dates]

axx1 = TableAxis({
  "Name": "topicCountBandsAfter",
  "Version" : "1",
  "Elements": [
    { "ElementGroup": {
      "SourceElements": "4.2.topicsPerCustomerBandedBefore|*|band",
      "Operations": [
        {"Type": "Sort", "SortBy": "lambda x: int(x.ElementText[0].replace('151+',str(10**6)).replace('1+',str(10**7)).replace(' to ', ''))"}
      ] } }
  ]
})

axx2 = TableAxis({
    "Name": "4_2_Distribution_of_topics_per_Customer",
    "Version" : "1",
    "Elements": [
      { "ElementText": ["Refresh Period (Start - End)", "...", "Before Interest Affinity", "Number of customers with topics"], "Condition": "4.2.topicsPerCustomerBandedBefore|*|count" },
      { "ElementText": ["Refresh Period (Start - End)", "...", "Before Interest Affinity", "Percentage of Customers"], "Condition": "4.2.topicsPerCustomerBandedBefore|*|percentage" },
      { "ElementText": ["Refresh Period (Start - End)", "...", "After Interest Affinity", "Number of customers with topics"], "Condition": "4.2.topicsPerCustomerBandedAfter|*|count" },
      { "ElementText": ["Refresh Period (Start - End)","...", "After Interest Affinity", "Percentage of Customers"], "Condition": "4.2.topicsPerCustomerBandedAfter|*|percentage" }
    ]
}
)

tabx = Table()
tabx.pivotSparkOutput(axx1, axx2, trendJson)
tabx.TableTitles = ["Table 4.2", ("Distribution of Topics per Customer (All Customers)", 2)]

options = { "startRow": 20, "startCol": 2, "worksheetName": "Req4 Customer Dynamics"}
renderTable(tabx, options)