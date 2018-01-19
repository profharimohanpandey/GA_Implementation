def evolve(self, pop):
    """Evolve a population of networks.

    Args:
        pop (list): A list of network parameters
    """
    # Get scores for each network.
    graded = [(self.fitness(network), network) for network in pop]

    # Sort on the scores.
    graded = [x[1] for x in sorted(graded, key=lambda x: x[0], reverse=True)]

    # Get the number we want to keep for the next gen.
    retain_length = int(len(graded)*self.retain)

    # The parents are every network we want to keep.
    parents = graded[:retain_length]

    # For those we aren't keeping, randomly keep some anyway.
    for individual in graded[retain_length:]:
        if self.random_select > random.random():
            parents.append(individual)

    # Randomly mutate some of the networks we're keeping.
    for individual in parents:
        if self.mutate_chance > random.random():
            individual = self.mutate(individual)

    # Now find out how many spots we have left to fill.
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []

    # Add children, which are bred from two remaining networks.
    while len(children) < desired_length:

        # Get a random mom and dad.
        male = random.randint(0, parents_length-1)
        female = random.randint(0, parents_length-1)

        # Assuming they aren't the same network...
        if male != female:
            male = parents[male]
            female = parents[female]

            # Breed them.
            babies = self.breed(male, female)

            # Add the children one at a time.
            for baby in babies:
                # Don't grow larger than desired length.
                if len(children) < desired_length:
                    children.append(baby)

    parents.extend(children)

    return parents
