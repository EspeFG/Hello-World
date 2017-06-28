from main_include import *

ax2_1 = TableAxis(json.load(open(varDefPath + "Trend_scripts/Req_2_1_rows.json", "r")))

ax2 = TableAxis(json.load(open(varDefPath + "Trend_scripts/Req_2_1_cols.json", "r")))

axsum = TableAxis(json.load(open(varDefPath + "Trend_scripts/Req_2_2_cols.json", "r")))

trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))
dates = ['2017-05-11','2017-06-01','2017-06-08','2017-06-16']
inputJson = [ [json.load(open(varDefPath + "trend_" + d + ".json")), 
				json.load(open(varDefPath + "profileReport-" + d + ".json", "r"))] for d in dates]

tab = Table()
tab.pivotSparkOutput(ax2_1, ax2, trendJson)
tab.RowHeaders = ["Week Number","Date"]
tab.TableHeaders = ["Latest Refresh"]
tab.TableTitles = ["Table 2.1", ("Weekly View", 2)]
tab.TableNotes = [("All figures on this sheet are before Interest Affinity", 3)]
from crosstabs.renderers import HTMLRenderer
html = HTMLRenderer.Render(tab, {})
display(HTML(html))
tab = Table()
for j in inputJson:
    tab.addElasticSearchColumn(j, axsum, "&nbsp;")   
tab.TableTitles = ["Table 2.2", "Summary Action View (All Customers)"]
tab.SuppressRowLabels = True    
tab.SwapAxis()

options = { "startRow": 2, "startCol": 2, "worksheetName": "Req 2 Customer Activity"}
renderTable(tab, options)