from main_include import *

trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))
dates = ['2017-05-11','2017-06-01','2017-06-08','2017-06-16']
inputJson = [ [json.load(open(varDefPath + "trend_" + d + ".json")), 
        json.load(open(varDefPath + "profileReport-" + d + ".json", "r"))] for d in dates]

o2AudienceCols = TableAxis( {
    "Name": "o2AudienceAll",
    "Version": 1,
    "Elements": [
        { "ElementText": ["Refresh Period", "Active Customers *", "Count"], "Condition": "6.1.o2AudienceAssignment|*|count" },
        { "ElementText": ["Refresh Period", "% Active Customers", "%"], "Condition": "6.1.o2AudienceAssignment|*|percentage", "DataFormatting" : {"NumberFormat":"0.0%"} }
    ]
})

o2Audiences = TableAxis({
    "Name": "o2Audiences",
    "Version" : "1",
    "Elements": [
        { "ElementGroup": {
            "ElementText": ["O2 Audiences Assignment"],
            "SourceElements": "6.1.o2AudienceAssignment|*|o2Audience",
            "Formatting" : [{}, {"font": {"bold": "False"}, "alignment": {"horizontal":"left"}}],
            "Operations": [
                {"Type": "Sort", "Order": "asc"}
            ] } }
    ]
})

o2AudiencesAll = TableAxis({
    "Name": "o2AudiencesAll",
    "Version" : "1",
    "Elements": [
        { "ElementText": ["O2 Audiences Assignment", "Customers with audiences assigned (Valid N)"], "Condition": "6.2.activeUsersWithO2Audiences|activeUsersWithO2Audiences" }
    ]
})

tab6 = Table()
tab6.pivotSparkOutput(o2Audiences, o2AudienceCols, trendJson)
from crosstabs.renderers import HTMLRenderer
options = { "startRow": 1, "startCol": 2, "worksheetName": "Req6 Audience Analysis"}
renderTable(tab6, options)