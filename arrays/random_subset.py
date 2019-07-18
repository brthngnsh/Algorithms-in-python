import random


def random_subsets(n,k):
    changed_elements = {}
    for i in range(k):
        random_idx = random.randrange(i,n)
        random_idx_mapped = changed_elements.get(random_idx,random_idx)
        i_mapped = changed_elements.get(i,i)
        changed_elements[random_idx] = i_mapped
        changed_elements[i] = random_idx_mapped
    return [changed_elements[i] for i in range(k)]
