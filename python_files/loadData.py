def loadDat(data_path,sessions):
    '''
    This function will load the Steinmetz data.
    
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
    '''
    
    #Fetch dependencies
    import numpy as np
    import glob
    import csv

    #Get all paths
    session_paths = glob.glob(data_path + '*')
   
    #Get number of sessions
    no_of_sessions = len(sessions)
    
    #Define dictionaries
    #Intervals - Time stamps which are useful
    spontaneous_intervals = {}
    trials_intervals = {}
    
    #Channels - (Locations in the brain)
    channel_brainLocations = {x:[] for x in range(no_of_sessions)} 
    
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

    return no_of_sessions ,spontaneous_intervals, trials_intervals, channel_brainLocations, clusters_phy_annotation, clusters_peakChannel, spikes_amps, spikes_clusters, spikes_depths, spikes_times