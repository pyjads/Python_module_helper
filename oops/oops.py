#%%
class Employee:
    salary = 1000
    def __init__(self, name, sex, nationality, gmail):
        self.name = name
        self.sex = sex
        self.nationality = nationality
        self.gmail = gmail

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __gmail(self):
        return self.email + '@gmail.com'

    def gmail(self):
        return self.__gmail()

class CTS(Employee):

    def __init__(self, name, sex, nationality):
        self.name = name
        self.sex = sex
        self.nationality = nationality

    def gmail(self):
        return super(CTS, self).gmail()


if __name__ == '__main__':
    e = CTS('sanket','M','Indian','sanket@gmail.com')
    print(e.email)