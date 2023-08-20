import pytest
import main
from main import Employee, PayrollSystem, SalaryEmployee, HourlyEmployee, CommissionEmployee, Manager, Secretary, \
    SalesPerson, FactoryWorker


@pytest.fixture
def sample_employees():
    cs = CommissionEmployee(1, "hendry", 200, 300)
    hm = HourlyEmployee(2, "mwamburi", 4, 30)
    sm = SalaryEmployee(4, "Mkandoe", 400)
    return [cs, hm, sm]


# testing attributes


def test_employee_attributes(sample_employees):
    for employee in sample_employees:
        assert hasattr(employee, "id")
        assert hasattr(employee, "name")


def test_calculate_payroll(sample_employees):
    payroll_system = PayrollSystem()
    expected_output = [200 + 300, 4 * 30, 400]
    for i, employee in enumerate(sample_employees):
        assert employee.calculate_payroll() == expected_output[i]



