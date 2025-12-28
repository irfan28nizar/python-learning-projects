def calculate_averages(students):
    avg_scores = {}
    for k, v in students.items():
        avg_scores[k] = round(sum(v)/len(v),1)
    return avg_scores