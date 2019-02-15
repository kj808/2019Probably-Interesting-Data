def assign(data,centroids):
    import numpy as np
    #print("----ASSIGN----")
    #for all points
    for point in data:
        #create an array with all the distances from the point to the centroids
        dist=np.sqrt(np.sum((point[1:]-centroids)**2, axis=1))
        #Grab the centorid that's closest
        cluster=np.argmin(dist)    
        #Record the closest centroid cluster
        point[0]=cluster
    
    
def update(data,centroids):
    import numpy as np
    #print("----UPDATE----")
    change=False
    #Calculate the totals for each different clusters
    for i in range(len(centroids)):
        filtered=data[data[:,0]==i]
        item=np.mean(filtered[:,1:], axis=0)
        #If there was a change
        if not np.array_equal(centroids[int(i)],item) and not np.isnan(item).any():
            centroids[int(i)]=item
            change=True
    #Check if centroid already located in calculated spot
    if change==True:
        return True
    else: #keep going!
        return False

    
def kmean(data, k):
    import random
    import numpy as np
    #Create column representing clusters to the data
    clusterlist = np.zeros((1,(len(data))))
    newdata=np.append(arr=clusterlist.T,values=data, axis=1)
    
    #Create the list of centroids with random starting locations
    columns=len(data[0])
    cents=k
    centroids = np.random.rand(cents,columns)
       
    #Start assigning the points to clusters
    #Keeps track of when to stop
    changed=True
    while changed==True:
        assign(newdata, centroids)
        changed=update(newdata, centroids)
    
    return (newdata,centroids)
