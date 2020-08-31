from time import sleep
if __name__ == '__main__':
   def Read_Only(filename, keyword):
      result = None
      try:
         with open(filename, 'rt') as file:
            if keyword in file:
               result = f'Chave encontrada no arquivo {filename}'
               return result
            else:
               result = f'Chave não encontrada no arquivo {filename}'
      except FileNotFoundError:
         print('Esse arquivo não existe!')
         result = False
         return result
      return result
