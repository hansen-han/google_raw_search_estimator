from pytrends.request import TrendReq

def raw_search_estimation(keyword):
    '''
    Description
    -----------
    Provides an estimate of how many people in the United States search for 
    the provided keyword annually. Estimate is calculated by comparing the
    relative search frequency of the keyword to search volumes of various
    standardized tests in the US (GMAT, GRE, LSAT, MCAT, SAT) and their 
    respective search populations (how many people take the exam per year).


    Disclaimer: Please use this at your own risk. There are so many reasons
    why this estimate is incomplete such as:

    -Search frequency of a given keyword can vary dramatically, (ie. the same
    person preparing for the MCAT will make many of the search queries throughout
    the year vs. someone looking up the lyrics for a song they heard in the gas
    station will likely not make repeated searches that year)
    -Various people who search up the exam do not actually sit for the exam
    (ie. parents, family, advisors, etc.), which means the populations used to
    estimate to search population also are not reflective of the actual
    search population.  


    Parameters
    ----------
    keyword: string
        The search phrase you want to estimate the raw search population for.

    Returns
    -------
    estimate: float
        The estimated number of people in the United States who have searched for
        that phrase in the past year. 

    '''

    gmat_students = 200000 #Estimated (https://www.gmac.com/gmat-other-assessments/about-the-gmat-exam/the-gmat-advantage)
    gre_students = 574677 #As of 2016 (https://www.ets.org/s/gre/pdf/snapshot_test_taker_data_2016.pdf)
    lsat_students = 105883 #As of 2014 (https://lawschooli.com/how-many-people-take-the-lsat-each-year/)
    mcat_students = 80000 #https://www.aamc.org/system/files/2020-07/services_mcat_using-mcat-data-in-2021-medical-student-selection-guide_07082020_0.pdf
    sat_students = 2000000

    kw_list= ['LSAT', 'GRE', 'SAT', keyword]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='US', gprop ='')

    r1 = pytrends.interest_over_time()
    r1 = r1.drop(axis=1, labels = ['isPartial'])

    estimates = []
    estimates.append(lsat_students/r1[0])
    estimates.append(gre_students/r1[1])
    estimates.append(sat_students/r1[2])
    estimate = (sum(estimates)/len(estimates))*r1[3])
    return estimate



    
