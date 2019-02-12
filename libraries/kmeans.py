#Assign ALL points to closest centroid
def assign(data,labels,centroid):
    #Keeps track of when to stop
    keepgoing=True
    while keepgoing==False:
        #for all points
        for point in data:
            total=0
            centCloseness={}
            #for for each centroid
            for cent in centroid:
                #calculate the euclidean distance and record
                for d in len(data[0]):
                    total+=(point[d]-cen[d])**2
                total=sqrt(total)
                cenCloseness[cent[0]]=total
                total=0
            #Check which is closest and apply
            closest=min(cenCloseness, key=cenCloseness.get)
            labels[point] = closest

        #update centroids
        keepgoing=update(data, labels, centroid)
    
    
def update(data, labels, centroid):
    #Readjust centroids to mean of cluster
    #Keep track of means
    for cent in centroid:
        dimension=[]
        for i in len(data[0]):
            dimension.append(0)
        meanCounts[cent]=dimension
    #Calculate the mean location
    for point in data:
        for i in len(point):
            meanCounts[labels[point]]+=point
    #Calculate the final mean
    for cent in centroid:
        total=labels.count(cent)
        if total!=0:
            meanCounts[cent]=meanCounts[cent]/total
        else:
            #Keep centroid in the same place
            meanCounts[cent]=-1
        
    #Check if centroid already located in calculated spot
    for item in meanCounts.values():
        if item!=-1 or item!=0:
            return True
        else: #keep going!
            return False

    
def kmean(data, k):
    import random
    #Grab vector dimension
    dimension=len(data[0])
    #Create column representing clusters
    clusterlist={}
    centroidLocations = []
    #For all k, randomize starting position
    for i in k:
        tup=[]
        for d in dimension:
            tup.append(random.randint)
        centroidLocations.append((k, tup))
        
    assign(data, centroidLocations, clusterlist)
    return (data, centroidLocations, clusterlist)
    
