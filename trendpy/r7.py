from main_include import *

trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))
dates = ['2017-05-11','2017-06-01','2017-06-08','2017-06-16']
inputJson = [ [json.load(open(varDefPath + "trend_" + d + ".json")), 
        json.load(open(varDefPath + "profileReport-" + d + ".json", "r"))] for d in dates]

InterestCols = TableAxis( {
    "Name": "Interest",
    "Version": 1,
    "Elements": [
        { "ElementText": ["Refresh Period","[!2.1.weeklyView|*|date]", "Active Customers *", "Count"], "Condition": "7.1.topicAssignment|*|count" },
        { "ElementText": ["Refresh Period","[!2.1.weeklyView|*|date]", "% Active Customers", "%"], "Condition": "7.1.topicAssignment|*|percentage", "DataFormatting" : {"NumberFormat":"0.0%"} }
    ]
})

Interests = TableAxis({
    "Name": "Interest",
    "Version" : "1",
    "Elements": [
        { "ElementGroup": {
            "ElementText": [],
            "SourceElements": "7.1.topicAssignment|*|topic",
            "Formatting" : [{}, {"font": {"bold": "False"}, "alignment": {"horizontal":"left"}}],
            "Operations": [
                {"Type": "Sort", "Order": "asc"},
                {"Type": "AddIndex"}
            ] } }
    ]
})

tab7 = Table()
tab7.pivotSparkOutput(Interests, InterestCols, trendJson)
from crosstabs.renderers import HTMLRenderer

options = { "startRow": 2, "startCol": 2, "worksheetName": "Req7 Topic Analysis"}
renderTable(tab7, options)