def empirical_pmf(samples):
    counts = {}
    total = 0

    for value in samples:
        counts[value] = counts.get(value, 0) + 1
        total += 1

    return [(value, counts[value] / total) for value in sorted(counts)]