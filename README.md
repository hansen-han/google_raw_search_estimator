# Google Raw Search Estimator
Provides an estimate of how many people in the United States search for the provided keyword annually. Estimate is calculated by comparing the relative search frequency of the keyword to search volumes of various standardized tests in the US (GMAT, GRE, LSAT, MCAT, SAT) and their respective search populations (how many people take the exam per year).

Relative search frequency data is from Google Trends via [pytrends](https://github.com/GeneralMills/pytrends). 

# Rationale & Approach
I thought of this project when I discovered Google Trends while studying for the GRE. While powerful and useful, Google Trends only provides the relative search frequency for any given keyword (relative to itself, or other keywords it is being compared to). This means that if you are doing market research for say a new product idea such as "dog sweaters", you can only see how search patterns have changed, not the number of people who have actually been searching. I noticed that I had been searching for the GRE relatively often, and thought that given the number of people who took the GRE and the relative search frequency for "GRE" against "dog sweaters", you could get a rough estimate of how many people are searching for "dog sweaters":


People Interested in the GRE = Annual Test Takers = [574,677](https://www.ets.org/s/gre/pdf/snapshot_test_taker_data_2016.pdf) people  

Google Trends Relative Interest ("GRE") = 75  

Google Trends Relative Interest ("dog sweaters") =  3  

  
  

*(People Interested in Dog Sweaters)/(People Interested in the GRE) = (Google Trends Relative Interest ("dog sweaters"))/(Google Trends Relative Interest ("GRE"))*  

*People Interested in Dog Sweaters = (3/75) * (547,677 people)*  

*People Interested in Dog Sweaters = 21,907.08 people*  


Expanding this idea to a combination of other standardized tests (GMAT, GRE, LSAT, MCAT, SAT) and the number of people who are known to take them annually, I made an easy python tool to estimate population sizes for certain keyword searches. 

# Example
On September 17th, 2020:
```python
search_population = raw_search_estimation("unemployment")
print("Estimated Search Population (Annually): " + str(search_population))

Estimated Search Population (Annually): 21460222.81721452
```

The estimate of 21.4 million people for the year using this method is remarkably close to the reported peak of **20.5 million** people who were unemployed in May due to the COVID-19 crisis according to the [Pew Research Center](https://www.pewresearch.org/fact-tank/2020/06/11/unemployment-rose-higher-in-three-months-of-covid-19-than-it-did-in-two-years-of-the-great-recession/#:~:text=Unemployment%20rose%20higher%20in%20three,years%20of%20the%20Great%20Recession&text=The%20COVID%2D19%20outbreak%20and,20.5%20million%20in%20May%202020.). This suggests this tool may in fact be useful for estimating the number of people searching for given terms and could have high-impact applications in both academic and market research contexts.

# Issues & Considerations
*"All models are wrong, but some are useful"*

Generally, the two variables that contribute to search volume for a given keyword are 1) the number of people who search (population size) and 2) how frequently they search (interest level).

This approach is inherently useful because it does not account for the interest level of 

The similarity between how many people are estimated to searching for "unemployment" this year and how many people were actually unemployed in the United States may simply be a coincidence. On the other hand, one could speculate that it may have been accurate because the reference for the estimate (standardized tests) and the query "unemployment" had similar high interest levels.

# Future Work
* Returning a range of values instead of a single value for the estimate
* Exploring ways to account and quantify interest levels, possibly by finding additional reference data
 
