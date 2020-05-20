class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:
    def __init__(self, code, name, salary, department):
        if (type(self) == Employee):
            raise TypeError('Employee não pode ser instanciado diretamente')
        else:
            self.__departament = department
            self.code = code
            self.name = name
            self.salary = salary

    def calc_bonus(self):
        raise NotImplementedError('Necessário implementação da função')

    def get_hours(self):
        return 8

    def get_departament(self):
        return self.__departament.name

    def set_department(self, department_name):
        self.__departament.name = department_name


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value

    def calc_bonus(self):
        return self.__sales * 0.15