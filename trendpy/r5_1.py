from main_include import *

trendJson = json.load(open(varDefPath + "trend_2017-06-16.json"))
profileJson = json.load(open(varDefPath + "profileReport-2017-06-16.json"))

ax1_51 = TableAxis({
  "Name": "5_1_Customers_per_Topic_Deciles",
  "Version" : "1",
  "SourcePath": "decile",
  "Elements": [
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "Decile 10"], "Condition": "10" },
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "Decile 9"], "Condition": "9" },
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "Decile 8"], "Condition": "8" },
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "Decile 7"], "Condition": "7" },
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "Decile 6"], "Condition": "6" },
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "Decile 5"], "Condition": "5" },
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "Decile 4"], "Condition": "4" },
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "Decile 3"], "Condition": "3" },
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "Decile 2"], "Condition": "2" },
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "Decile 1"], "Condition": "1" },
    { "ElementText": ["Distribution of Customer per Topic (Deciles)", "All"], "Condition": "all" }
   
  ]
})

ax2_51 = TableAxis( {
  "Name": "5_1_Customers_per_Topic_Columns",
  "Version" : "1",
  "Elements": [
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Number of distinct topics"], "Condition": "5.1.customersPerTopicDecilesBefore|*|topicCount" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Number of customer-topic-pairs (CTP)"], "Condition": "5.1.customersPerTopicDecilesBefore|*|CTPCount" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Percentage of CTP"], "Condition": "5.1.customersPerTopicDecilesBefore|*|CTPPercentage" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Cumulative %"], "Condition": "5.1.customersPerTopicDecilesBefore|*|CTPPercentage" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Mean customers per topic"], "Condition": "5.1.customersPerTopicDecilesBefore|*|meanCustomersPerTopic" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Std dev of customers per topic"], "Condition": "5.1.customersPerTopicDecilesBefore|*|stdDevCustomersPerTopic" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Min customers per topic"], "Condition": "5.1.customersPerTopicDecilesBefore|*|minCustomersPerTopic" },
    { "ElementText": ["Latest refresh period", "Before Interest Affinity", "Max customers per topic"], "Condition": "5.1.customersPerTopicDecilesBefore|*|maxCustomersPerTopic" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Number of distinct topics"], "Condition": "5.1.customersPerTopicDecilesAfter|*|topicCount" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Number of customer-topic-pairs (CTP)"], "Condition": "5.1.customersPerTopicDecilesAfter|*|CTPCount" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Percentage of CTP"], "Condition": "5.1.customersPerTopicDecilesAfter|*|CTPPercentage" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Cumulative %"], "Condition": "5.1.customersPerTopicDecilesAfter|*|CTPPercentage" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Mean customers per topic"], "Condition": "5.1.customersPerTopicDecilesAfter|*|meanCustomersPerTopic" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Std dev of customers per topic"], "Condition": "5.1.customersPerTopicDecilesAfter|*|stdDevCustomersPerTopic" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Min customers per topic"], "Condition": "5.1.customersPerTopicDecilesAfter|*|minCustomersPerTopic" },
    { "ElementText": ["Latest refresh period", "After Interest Affinity", "Max customers per topic"], "Condition": "5.1.customersPerTopicDecilesAfter|*|maxCustomersPerTopic" }
  ]
})

tab51 = Table()
tab51.pivotSparkOutput(ax1_51, ax2_51, trendJson)
from crosstabs.renderers import HTMLRenderer
tab51.TableTitles = ["Table 5.1", "Distribution of customers per Topic Quantile (All Customers)"]

options = { "startRow": 2, "startCol": 2, "worksheetName": "Req5 Topic Dynamics"}
renderTable(tab51, options)
