from SavingsAccount import *
from Bank import *
import pytest
from Main_Bank_VersionX import *

# Truong hop bank da co account
@pytest.fixture
def setup_fixtures():
    bank = Bank()
    bank.createAccount('Joe', "123", 500)
    bank.createAccount('John', "456", 600)
    bank.createAccount('Huy', "789", 700)
    bank.createAccount('AmazingShadow', "124", 800)
    return bank

# Truong hop bank chua co account nao
@pytest.fixture
def setup_fixtures_showAll():
    bank = Bank()
    return bank

def test_bank_create_account(setup_fixtures):
    setup_fixtures.createAccount('Draven', "123", 1000)

    assert setup_fixtures.accountsDict[4].show() == 1000 and setup_fixtures.counter == 5

def test_open_bank_account(setup_fixtures, monkeypatch, capfd):
    inputs = iter(['Huy', '123', 500])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    setup_fixtures.open_account()
    
    out, err = capfd.readouterr()
    expected_output = '\n*** Open Account ***'
    assert out.startswith(expected_output), f"Expected output to start with '{expected_output}', but got '{out}'"



def test_close_bank_account(setup_fixtures, monkeypatch, capfd):
    expected_outputs = {
        (0, '456'): '\n*** Close Account ***\nwrong password\nprogram ended\n',
        (0, '123'): '\n*** Close Account ***\npw ok!\nYou had 500 in your bank account wich they will return to you\nAccount: 0 eliminated\n',
    }

    for input_tuple, expected_output in expected_outputs.items():
        # Thiết lập đầu vào cho lần lặp hiện tại
        inputs = iter(input_tuple)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        # Chạy thử nghiệm cho đầu vào hiện tại
        setup_fixtures.closeAccount()

        # Đọc đầu ra
        captured= capfd.readouterr()

        # Kiểm tra đầu ra
        assert expected_output in captured.out


def test_bank_balance(setup_fixtures, monkeypatch, capfd):
    expected_outputs = {
        (0, '123'): '\n*** Balance ***\npw ok!\nBalance: 500\n',
        (0, '456'): '\n*** Balance ***\nwrong password\nprogram ended\n',
        # Add more mappings as needed
    }

    for input_tuple, expected_output in expected_outputs.items():
        # Thiết lập đầu vào cho lần lặp hiện tại
        inputs = iter(input_tuple)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        # Chạy thử nghiệm cho đầu vào hiện tại
        setup_fixtures.balance()

        # Đọc đầu ra
        captured= capfd.readouterr()

        # Kiểm tra đầu ra
        assert expected_output in captured.out


def test_bank_deposit(setup_fixtures, monkeypatch, capfd):
    expected_outputs = {
        (0, '123', 1000): '\n*** Deposit ***\npw ok!\ndeposit of 1000 done!\n',
        (0, '456', 3000): '\n*** Deposit ***\nwrong password\nprogram ended\n',
    }

    for input_tuple, expected_output in expected_outputs.items():
        # Thiết lập đầu vào cho lần lặp hiện tại
        inputs = iter(input_tuple)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        # Chạy thử nghiệm cho đầu vào hiện tại
        setup_fixtures.deposit()

        # Đọc đầu ra
        captured= capfd.readouterr()

        # Kiểm tra đầu ra
        assert expected_output in captured.out


def test_bank_withdraw(setup_fixtures, monkeypatch, capfd):
    expected_outputs = {
        (0, '123', 200): '\n*** Withdraw ***\npw ok!\nwithdraw of 200 done!\n',
        (0, '456', 3000): '\n*** Withdraw ***\nwrong password\nprogram ended\n',
    }

    for input_tuple, expected_output in expected_outputs.items():
        # Thiết lập đầu vào cho lần lặp hiện tại
        inputs = iter(input_tuple)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        # Chạy thử nghiệm cho đầu vào hiện tại
        setup_fixtures.withdraw()

        # Đọc đầu ra
        captured= capfd.readouterr()

        # Kiểm tra đầu ra
        assert expected_output in captured.out

def test_bank_show(setup_fixtures, monkeypatch, capfd):
    expected_outputs = {
        (0, '123'): '\n*** Show info account ***\npw ok!\nAccount N: 0 Name: Joe Balance: 500\n',
        (0, '456'): '\n*** Show info account ***\nwrong password\nprogram ended\n',
        # Add more mappings as needed
    }

    for input_tuple, expected_output in expected_outputs.items():
        # Thiết lập đầu vào cho lần lặp hiện tại
        inputs = iter(input_tuple)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        # Chạy thử nghiệm cho đầu vào hiện tại
        setup_fixtures.show()

        # Đọc đầu ra
        captured= capfd.readouterr()

        # Kiểm tra đầu ra
        assert expected_output in captured.out


def test_bank_showAllAccount(setup_fixtures, capfd):
    # Chạy thử nghiệm cho đầu vào hiện tại
    setup_fixtures.show_all_account()

    # Đọc đầu ra
    captured= capfd.readouterr()

    # Kiểm tra đầu ra
    assert '\n*** Accounts list ***\nN.:0 Name: Joe Pw: 123 Balance: 500\nN.:1 Name: John Pw: 456 Balance: 600\nN.:2 Name: Huy Pw: 789 Balance: 700\nN.:3 Name: AmazingShadow Pw: 124 Balance: 800\n' \
                                    in captured.out

def test_bank_showAllAccount_empy(setup_fixtures_showAll, capfd):
    # Chạy thử nghiệm cho đầu vào hiện tại
    setup_fixtures_showAll.show_all_account()

    # Đọc đầu ra
    captured= capfd.readouterr()

    # Kiểm tra đầu ra
    assert '\n*** Accounts list ***\n<empty>\n' in captured.out