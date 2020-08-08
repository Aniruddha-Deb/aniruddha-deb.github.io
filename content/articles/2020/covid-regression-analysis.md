Title: COVID 19 regression analysis 
Date: 2020-05-06 21:30
Category: Mathematics
Tags: Mathematics, COVID 19
Slug: covid-regression-analysis

![regression]({static}res/covid-regression-analysis.png)
This is a regression analysis attempt for the COVID-19 spread data. The graphs represent total cases per day. The Orange graph is USA, the smaller graph on the left is China and the graph on the right is India. A Standard gaussian curve of the form $Ae^{-b(x-c)^2}$ is fitted on the data manually (They don't fit the USA data very well though)

The y-axis scale is 5000 cases/large division and 1000 cases/small division. Currently, 50 represents today's date for India i.e. May 6. Looking at a predicted worst case curve, we see it peaking somewhere around May 20 ($\pm$ 5 days). It should go down post that point. The total number of cases is the integral under the curve. For a gaussian distribution, it comes out to be $a\sqrt{\frac \pi b}$. Taking half of this (before the peak), we end up with $\approx 130,000$ cases. India can expect to see this number $\pm$ 10% of cases by May end and a overall of $\approx 200,000 \pm 10%$ cases by June end, worst case. 

Let's hope I'm wrong here and we can flatten the curve sooner than expected.
