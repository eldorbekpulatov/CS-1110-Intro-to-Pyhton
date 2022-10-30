# a6.py
# Eldor Bekpulatov (eb 654)
# November 16th, 2016
"""Classes to perform KMeans Clustering"""

import math
import random
import numpy
import copy

# HELPER FUNCTIONS FOR ASSERTS GO HERE
def is_point(thelist):
    """Return: True if thelist is a list of int or float"""
    if (type(thelist) != list):
        return False
    
    # All float
    okay = True
    for x in thelist:
        if (not type(x) in [int,float]):
            okay = False
    
    return okay

def is_content(con, dim):
    """Return: True if the contents is a valid list of point
                    with correct dimensions; False otherwise
        
        Prameter con: Contents of the dataset
        Precondition: anything
        
        Parameter dim: dimension of the points
        Precondition: int >0"""
        
    if con==None:
        return True
    if type(con)==list:
        boo=[]
        for x in con:
            boo.append(is_point(x))
        if False in boo:
            return False
        
        i=0
        l=[]
        for x in con:
            l.append(len(con[i])==dim)
            i+=1
        if False in l:
            return False
        return True

def is_valid_list(ds, lis, k):
    """Return: True if seed_inds is a valid k list
    
    Parameter lis: list of indices to check if valid
    Precondition: Can be anything
    
    Parameter k: Number of lusters
    Precondition: Is an int >0 and lees than Dataset.getSize()
    
    Parameter ds: Dataset
    Precondition: instance of Dataset
    """
    
    if type(lis)==list:  
        if len(lis)==k:
            for x in lis:
                x<=ds.getSize()
        return True
    else:
        return False

# CLASSES
class Dataset(object):
    """Instance is a dataset for k-means clustering.
    
    The data is stored as a list of list of numbers
    (ints or floats).  Each component list is a data point.
    
    Instance Attributes:
        _dimension: the point dimension for this dataset
            [int > 0. Value never changes after initialization]
        
        _contents: the dataset contents
            [a 2D list of numbers (float or int), possibly empty]:
    
    ADDITIONAL INVARIANT:
        The number of columns in _contents is equal to _dimension.  
        That is, for every item _contents[i] in the list _contents, 
        len(_contents[i]) == dimension.
    
    None of the attributes should be accessed directly outside of the class
    Dataset (e.g. in the methods of class Cluster or KMeans). Instead, this class 
    has getter and setter style methods (with the appropriate preconditions) for 
    modifying these values.
    """
    
    def __init__(self, dim, contents=None):
        """Initializer: Creates a dataset for the given point dimension.
        
        Note that contents (which is the initial value for attribute _contents)
        is optional. When assigning contents to the attribute _contents the initializer
        COPIES the  list contents. If contents is None, the initializer assigns 
        _contents an empty list.
        
        Parameter dim: the initial value for attribute _dimension.  
        Precondition: dim is an int > 0.
        
        Parameter contents: the initial value for attribute _contents (optional). 
        Precondition: contents is either None or is a 2D list of numbers (int or float). 
        If contents is not None, then contents if not empty and the number of columns of 
        contents is equal to dim.
        """
        assert type(dim)==int and dim>0
        assert is_content(contents, dim)
        
        if contents==None:
            contents=[]
        np=copy.deepcopy(contents)
        """np=[]
        i=0
        for y in contents:
            nl=[]
            for x in contents[i]:
                nl.append(x)
            np.append(nl)
            i+=1"""
        self._contents=np
        self._dimension=dim
        
    
    def getDimension(self):
        """Returns: The point dimension of this data set.
        """
        return self._dimension
    
    def getSize(self):
        """Returns: the number of elements in this data set.
        """
        size =len(self._contents)
        return size
    
    def getContents(self):
        """Returns: The contents of this data set as a list.
        
        This method returns the attribute _contents directly.  Any changes made to this 
        list will modify the data set.  If you want to access the data set, but want to 
        protect yourself from modifying the data, use getPoint() instead.
        """
        return self._contents
    
    def getPoint(self, i):
        """Returns: A COPY of the point at index i in this data set.
        
        Often, we want to access a point in the data set, but we want a copy
        to make sure that we do not accidentally modify the data set.  That
        is the purpose of this method.  
        
        If you actually want to modify the data set, use the method getContents().
        That returns the list storing the data set, and any changes to that
        list will alter the data set.
        
        Parameter i: the index position of the point
        Precondition: i is an int that refers to a valid position in 0..getSize()-1
        """
        #ASSERT HERE
        assert type(i)==int and 0<=i<=self.getSize()-1
        cop=[]
        for c in self.getContents()[i]:
            cop.append ((c))
        return cop
    
    def addPoint(self, point):
        """Adds a COPY of point at the end of _contents.
        
        This method does not add the point directly. It adds a copy of the point.
        
        Parameter point: the point to add
        Precondition: point is a list of numbers (int or float), len(point) = _dimension.
        """
        assert is_point(point)
        
        newp=[]
        for x in point:
            newp.append((x))
        self._contents.append(newp)
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._contents)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)


