from abc import abstractmethod, ABC


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        journey = 8
        return journey


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def get_department(self):
        return self.__department.name

    def set_department(self, department):
        self._department.name = department

    def calc_bonus(self):
        sales_bonus = 0.15
        return self.salary * sales_bonus


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, value):
        self.__sales += value

    def calc_bonus(self):
        sales_bonus = 0.15
        return self.__sales * sales_bonus
