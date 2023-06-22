def print_dict(random_dict):
    print(set(v for i in range(len(random_dict)) for (k, v) in random_dict[i].items()))


ran_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
            {"V": "S009"}, {"VIII": "S007"}]
print_dict(ran_dict)
