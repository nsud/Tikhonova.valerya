class Employee:
    def __init__(self, name, sen):
        self.name = name
        # Международная премия
        self.prem = 2
        # Всего была 2 раза... у каждой по 2 балла
        self.sen = sen + (self.prem * 2)

        self.grade = 1

    def grade_up(self):
        self.grade += 1

    def print_(self):
        print(f"{self.name} - {self.grade}")

    def check(self):
        pass


class Designer(Employee):
    def __init__(self, name, sen):
        super().__init__(name, sen)

    def check(self):
        self.sen += 1

        if self.sen % 7 == 0:
            self.grade_up()

        return self.print_()