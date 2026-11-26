import stim

def create_surface_code (distance, rounds, noise):
    circuit = stim.Circuit.generated(
        "surface_code:rotated_memory_x",
        distance=distance,
        rounds=rounds,
        after_clifford_depolarization=noise 
    )

    return circuit

if __name__ == "__main__":
    circuit = create_surface_code(3, 3, 0.01)
    print(circuit)


