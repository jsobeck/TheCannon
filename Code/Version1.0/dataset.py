import numpy as np

"""Classes and methods for a Dataset of stars.

Provides the ability to initialize the dataset, modify it by adding or
removing spectra, changing label names, adding or removing labels.

Methods
-------
remove_stars

"""

class Dataset(object):
    """A class to represent a Dataset of stellar spectra and labels.
    
    Parameters
    ----------
    IDs: numpy ndarray, list
        Specify the names (or IDs, in whatever format) of the stars.
    spectra: numpy ndarray
        spectra[:,:,0] = wavelengths, pixel values
        spectra[:,:,1] = flux (spectrum)
        spectra[:,:,2] = flux error array
    labels: numpy ndarray, list, optional
        Training labels for training set, but None for test set
    
    Methods
    -------
    set_IDs
    set_spectra
    set_label_names
    set_label_values

    """

    def __init__(self, IDs, spectra, label_names, label_values=None):
        self.IDs = IDs
        self.spectra = spectra 
        self.label_names = label_names
        self.label_values = label_values 
  
    def set_IDs(self, IDs):
        self.IDs = IDs

    def set_spectra(self, spectra):
        self.spectra = spectra

    def set_label_names(self, label_names):
        self.label_names = label_names

    def set_label_values(self, label_values):
        self.label_values = label_values

def remove_stars(dataset, mask):
    """A method to remove a subset of stars from the Dataset. 
    
    Parameters
    ---------
    mask: numpy ndarray of booleans. True means "remove"
    """
    ntokeep = 1-np.sum(mask)
    return Dataset(dataset.IDs[mask], dataset.spectra[mask],
            dataset.label_names, dataset.label_values[mask])
    print "New dataset constructed with %s stars included" %ntokeep
