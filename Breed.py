def breed(self, mother, father):
    """Make two children as parts of their parents.

    Args:
        mother (dict): Network parameters
        father (dict): Network parameters

    """
    children = []
    for _ in range(2):

        child = {}

        # Loop through the parameters and pick params for the kid.
        for param in self.nn_param_choices:
            child[param] = random.choice(
                [mother.network[param], father.network[param]]
            )

        # Now create a network object.
        network = Network(self.nn_param_choices)
        network.create_set(child)

        children.append(network)

    return children