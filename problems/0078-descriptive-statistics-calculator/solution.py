import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1

    highest_count = max(counts.values())
    mode = min(value for value, count in counts.items() if count == highest_count)

    q1, q2, q3 = np.percentile(data, [25, 50, 75])
    variance = np.var(data)

    return {
        "mean": float(np.mean(data)),
        "median": float(q2),
        "mode": int(mode),
        "variance": float(variance),
        "standard_deviation": float(np.sqrt(variance)),
        "25th_percentile": float(q1),
        "50th_percentile": float(q2),
        "75th_percentile": float(q3),
        "interquartile_range": float(q3 - q1),
    }