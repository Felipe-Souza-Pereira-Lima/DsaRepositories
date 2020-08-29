from Scripta import init, migrateWarnings
init()
migrateWarnings('test')
def Read_only(filename, line):
    with open(filename, 'rt') as text:
        result = None
        if line in text:
            result = True
            return result
        else:
            result = False
            return result
        return result
def Read_only_API(filenameto, lineto, valuecharms):
    resulta =  Read_only(filenameto, lineto)
    if resulta is True:
        if valuecharms is not None:
            resulter = f'Chave encontrada ({lineto})\nValores de ambos são chaves validas!'
            return resulter
        else:
            resulter = resulta
            return True
    else:
        return 'Chave invalida no texto!'
        