#test_Employee_Details.py
import pytest
from Employee_Details import get_employee_details

def test_get_employee_details():
    #Sample data
    name = "Alice Smith"
    emp_id = "E1234"
    department = "HR"
    salary = "60000"
    #expected output
    expected_output = (
        "Employee Name: Alice Smith,"
        "Employee ID: E1234,"
        "Department: HR,"
        "Salary: 60000"
    )
    #assertion
    assert get_employee_details(name, emp_id, department, salary) == expected_output
