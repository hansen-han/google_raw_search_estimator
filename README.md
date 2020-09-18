# Google Raw Search Estimator
Determine an estimated number of people in the United States who have searched for a given phrase in the past year.  

# Background


# Approach


# Issues & Considerations

* Search Frequency:
* Underestimating Search Population:


# Example
*"All models are wrong, but some are useful"*

On September 17th, 2020:
```python
search_population = raw_search_estimation("unemployment")
print("Estimated Search Population (Annually): " + str(search_population))

Estimated Search Population (Annually): 21460222.81721452
```


The estimate of 21.4 million people for the year using this method is remarkably close to the reported peak of **20.5 million** people who were unemployed in May due to the COVID-19 crisis according to the [Pew Research Center](https://www.pewresearch.org/fact-tank/2020/06/11/unemployment-rose-higher-in-three-months-of-covid-19-than-it-did-in-two-years-of-the-great-recession/#:~:text=Unemployment%20rose%20higher%20in%20three,years%20of%20the%20Great%20Recession&text=The%20COVID%2D19%20outbreak%20and,20.5%20million%20in%20May%202020.). This suggests this tool may in fact be useful for estimating the number of people searching for given terms and could have high-impact applications in both academic and market research contexts.


# To-Do
* Creating a range of values for the estimate.
* Using different reference populations besides standardized testing
 