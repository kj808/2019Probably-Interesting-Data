#Resources
#--EM Alg
#https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm#Gaussian_mixture
#https://scikit-learn.org/stable/modules/mixture.html#expectation-maximization
#--Mix Model
#https://en.wikipedia.org/wiki/Mixture_model#Gaussian_mixture_model
#--Multivariate Function
#https://en.wikipedia.org/wiki/Multivariate_normal_distribution
#--Covariance Matrix
#https://en.wikipedia.org/wiki/Covariance_matrix
#--Normal Distribution
#https://en.wikipedia.org/wiki/Normal_distribution

#Gauss Distribution
def gaussDist(x,mean,variance):
    import numpy as np
    pi=float(3.14)
    exponent=np.negative(np.divide(((x-mean)**2),(2*variance)))
    divider=np.sqrt(2*pi*variance)
    
    probability=np.divide(np.exp(exponent),divider)
    return probability
    
    
#Mixed Models
#Must pass defined means and variables in format: [(mean,var),(mean,var),(mean,var)]
def gaussMixed(data,meanvar):
    import numpy as np
    featureprobs=[]
    for mean,variance in meanvar:
    #calculate the gausian distribution for each point
        values=gaussDist(data, mean, variance)
        featureprobs.append(values)
    return featureprobs
    
    
#Expectation-Maximization
#Two steps
#E
    #For all steps in kmeans cluster selection, use gaussian distribution


#M