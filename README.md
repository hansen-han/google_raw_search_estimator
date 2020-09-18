# google-raw-search-estimator
Determine an estimated number of people in the United States who have searched for a given phrase in the past year.  

# Background

# Example

On September 17th, 2020:
```python

search_population = raw_search_estimation("unemployment")
print(search_population)
print("Estimated Search Population (Annually): " + str(search_population))
```
Estimated Search Population (Annually): 21460222.81721452


"All models are wrong, but some are useful"

This estimate of 21 million people for the year using this method is very close to the reported peak of 20.5 million people who were unemployed due to the COVID-19 crisis according to Pew Research, suggesting that this method may actually be useful for estimating the number of people searching for given terms. 

(https://www.pewresearch.org/fact-tank/2020/06/11/unemployment-rose-higher-in-three-months-of-covid-19-than-it-did-in-two-years-of-the-great-recession/#:~:text=Unemployment%20rose%20higher%20in%20three,years%20of%20the%20Great%20Recession&text=The%20COVID%2D19%20outbreak%20and,20.5%20million%20in%20May%202020.) 

# Issues & Limitations

* Highly Variable Search Patterns:
* Innacurate Search Population Assumptions:
