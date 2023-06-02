import data


class taskMenu:
    choice = 0

    def mainMenu(self) -> None:
        try:
            choice = int(input(
                "Меню:\n1 -- Запись нового контакта\n2 -- Поиск контакта\n" +
                "3 -- Очистка записной книжки\n4 -- Показать все контакты\n" +
                "5 -- Выход из программы\nВаш выбор:"))
            if choice == 1:
                self.userInput(self)
            elif choice == 2:
                self.userRequest(self)
            elif choice == 3:
                data.dataWork.clearDict()
            elif choice == 4:
                self.showContacts(self)
            elif choice == 5:
                self.choice = -1
            else:
                raise ValueError
        except ValueError:
            print('Вы ввели не тот выбор')
            self.mainMenu(self)

    def userInput(self) -> dict:
        name = input('Введите имя: ')
        secondName = input('Введите фамилию: ')
        number = input('Введите номер телефона: ')
        user = {'name': name, 'secondName': secondName, 'number': number}
        data.dataWork.addContact(user)
        print('Вы записали контакт:')
        self.userPrint(user)

    def userRequest(self) -> None:
        user = data.dataWork.findContact(input('Введите ключ для поиска: '))
        if self.userPrint(user):
            choice = int(input(
                "1 -- Изменить контакт\n2 -- Удалить контакт\n3 -- Выход\nВаш выбор:"))
            if choice == 1:
                name = input('Введите имя: ')
                secondName = input('Введите фамилию: ')
                number = input('Введите номер телефона: ')
                userNew = {'name': name,
                           'secondName': secondName, 'number': number}
                data.dataWork.editContact(user, userNew)
            if choice == 2:
                self.deleteUser(self, user)

    def userPrint(user) -> bool:
        if user['name'] != None:
            print('Имя {}\nФамилия {}\nТелефон {}'.format(
                  user['name'], user['secondName'], user['number']))
            return True
        else:
            print('Никого не удалось найти((')
            return False

    def showContacts(self):
        for a in data.dataWork.retDict():
            self.userPrint(a)

    def deleteUser(self, user):
        print('Вы удалили:')
        self.userPrint(data.dataWork.deleteContact(user))
