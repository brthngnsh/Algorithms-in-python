import offline_data_sampling

def random_permutation(n):
    permutation = list(range(n))
    offline_data_sampling.offline_dats_sampling(n,permutation)
    return permutation