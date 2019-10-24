# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:05:22 2019

@author: Vaibhav
"""
import pandas as pd

def delta_ratio(vector_1, vector_2):
    """
    Returns a list that contains
    ratios of change of vector_1 w.r.t vector_2
    """
    if (len(vector_1) == 1):
        return vector_1[0] / vector_2[0]
    
    else:
        ratios = []
        vector_1 = delta(vector_1)
        vector_2 = delta(vector_2)
        for index in range(len(vector_1)):
            delta_1 = vector_1[index]
            delta_2 = vector_2[index]
            ratios.append(delta_1 / delta_2)
        return ratios
    
def delta(vector):
    """
    Calculates the difference b/w adjacent elements 
    in a vector and returns it as a list
    """
    if (len(vector) <= 1):
        return 0
    
    else:
        result_vector = []
        for index in range(len(vector)-1):
            result_vector.append(vector[index+1] - vector[index])
        return result_vector
    
def normalize_ratios(ratios):
    """
    This normalize each tuple in ratios by
    dividing each element in the tuple by last 
    last element in that tuple. This is in place.
    """
    tuple_len = len(ratios[0])
    for tup_index in range(len(ratios)):
        for ratio_index in range(tuple_len):
            ratios[tup_index][ratio_index] /= ratios[tup_index][-1]
            
    
def weighted_mean(vector):
    """
    Returns the weighted mean of a vector based on
    weights provided by delta_weightage_mapping
    """
    wtd_mean = vector[0];
    for index in range(1, len(vector)-1):
        w1, w2 = delta_weightage_mapping(wtd_mean, vector[index])
        wtd_mean = (w1 * wtd_mean) + (w2 * vector[index])
    return wtd_mean

def delta_weightage_mapping(val_1, val_2):
    """
    Calculate the necessary weights to find the mean
    of the parameters. Can be modified to accomodate 
    the volatility in the data
    """
    percentage_diff = (val_2 - val_1) / val_1
    #percentage_diff = abs(percentage_diff)
    w1 = 0.7
    w2 = 0.3 + (percentage_diff)
    return (w1, w2)

def predict_next_without_contr(vector):
    """
    Predict the next value of the vector based on 
    delta_weightage_mapping and without taking into 
    consideration any factor
    """
    delta_vector = delta(vector)
    #Calculate mean value of change
    wtd_mean_change = weighted_mean(delta_vector)
    #add wtd_mean_change to last val of vector
    predicted_val = vector[-1] + wtd_mean_change
    return predicted_val

def predict_contribution(ratios):
    """
    Predict the contribution of each factor based 
    on delta_weightage_mapping
    """
    normalize_ratios(ratios)
    factors_count = len(ratios[0])
    factor_contributions = []
    for factor in range(factors_count):
        fact_contr_values = [ratio[factor] for ratio in ratios]
        fact_contr = predict_next(fact_contr_values)
        factor_contributions.append(fact_contr)
    return factor_contributions

def predict_next(data):
    """
    Predict next value based on all the factors
    Assume last value of each row is value to be predicted.
    And all other values are factors
    """
    factor_values = [row[:-1] for row in data]
    normalize(factor_values)
    factor_contributions = predict_contributions(factor_values)
    
#predict val of delta R / delta D
    
    
    

