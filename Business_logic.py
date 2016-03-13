__author__ = 'darina'

list_with_dict = [ {'number': 1234,'FIO': 'Akhmedova','street': 'Lesi','house': 1},
                   {'number': 5434,'FIO': 'Ivanov','street': 'Vasi','house': 1},
                   {'number': 5436,'FIO': 'Ivanov','street': 'Vasi','house': 2}
                 ]
print(list_with_dict)


def add(new_number, new_FIO, new_street, new_house):

    list_with_dict.append({'number': new_number, 'FIO': new_FIO, 'street': new_street, 'house': new_house})

def delete(value):
    i = 0
    for dct in list_with_dict:
        if dct.get('number')!=value:
            i = i+1
        else:
            list_with_dict.pop(i)

def change(key, number = '', FIO = '', street = '', house = ''):

     l = [number, FIO, street, house]
     list = ['number', 'FIO', 'street', 'house']
     for dct in list_with_dict:
      if dct.get('number')==key:
       j = 0
       while j != 3:
        if l[j]=='':
            continue
        else:
            dct[list[j]]=l[j]
        j = j+1

def find (number = '', FIO = '', street = '', house = ''):
     i = 0
     q = []
     l = ['number','FIO', 'street', 'house']
     list = [number, FIO, street, house]
     for dct in list_with_dict:
      j = 0
      a = 0
      b = 0
      while j!=3:
        if list[j]=='':
            b = b+1
        elif dct.get(l[j])==list[j]:
            a = a+1
        j = j+1

      if a == 4-b:
            q.append(dct)
     return q


