#############################################################
# Author(s) : Debaditya, Anwesha, Anna                      #
#############################################################

def loadDat(data_path,sessions):
    '''
    WARNING!:This is an outdated function
    
    This function returns all the required variables.
    
    Args:
    
    data_path - [str] This is the path to the file where the folders with the trials are present.
    sessions - [list] list of indxes of sessions to load.
    
    Return:
    
    no_of_sessions - [int] The total no. of sessions loaded.
    spontaneous_intervals - [dict] Intervals of spontaneous activity indexed by session
    trials_intervals - [dict] Intervals of the trial indexed by session
    channel_brainLocations - [dict] Name of the location of the probe indexed by session
    clusters_phy_annotation - [dict] Cluster accuracy indexed by session
    clusters_peakChannel - [dict] Cluster peak channel indexed by session
    spikes_amps - [dict] Spike amplitudes indexed by session
    spikes_clusters - [dict] Spike cluster origin indexed by session
    spikes_depths - [dict] Spike origin depth indexed by session
    spikes_times - [dict] Spike times indexed by session
    
    Usage Example:
    data_path = '/NMA/Mapping Brain Networks/data/allData/'
    #Sessions that you want to extract
    sessions = [11,12] #Session 11,12
    #Load Data
    no_of_sessions ,spontaneous_intervals, trials_intervals, channel_brainLocations, clusters_phy_annotation, clusters_peakChannel, spikes_amps, spikes_clusters, spikes_depths, spikes_times = loadDat(data_path,sessions) 
    '''
    
    #Fetch dependencies
    import numpy as np
    import glob
    import csv

    print('Importing the data for sessions',sessions)
    #Get all paths
    session_paths = glob.glob(data_path + '*')
   
    #Get number of sessions
    no_of_sessions = len(sessions)
    
    #Define dictionaries
    #Intervals - Time stamps which are useful
    spontaneous_intervals = {}
    trials_intervals = {}
    
    #Channels - (Locations in the brain)
    channel_brainLocations = {x:[] for x in sessions} 
    
    #Clusters - Specific neruons / group of neurons
    clusters_phy_annotation = {}
    clusters_peakChannel = {}
    
    #Spikes - All the data about the spikes
    spikes_amps = {}
    spikes_clusters = {}
    spikes_depths = {}
    spikes_times = {}
    
    #Run the for loop to get the values.
    for session in sessions:
        path = session_paths[session]
        #Load Intervals
        spontaneous_intervals[session] = np.load(path + '/spontaneous.intervals.npy', allow_pickle=True)
        trials_intervals[session] = np.load(path + '/trials.intervals.npy', allow_pickle = True)
        
        #Load channels
        with open(path + '/channels.brainLocation.tsv') as tsvfile:
            reader = csv.DictReader(tsvfile, dialect='excel-tab')
            for row in reader:
                channel_brainLocations[session].append(row['allen_ontology'])
        
        #Load Clusters
        clusters_phy_annotation[session] = np.load(path + '/clusters._phy_annotation.npy', allow_pickle = True)
        clusters_peakChannel[session] = np.load(path + '/clusters.peakChannel.npy', allow_pickle = True)
        
        #load Spikes
        spikes_amps[session] = np.load(path + '/spikes.amps.npy', allow_pickle = True)
        spikes_clusters[session] = np.load(path + '/spikes.clusters.npy', allow_pickle = True)
        spikes_depths[session] = np.load(path + '/spikes.depths.npy', allow_pickle = True)
        spikes_times[session] = np.load(path + '/spikes.times.npy', allow_pickle = True)
        
        print('Data Successfully loaded for session',session)
    return no_of_sessions ,spontaneous_intervals, trials_intervals, channel_brainLocations, clusters_phy_annotation, clusters_peakChannel, spikes_amps, spikes_clusters, spikes_depths, spikes_times


