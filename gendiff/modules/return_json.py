from gendiff.modules.diff import diff


def return_json(file1, file2):
    # result = list(diff(file1, file2))
    return diff(file1, file2) 
    # result.sort(key=lambda x: x[2])
    # result = '\n  '.join(result).\
    #     replace('True', 'true').\
    #     replace('False', 'false')
    # return ''.join(("{\n  ", result, "\n}\n"))
