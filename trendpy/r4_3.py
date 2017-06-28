from main_include import *

trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))
dates = ['2017-05-11','2017-06-01','2017-06-08','2017-06-16']
inputJson = [ [json.load(open(varDefPath + "trend_" + d + ".json")), 
        json.load(open(varDefPath + "profileReport-" + d + ".json", "r"))] for d in dates]


ax1_43 = TableAxis({
  "Name": "02AudiencetopicCountBandsAfter",
  "Version" : "1",
  "Elements": [
    { "ElementGroup": {
      "SourceElements": "4.3.o2AudiencesPerCustomerBandedAfter|*|band",
      "Operations": [
        {"Type": "Sort", "Order": "asc", "SortBy": "lambda x: int(x.ElementText[0].replace('1+',str(10**3)).replace('+', ''))"}
      ] } }
  ]
})

ax2_43 = TableAxis({
    "Name": "4_3_O2Audiences_per_Customer",
    "Version" : "1",
    "Elements": [
      { "ElementText": ["Refresh Period (Start - End)", "...", "Before Interest Affinity", "Number of customers with O2 Audience topics"], "Condition": "4.3.o2AudiencesPerCustomerBandedBefore|*|count" },
      { "ElementText": ["Refresh Period (Start - End)", "...", "Before Interest Affinity", "Percentage of Customers"], "Condition": "4.3.o2AudiencesPerCustomerBandedBefore|*|percentage" },
      { "ElementText": ["Refresh Period (Start - End)", "...", "After Interest Affinity", "Number of customers with O2 Audience topics"], "Condition": "4.3.o2AudiencesPerCustomerBandedAfter|*|count" },
      { "ElementText": ["Refresh Period (Start - End)", "...", "After Interest Affinity", "Percentage of Customers"], "Condition": "4.3.o2AudiencesPerCustomerBandedAfter|*|percentage" }
    ]
})

tab43 = Table()
tab43.pivotSparkOutput(ax1_43, ax2_43, trendJson)
tab43.TableTitles = ["Table 4.3", ("Distribution of O2 Audiences per Customer (All Customers)", 2)]

options = { "startRow": 60, "startCol": 2, "worksheetName": "Req4 Customer Dynamics"}
renderTable(tab43, options)