class Cluster(object):
    """An instance is a cluster, a subset of the points in a dataset.
    
    A cluster is represented as a list of integers that give the indices
    in the dataset of the points contained in the cluster.  For instance,
    a cluster consisting of the points with indices 0, 4, and 5 in the
    dataset's data array would be represented by the index list [0,4,5].
    
    A cluster instance also contains a centroid that is used as part of
    the k-means algorithm.  This centroid is an n-D point (where n is
    the dimension of the dataset), represented as a list of n numbers,
    not as an index into the dataset.  (This is because the centroid
    is generally not a point in the dataset, but rather is usually in between
    the data points.)
    
    Instance Attributes:
        _dataset: the dataset this cluster is a subset of  [Dataset]
        
        _indices: the indices of this cluster's points in the dataset  [list of int]
        
        _centroid: the centroid of this cluster  [list of numbers]
    
    ADDITIONAL INVARIANTS:
        len(_centroid) == _dataset.getDimension()
        0 <= _indices[i] < _dataset.getSize(), for all 0 <= i < len(_indices)
    """
    
    # Part A
    def __init__(self, ds, centroid):
        """Initializer: Creates a new empty cluster with the given centroid.
        
        Remember that a centroid is a point and hence a list.  The initializer COPIES
        the centroid; it does not use the original list.
        
        IMPORTANT: READ THE PRECONDITION OF ds VERY CAREFULLY
        
        Parameter ds: the Dataset for this cluster
        Precondition: ds is a instance of Dataset OR a subclass of Dataset
        
        Parameter centroid: the centroid point (which might not be a point in ds)
        Precondition: centroid is a list of numbers (int or float),
          len(centroid) = ds.getDimension()
        """
        assert isinstance(ds, Dataset) or issubclass(ds, Dataset)
        assert is_point(centroid) and len(centroid)==ds.getDimension()
        cen=[]
        for x in centroid:
            cen.append(x)
        self._dataset=ds
        self._centroid=cen
        self._indices=[]

    def getCentroid(self):
        """Returns: the centroid of this cluster.
        
        This getter method is to protect access to the centroid.
        """
        return self._centroid
    
    def getIndices(self):
        """Returns: the indices of points in this cluster
        
        This method returns the attribute _indices directly.  Any changes
        made to this list will modify the cluster.
        """
        return self._indices
    
    def addIndex(self, index):
        """Adds the given dataset index to this cluster.
        
        If the index is already in this cluster, then this method leaves the
        cluster unchanged.
        
        Parameter index: the index of the point to add
        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int in the range 0.._dataset.getSize()-1.
        """
        assert type(index)==int and 0<=index<=self._dataset.getSize()-1
        if index not in self._indices:
            self._indices.append(index)
    
    def clear(self):
        """Removes all points from this cluster, but leave the centroid unchanged.
        """
        self._indices=[]
    
    def getContents(self):
        """Returns: a new list containing copies of the points in this cluster.
        
        The result is a list of list of numbers.  It has to be computed from
        the indices.
        """
        nl=[]

        for x in self._indices:
            nl.append(copy.deepcopy(self._dataset.getPoint(x)))
        return nl
    
    # Part B
    def distance(self, point):
        """Returns: The euclidean distance from point to this cluster's centroid.
        
        Parameter point: the point to compare to this cluster's centroid
        Precondition: point is a list of numbers (int or float),
          len(point) = _ds.getDimension()
        """
        assert is_point(point)
        assert len(point) ==self._dataset.getDimension()
        
        l=[]
        for x in range(0, len(point)):
            l.append((point[x]-self._centroid[x])**2)
        return math.sqrt(sum(l))
    
    def updateCentroid(self):
        """Returns: Trues if the centroid remains unchanged; False otherwise.
        
        This method recomputes the _centroid attribute of this cluster. The
        new _centroid attribute is the average of the points of _contents
        (To average a point, average each coordinate separately).  
        
        Whether the centroid "remained the same" after recomputation is determined 
        by the function numpy.allclose().  The return value should be interpreted
        as an indication of whether the starting centroid was a "stable" position 
        or not.
        
        If there are no points in the cluster, the centroid. does not change.
        """
        oldcen=[]
        for x in self._centroid:
            oldcen.append(x)
        
        if self.getContents()==0:
            return True
        else:
            i=0
            l=[]
            for t in range (0, len(self.getContents()[0])):
                m=[]
                for x in self.getContents():
                    m.append(x[i])
                i+=1
                l.append(m)
            centroid=[]
            for x in l:
                centroid.append(sum(x)/float(len(x)))
            self._centroid=centroid
            return numpy.allclose(self.getCentroid(), oldcen)
            
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._centroid)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)


