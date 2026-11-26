def generate_data(circuit, shots):
    """Return detector events and observable flips for simulated shots."""
    sampler_object = circuit.compile_detector_sampler()
    return sampler_object.sample(shots, separate_observables=True)
