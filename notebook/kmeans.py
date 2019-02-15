#Assign ALL points to closest centroid     
def assign(data,centroids):
    #Keeps track of when to stop
    changed=True
    while changed==True:
        #for all points
        for point in data:
            #create an array with all the distances from the point to the centroids
            dist=np.sqrt(np.sum((point[:,1:]-centroids)**2, axis=1))
            #Grab the centorid that's closest
            cluster=np.argmin(dist)    
            #Record the closest centroid cluster
            point[0]=cluster
        #update centroids
        keepgoing=update(data, labels, centroid)
    
    
def update(data, labels, centroid):
    change=False
    #Calculate the totals for each different clusters
    for i in str(len(centroid)):
        item=np.mean(data[np.where(data[:,0]==i)], axis=0)
        #If there was a change
        if centroid[i]!=item:
            centroid[i]=item
            change=True
    #Check if centroid already located in calculated spot
    if change==True:
        return True
    else: #keep going!
        return False

    
def kmean(data, k):
    import random
    #Create column representing clusters to the data
    clusterlist = np.zeros_like((1,len(data)))
    newdata=np.append(clusterlist, data, axis=1)
    print(newdata)
    
    #Create the list of centroids with random starting locations
    legnthy=len(data[0])
    print(legnthy)
    centroids = np.random.rand(k,len(data[0]))
       
    #Start assigning the points to clusters
    assign(newdata, centroids)
    return newdata
    
