import pickle
dataPath = 'data.pickle'

class dataWork:
    def addContact(user : dict):
        try:
            with open(dataPath, 'rb') as f:
                swap = pickle.load(f)
            with open(dataPath, 'wb') as f:
                swap.append(user)
                pickle.dump(swap, f)
        except EOFError:
            with open(dataPath, 'wb') as f:
                pickle.dump([user], f)
    
    def findContact(key) -> dict:
        try:
            with open(dataPath, 'rb') as f:
                swap = pickle.load(f)
                for q in swap:
                    if q['name'] == key or q['secondName'] == key or q['number'] == key:
                        return q
            return {'name' : None, 'secondName' : None, 'number' : None}
        except EOFError:
            print('Нельзя ничего найти в пустой книге')
            return {'name' : None, 'secondName' : None, 'number' : None}

    def editContact(user, userNew):
        dataWork.deleteContact(user)
        dataWork.addContact(userNew)

    def deleteContact(user) -> dict:
        with open(dataPath, 'rb') as f:
            swap = pickle.load(f)
        for q in swap:
            if q == user:
                swap.remove(q)
                with open(dataPath, 'wb') as f:
                    pickle.dump(swap, f)
                return q

    def retDict() -> list:
        try:
            with open(dataPath, 'rb') as f:
                swap = pickle.load(f)
            return swap
        except EOFError:
            print('А книга-то пустая(')

    def clearDict():
        with open(dataPath, 'wb') as f:
            pass