from unittest import result

filter_by_avg = lambda d: (
    lambda avg_total: dict(
        filter(
            lambda item: (sum(item[1]) / len(item[1])) > avg_total if item[1] else False,
                          d.items()
        )
    )
)(
        sum(sum(v) for v in d.values()) / sum(len(v) for v in d.values()) #общ сред знач 30
        if d and any (d.values()) else 0
    )

data = {
    "офис_1": [10, 20, 30],  # Среднее: 20
    "офис_2": [5, 10, 15],   # Среднее: 10
    "офис_3": [50, 60, 70],  # Среднее: 60
}

result = filter_by_avg(data)
print(result)