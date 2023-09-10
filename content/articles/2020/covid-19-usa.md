---
title: 'COVID-19 USA Analysis: effects of the lack of lockdown'
publishDate: '2020-05-29T20:00:00'
categories: Mathematics
tags:
- Mathematics
- COVID 19
slug: covid-19-usa
---

The USA currently stands at 1.76 million COVID-19 cases. That's more than the next 5 nations combined. A large number of these cases are due to government inaction against the virus. The lack of a concerted lockdown across the country is also to blame. Here's a graph showing the daily number of cases of COVID-19 in the USA.

<center>![Daily covid cases]({static}res/covid-19-usa/covid-cases-daily.png)</center><br>
<center><sup>Source: Google</sup></center><br>
Notice something strange? After reaching saturation, the curve shows a weird oscillatory behaviour. Is there a pattern to this? Let's overlay some week markers on the data to get a better feel of it.

<center>![covid weekly]({static}res/covid-19-usa/covid-weekly.png)</center><br>
<center><sup>Source: Our World in data\*</sup></center><br>
The pattern is much more obvious now. It is clearly visible that reported cases are at their lowest on the first few days of the week and they are at their highest during the weekends. Summing up the data proves this (quite dramatically)

<center>![covid sum]({static}res/covid-19-usa/covid-sum.png)</center><br>
<center><sup>Sum of cases/day from 1 Mar to today</sup></center><br>
This data now allows us to paint a picture. The mean time of incubation of Coronavirus is 5.1 days<sup>[1]</sup>. One inference is that more people are going out on Sunday night and getting tested on Friday morning. This is not very probable as most of the hospitality business (malls, hotels etc) is shut. The more likely reason is that *people are going to work on a Monday and Tuesday, displaying symptoms in a week and then getting tested at the end of the week*. **This situation would not arise if a nationwide lockdown was implemented**. This is the key reason behind the large number of cases and also behind the recurring patterns of occurence of new cases.

The analysis also presents several lessons for nations in the nascent phase of the virus: India has lifted it's lockdown just as the number of cases are peaking. While isolation of zones where infected patients have been found continues, urging people to return to work in these times may present the same pattern as shown above.

-------------

\* Our World in Data recorded a spike of ~48000 cases on April 26. This seemed suspicious, which is why that data point was substituted by the Google/Wikipedia data for the same date.

\[1\]: Lauer, Stephen A., et al. “The Incubation Period of Coronavirus Disease 2019 (COVID-19) From Publicly Reported Confirmed Cases: Estimation and Application.” Annals of Internal Medicine, vol. 172, no. 9, Mar. 2020, pp. 577–82. acpjournals.org (Atypon), doi:[10.7326/M20-0504](https://doi.org/10.7326/M20-0504).
