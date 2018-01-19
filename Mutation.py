def mutate(self, network):
    """Randomly mutate one part of the network.

    Args:
        network (dict): The network parameters to mutate

    """
    # Choose a random key.
    mutation = random.choice(list(self.nn_param_choices.keys()))

    # Mutate one of the params.
    network.network[mutation] = random.choice(self.nn_param_choices[mutation])

    return network
