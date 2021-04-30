class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'Меня зовут {self.name}, мне {self.age} лет, но вы никому об этом не говорите..')


class Boss(Person):

    def __init__(self, name, age, company, salary, month_budget, max_number_of_complaints):
        super().__init__(name, age)
        self.company = company  # название компании, которой руководит босс
        self.salary = salary
        self.employees = []  # сначала у босса ваще нет работников, он их должен нанять
        self.month_budget = month_budget
        self.number_of_complaints = 0  # количество жалоб от сотрудников
        self.max_number_of_complaints = max_number_of_complaints  # максимально возможное количество жалоб

    def employ_person(self, new_employee):
        spending = 0
        for employee in self.employees:
            spending += employee.salary
        if spending + new_employee.salary <= self.month_budget:
            self.employees.append(new_employee)
            print(f'Вы только что приняли на работу в свою компанию работника {new_employee.name}. '
                  f'Не забывайте платить ему зарплату каждый месяц, а не то он на вас пожалуется!')
        else:
            print(f'Нельзя принять на работу работника {new_employee.name}, '
                  f'потому что вы не сможете платить ему зарплату')

    def dismiss(self, employee):
        self.employees.remove(employee)
        print(f'Работник {employee.name} был уволен из компании {self.company}, потому что он плохо себя вёл')

    def dismiss_yourself(self):
        print('Ухожу по собственному желанию, потому что меня здесь не любят и не ценят:(')

    def punish(self, employee):
        employee.number_of_punishments += 1
        if employee.number_of_punishments == employee.max_number_of_punishments:
            self.dismiss(employee)
        else:
            print('Друг, я наказываю тебя. Если будешь продолжать плохо себя вести - уволю!')


class Employee(Person):

    def __init__(self, name, age, salary, max_number_of_punishments):
        super().__init__(name, age)
        self.salary = salary
        self.number_of_punishments = 0
        self.max_number_of_punishments = max_number_of_punishments

    def get_hired(self, boss):  # устроиться на работу к данному боссу
        boss.employ_person(self)
        if self in boss.employees:
            print(f'Поздравляем, вы были приняты на работу в компанию {boss.company}, вашего начальника зовут {boss.name}.'
                  f'Полное социальное страхование, не бойтесь жаловаться на вашего начальника, если он не будет платить'
                  f'Вам зарплату!')

    def complain(self, boss):  # пожаловаться на босса
        boss.number_of_complaints += 1
        if boss.number_of_complaints == boss.max_number_of_complaints:
            boss.dismiss_yourself()
        else:
            print('Ну почему мой начальник такой тупой, и он до сих пор не уволился:(')


boss = Boss('Пётр', 35, 'Google', 50000, 500000, 4)
boss.introduce()
employee1 = Employee('Серёга', 29, 20000, 5)
employee1.introduce()
employee2 = Employee('Павлик', 20, 25000, 3)
employee2.introduce()
employee3 = Employee('Фёдор', 20, 15000, 2)
employee3.introduce()
employee1.get_hired(boss)
employee2.get_hired(boss)
employee3.get_hired(boss)
boss.punish(employee3)
boss.punish(employee3)
employee1.complain(boss)
employee2.complain(boss)
employee2.complain(boss)
employee2.complain(boss)
