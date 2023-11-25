from SavingsAccount import *
from CreditAccount import *
from Bank import *
from Main_Bank_VersionX import *
import pytest
from unittest.mock import patch


# Test SavingsAccunt
@pytest.fixture
def setup_fixtures_Savings():
    return SavingsAccount('Huy', '123456', 5000)

# Unitest
def test_unit_show_vailable_balance_SavingsAccount(setup_fixtures_Savings, capfd):
    # Chạy thử nghiệm cho đầu vào hiện tại
    setup_fixtures_Savings.show_available_balance()

    # Đọc đầu ra
    captured = capfd.readouterr()

    # Kiểm tra đầu ra
    assert 'Balance: 5000\n' in captured.out

# Integration test
def test_integration_show_vailable_balance_SavingsAccount(capsys, setup_fixtures_Savings):
    with patch("Main_Bank_VersionX.Account.show") as mock_show:
        # Thiết lập giá trị trả về giả mạo của phương thức show
        mock_show.return_value = 5000

        # Gọi hàm được kiểm thử
        setup_fixtures_Savings.show_available_balance()

    captured = capsys.readouterr()
    expected_output = 'Balance: 5000\n'

    assert captured.out == expected_output


# Test CreditAccount
@pytest.fixture
def setup_fixtures_Credit():
    return CreditAccount('Huy', '123456', 2000)

# Unitest
def test_unit_show_vailable_balance_CreditAccount(setup_fixtures_Credit, capfd):
    # Chạy thử nghiệm cho đầu vào hiện tại
    setup_fixtures_Credit.show_available_balance()

    # Đọc đầu ra
    captured = capfd.readouterr()

    # Kiểm tra đầu ra
    assert 'Balance: 2000\n' in captured.out

# Integration test
def test_integration_show_vailable_balance_CreditAccount(capsys, setup_fixtures_Credit):
    with patch("Main_Bank_VersionX.Account.show") as mock_show:
        # Thiết lập giá trị trả về giả mạo của phương thức show
        mock_show.return_value = 2000

        # Gọi hàm được kiểm thử
        setup_fixtures_Credit.show_available_balance()

    captured = capsys.readouterr()
    expected_output = 'Balance: 2000\n'

    assert captured.out == expected_output
