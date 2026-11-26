import pymatching

def create_decoder(circuit):
    error_model = circuit.detector_error_model(decompose_errors=True)
    decoder = pymatching.Matching.from_detector_error_model(error_model)
    return decoder


def decode_data(decoder, detectors):
    return decoder.decode_batch(detectors)