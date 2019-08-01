import difflib


def diff_lists(a, b):
    """
    get added list and removed list, from 2 lists diff
    """
    d = difflib.Differ()

    added = []
    removed = []
    for item in list(d.compare(a, b)):
        if item.startswith('+'):
            added.append(item[1:].strip())
        if item.startswith('-'):
            removed.append(item[1:].strip())

    return (added, removed)
