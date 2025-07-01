def flatten_dict(d):
    result = {}
    
    for key, value in d.items():
        if isinstance(value, dict):
            flat_value = flatten_dict(value)
            for sub_key, sub_value in flat_value.items():
                result[key + "." + sub_key] = sub_value
        else:
            result[key] = value
    
    return result


input1 = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3
        }
    }
}              

print(flatten_dict(input1))
            