def get_session_info(root, path):
    '''
    This function returns the date on which the session was carried out and the name of the mouse.
    
    Args:
    root - [string] The root directory path.
    path - [string] The path to the session directory.
    
    Returns:
    date - [string] Date the experiment was conducted in YYYY-MM-DD format.
    name - [string] Name of the mouse
    '''
    
    #Get substring
    name_date = path.replace(root+'\\','')
    
    #Get date
    date = name_date[:-11]
    
    #Get name
    name = name_date[-10:]
    
    return date, name

def get_cluster_info(path):
    '''
    This function returns information about clusters.
    
    Args:
    path - [string] The path to the session directory.
    
    Returns:
    good_clusters - [ndarray] Logical values representing if a cluster is 'good'.
    brain_regions - [list] Location where a cluster is located.
    '''
    
    #Get good clusters. _phy_annotation >=2
    good_clusters = (np.load(path + '/clusters._phy_annotation.npy')>=2).flatten()
    
    #Get cluster_channels
    cluster_channels = (np.load(path + '/clusters.peakChannel.npy').astype(int) - 1).flatten()
    
    #Create brain region temp variable
    brain_regions = []
    
    #Open channel files
    with open(path + '/channels.brainLocation.tsv') as tsvfile:
        
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        
        for row in reader:
            
            #Parse regions
            brain_regions.append(row['allen_ontology'])
    
    #Create cluster location list.
    cluster_locations = []
    
    #Iterate through the channels and parse the brain locations
    for cluster_channel in cluster_channels:
        
        brain_region = brain_regions[cluster_channel]
        cluster_locations.append(brain_region)
        del brain_region
            
    #Return the variables.
    return good_clusters, cluster_locations
 
def get_cluster_spikes(path):
    '''
    This function retuns the spikes sorted according to clusters.
    
    args:
    path - [string] The path to the session directory.
    
    return:
    cluster_spikes - [list] This is a list of lists of spike timings.
    '''
    #Load the spikes
    spikes = np.load(path + '/spikes.times.npy', allow_pickle = True).flatten()
    
    #load the cluster_ids
    cluster_ids = np.load(path + '/spikes.clusters.npy', allow_pickle = True).flatten()
    
    #Create empty list
    clusters_spikes = [] #NOTE I CHANGED THIS LOOK INTO THIS LATER!
    
    #iterate through cluster_ids to arrange spikes.
    for cluster_id in range(np.max(cluster_ids)+1):
        cluster_spikes = spikes[np.where(cluster_ids == cluster_id)]
        clusters_spikes.append(cluster_spikes)
        
    #Return the variables.
    return cluster_spikes

def get_trial_info(path):
    '''
    This function returns all the information about the trials.
    
    args:
    path - [string] The path to the session directory.
    
    returns:
    trial_intervals
    visualStim_times
    goCue_times
    response_times
    feedback_times
    feedback_type
    '''
    
    trial_intervals = np.load(path + '/trials.intervals.npy', allow_pickle = True)
    visualStim_times = np.load(path + '/trials.visualStim_times.npy', allow_pickle = True)
    goCue_times = np.load(path + '/trials.goCue_times.npy', allow_pickle = True)
    response_times = np.load(path + '/trials.response_times.npy', allow_pickle = True)
    feedback_times = np.load(path + '/trials.feedback_times.npy', allow_pickle = True)
    feedback_type =np.load(path + '/trials.feedbackType.npy', allow_pickle = True)
    
    return trial_intervals, visualStim_times, goCue_times, response_times, feedback_times, feedback_type

## This part of the code can be used to save the data currently in memory

def save_data(filename, objects):
    '''
    This function will save the data you want to into the named file
    
    Args:
    
    filename - [string] The name of the file that you want to save your data into. (include extention .pkl)
    objects - [list] The list of objects you want to store from memory into the file.
    
    Return:
    
    void
    
    Usage Example:
    save_data('data.pkl',[no_of_sessions ,spontaneous_intervals, trials_intervals, channel_brainLocations, clusters_phy_annotation, clusters_peakChannel, spikes_amps, spikes_clusters, spikes_depths, spikes_times])
    '''
    
    #Grab dependencies
    import pickle
    
    #Open file
    with open(filename, 'wb') as f:
        #Dump memory
        pickle.dump(data, f)
        