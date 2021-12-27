
import os.path
import RutishauserLabtoNWB.events.newolddelay.python.export.no2nwb as no2nwb
import RutishauserLabtoNWB.events.newolddelay.python.export.data as data
from pynwb import NWBHDF5IO
import numpy as np
import logging



def NO2NWB_export(path_to_data):

    ## ========== User Inputs Here ========================================================================================
    #path_to_data = 'C:\\Users\\chandravadn1\\Desktop\\code\data\\Faraut et al 2018'  # Path to Native Data
    ## =====================================================================================================================


    #  Set the Path to save the NWB files
    pathToNWBfiles = input('Where do you want to save NWB files to (no need to put quotes): ')
    while (os.path.exists(pathToNWBfiles)) < 1:
        print('Sorry, this file [{}] does not exist, try again'.format(pathToNWBfiles))
        pathToNWBfiles = input('Where do you want to save NWB files to (no need to put quotes): ')

    # Get .ini file path
    subjects_ini = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(no2nwb.__file__))),
                                    'defineNOsessions_release.ini')
    if not os.path.exists(subjects_ini):
        print('This file does not exist: {}'.format(subjects_ini))


    # Create the NWB file and extract data from the original data format
    NOdata = data.NOData(path_to_data, subjects_ini)


    for session_nr in NOdata.sessions.keys():

        nwbfile = no2nwb.no2nwb(NOdata, session_nr, subjects_ini, path_to_data)

        len_new_old_labels = len(np.asarray(nwbfile.trials['new_old_labels_recog']))
        wrong_sessions = []
        print('The length of the new old label: {}'.format(len_new_old_labels))
        if (len_new_old_labels != 200) & (len_new_old_labels != 150):
            print('Session ' + str(session_nr))
            wrong_sessions.append(session_nr)
            logging.warning('The length of the label data is not either 200 or 150: ' + 'Session ' + str(session_nr))

        # Export and write the nwbfile
        session_name = NOdata.sessions[session_nr]['filename']

        # Check File Outputs
        outputFilePath = os.path.join(pathToNWBfiles, session_name)

        io = NWBHDF5IO(outputFilePath, mode='w')
        io.write(nwbfile, cache_spec = False)
        io.close()
        print('Successfully written this file: {}'.format(outputFilePath))
