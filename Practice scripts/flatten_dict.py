from typing import Any, Dict

def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """
    Flattens a nested dictionary by concatenating keys using a separator.

    Args:
        d (dict): Dictionary to flatten.
        parent_key (str): Used internally for recursion to build full keys.
        sep (str): Separator between keys (default is ".").

    Returns:
        dict: Flattened dictionary with dot-notated keys.
    """
    result = {}

    for key, value in d.items():
        full_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            result.update(flatten_dict(value, full_key, sep=sep))
        else:
            result[full_key] = value

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
# Output: {'a': 1, 'b.c': 2, 'b.d.e': 3}

print(flatten_dict(input1, sep="__"))
# Output: {'a': 1, 'b__c': 2, 'b__d__e': 3}
