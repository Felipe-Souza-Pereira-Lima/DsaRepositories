__version__ = '1.0.7'
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
def compare(str1, str2):
   if str1 == str2:
      return True
   else:
      return False
def compare_files(filename1, filename2):
   try:
      with open(filename1) as m1:
         m1 = m1.read()
      with open(filename2) as m2:
         m2 = m2.read()
   except FileNotFoundError:
      return 'Esse arquivo não existe!'
   else:
      if m1 == m2:
         return True
      else:
         return False
