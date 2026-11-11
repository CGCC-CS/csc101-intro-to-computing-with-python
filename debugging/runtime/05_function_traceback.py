def calculate_average(scores):
    return sum(scores) / len(scores)


def report_average(scores):
    result = calculate_average(scores)
    print("Average:", result)


report_average([80, 90, 100])
report_average([])