class ClusterGroup(object):
    """An instance is a set of clusters of the points in a dataset.
    
    Instance Attributes:
        _dataset: the dataset which this is a clustering of     [Dataset]
        
        _clusters: the clusters in this clustering (not empty)  [list of Cluster]
    """
    
    # Part A
    def __init__(self, ds, k, seed_inds=None):
        """Initializer: Creates a clustering of the dataset ds into k clusters.
        
        The clusters are initialized by randomly selecting k different points
        from the database to be the centroids of the clusters.  If seed_inds
        is supplied, it is a list of indices into the dataset that specifies
        which points should be the initial cluster centroids.
        
        IMPORTANT: READ THE PRECONDITION OF ds VERY CAREFULLY
        
        Parameter ds: the Dataset for this cluster group
        Precondition: ds is a instance of Dataset OR a subclass of Dataset
        
        Parameter k: The number of clusters (the k in k-means)
        Precondition: k is an int, 0 < k <= ds.getSize()
        
        Parameter seed_inds: the INDEXES of the points to start with
        Precondition: seed_inds is None, or a list of k valid indices into ds.
        """
        assert isinstance(ds, Dataset) 
        assert type(k)==int and 0<k<=ds.getSize()
        assert seed_inds==None or is_valid_list(ds, seed_inds, k)
        
        clcen=[]
        clus=[]

        if seed_inds==None:
            randints=random.sample(range(0,ds.getSize()-1), k)
            for ind in randints: 
                clcen.append(ds.getContents()[ind])
        
        if type(seed_inds)==list:
            for h in seed_inds:
                clcen.append(ds.getContents()[h])
                
        for c in clcen:
            clus.append(Cluster(ds, c))
            
        self._dataset=ds
        self._cluster=clus
        
    
    def getClusters(self):
        """Returns: The list of clusters in this object.
        
        This method returns the attribute _clusters directly.  Any changes
        made to this list will modify the set of clusters.
        """ 
        return self._cluster

    # Part B
    def _nearest_cluster(self, point):
        """Returns: Cluster nearest to point
    
        This method uses the distance method of each Cluster to compute the distance 
        between point and the cluster centroid. It returns the Cluster that is 
        the closest.
        
        Ties are broken in favor of clusters occurring earlier in the list of 
        self._clusters.
        
        Parameter point: the point to match
        Precondition: point is a list of numbers (int or float),
          len(point) = self._dataset.getDimension().
        """
        assert is_point(point)
        dist=[]
        for x in self.getClusters():
            dist.append(x.distance(point))
        i=dist.index(min(dist))
        return self.getClusters()[i]
        
    
    def _partition(self):
        """Repartitions the dataset so each point is in exactly one Cluster.
        """
        # First, clear each cluster of its points.  Then, for each point in the
        # dataset, find the nearest cluster and add the point to that cluster.
        
        for y in self.getClusters():
            y.clear()
        for x in range(0, self._dataset.getSize()):
            cl=self._nearest_cluster(self._dataset.getPoint(x))
            cl.addIndex(x)
    
    # Part C
    def _update(self):
        """Returns:True if all centroids are unchanged after an update; False otherwise.
        
        This method first updates the centroids of all clusters'.  When it is done, it
        checks whether any of them have changed. It then returns the appropriate value.
        """
        lis=[]
        for x in self.getClusters():
            lis.append(x.updateCentroid())
        if False in lis:
            return False
        else:
            return True
            
    def step(self):
        """Returns: True if the algorithm converges after one step; False otherwise.
        
        This method performs one cycle of the k-means algorithm. It then checks if
        the algorithm has converged and returns True or False
        """
        # In a cycle, we partition the points and then update the means.
        # IMPLEMENT ME
        self._partition()
        x=self._update()
        if x==True:
            return True
        else:
            return False
    
    # Part D
    def run(self, maxstep):
        """Continues clustering until either it converges or reaches maxstep steps.
        
        The stopping condition (convergence, maxsteps) is whichever comes first.
        
        Precondition maxstep: Maximum number of steps before giving up
        Precondition: maxstep is int >= 0.
        """
        # Call step repeatedly, up to maxstep times, until the algorithm
        # converges.  Stop after maxstep iterations even if the algorithm has not
        # converged.
        
        assert type(maxstep)==int and maxstep>=0
        i=0
        while i<=maxstep or self.step()==False:
            self.step()
            i+=1
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._clusters)
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)

