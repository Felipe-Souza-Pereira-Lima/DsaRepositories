from time import sleep
if __name__ == '__main__':
    def main(typeof, value, connect, Read_Only):
        for i in value:
            keys = [i, typeof, connect]
            if Read_Only == True:
                return keys
            if Read_Only is None:
                continue
            else:
                return 'Requesitos não encontrados'
        else:
            return False
        yield Read_Only, True, 1, 2, 3
    