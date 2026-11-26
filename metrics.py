import numpy as np

def logical_error_rate(predictions, observables):
    diff = predictions != observables
    return np.sum(diff)/len(observables)



