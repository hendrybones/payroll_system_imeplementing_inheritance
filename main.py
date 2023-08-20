# hr pyroll system
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating payroll")
        print("===========================")
        for employee in employees:
            print(f"payroll for: {employee.id} - {employee.name}")
            print(f"-check amount: {employee.calculate_payroll()}")
            print('')


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours')


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expands {hours} hours doing office paper')


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone')


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hr = PayrollSystem()
    cs = CommissionEmployee(1, "hendry", 200, 300)
    hm = HourlyEmployee(2,"mwamburi",4,30)
    sm = SalaryEmployee(4,"Mkandoe",400)
    hr.calculate_payroll([cs, hm, sm])

