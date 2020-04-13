![imagen](https://github.com/Flori-87/data-analysis-pipeline/blob/master/input/image.PNG)

# Analysis of world happiness data using pipelines


#### Project goal

The main goal of this project is to analyze a dataset using data analysis pipelines. For that purpose, a [csv file](https://www.kaggle.com/unsdsn/world-happiness) containing scores on topics that affect people's happiness will be used. This main goal will be achieve by performing the next tasks:
- Data cleaning and wrangling and dataset enrichment. 
- Statistic analysis using two parameters to filter the dataset. 
- Report with the analysis printed in console and saved in a pdf file.


#### Methods

The dataset about world happiness will be cleaned and then enriched using APIs. APIs used in this project provide data about income and weather in the analyzed countries. Moreover, a column with the ISO-alpha3 code for each country will be added through web scraping.
The analysis will be performed based on two parameters that will be received from console. The dataset will be filtered by those parameters and statistic analysis such as mean, maximum and minimum values will be calculated. Bar graphs showing the maximum scores on the analyzed topics for each region will be generated. Results will be printed in console and a report containing bar graphs will be generated in a pdf file.
