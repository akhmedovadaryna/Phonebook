# https://github.com/akhmedovadaryna/Phonebook/blob/master/phonebook

class Phonebook:
    """
    class Phonebook
    """
    def __init__(self, phone_list):
        self.__phone_list = phone_list

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__phone_list) - 1:
            raise StopIteration
        self.__index += 1
        return self.__phone_list[self.__index]

    def set_phone_list(self, phone_list):
        self.__phone_list = phone_list

    def get_phone_list(self):
        return self.__phone_list

    def add(self, number, fio, street, house):
        """
        Add a new entry in the phone book
        """
        self.__phone_list.append({'number': number, 'FIO': fio,
                                  'street': street, 'house': house})

    def delete(self, value):
        """
        Delete an entry from the phone book
        """
        i = 0
        flag = 0
        for dct in self.__phone_list:
            print(dct)
            if dct.get('number') != value:
                i += 1
            else:
                flag = 1
                self.__phone_list.pop(i)
        return flag

    def change(self, key, number='', fio='', street='', house=''):
        """
        Change an entry from the phone book
        """
        flag = 0
        l = [number, fio, street, house]
        l_list = ['number', 'FIO', 'street', 'house']
        for dct in self.__phone_list:
            if dct.get('number') == key:
                flag = 1
                j = 0
                while j <= 3:
                    if l[j] == '':
                        j += 1
                        continue
                    else:
                        dct[l_list[j]] = l[j]
                        j += 1
        return flag

    def find(self, number='', fio='', street='', house=''):
        """
        Find an entry from the phone book
        """
        q = []
        l = ['number', 'FIO', 'street', 'house']
        l_list = [number, fio, street, house]
        for dct in self.__phone_list:
            j = 0
            a = 0
            b = 0
            while j <= 3:
                if l_list[j] == '':
                    b += 1
                elif dct.get(l[j]) == l_list[j]:
                    a += 1
                j += 1

            if a == 4 - b:
                q.append(dct)
        return q

    def view_phonebook(self, phone_list=None):
        """
        View phone book
        """
        if phone_list is None:
            for i in self:
                print(i)
        else:
            for i in phone_list:
                print(i)
