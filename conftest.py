import pytest
import os
import xlrd
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xlsx_"):
            testdata = load_from_file(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_file(file):
    group_list = []
    workbook = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.abspath(__file__)), "%s.xlsx" % file))
    worksheet = workbook.sheet_by_index(0)
    for i in range(10):
        group_list.append(worksheet.cell(i, 0).value)
    print(group_list)
    return group_list
