import LoginClass as log

def getTypes():
    tp = []
    for types in (log.UserTypes):
        tp.append(types.name)

    return tp