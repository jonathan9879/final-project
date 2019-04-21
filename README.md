# How can I improve my spending habits? 
### By Jessie Lee Delgadillo Newman // Data Analysis Full Time Cohort - February 2019

## Overview
This project is an analysis on personal spending over the years, with the wish of improving in the future. Using personal banking data, statistics, and if necessary ML predictions, the goal of this project is to have a clear view of bad financial habits (if there are any), how they can negatively affect me without a change and what changes I can make to improve my spending habits.

My main hypothesis is that the transactions will be normally distributed:
- Null hypothesis (H0) = The independant variable (transaction amount) of my data (sample of personal transactions) will not be normally distributed.
- Hypothesis (H1) = The independant variable (transaction amount) of my data (sample of personal transactions) will be normally distributed.
- H0 = There isn't a correlation between certain words I send as messages to my girlfriend and the amount I spend.
- H1 = There is a correlation between certain words I send as messages to my girlfriend and the amount I spend.

To test my hypothesis I will use the cientific python library scipy. Specifically the normal test function based on Ralph D'Agostinos and E. S. Pearsons "Biometrika" journal article. Here are the references:
- D’Agostino, R. B. (1971), “An omnibus test of normality for moderate and large sample size”, Biometrika, 58, 341-348
- D’Agostino, R. and Pearson, E. S. (1973), “Tests for departure from normality”, Biometrika, 60, 613-622

The function will return a p-value that is interpreted against an alpha (in this case of 5%) and will find out if the dataset sample significantly deviates from a normal distribution.

## Data Preparation
The dataset comes from the oficial "La Caixa" website. When a user is in it's personal account, he/she can download immediatly a certain amount of transactions in XML format. This is what has been done for this project.
After downloading the dataset, which amounts for a total of 720 entries ranging from 26/07/2017 to 17/04/2019, it was converted to csv using Excel. 

The attributes/columns are as follow, all imported as strings:
- Date
- Concept	
- Category
- Amount
- Type
- Account

Personal information about location has been downloaded too using Google acounts "personal data" import webpage. Probably will be used in the future to better understand financial habits/patterns.
