import unittest
import re
from datetime import datetime

# Create a function that checks user enters between 1 and 7 capital letters 
def validate_symbol(symbol):
    return bool(re.fullmatch(r'[A-Z]{1,7}', symbol))

# Create a function that checks user enters 1 or 2
def validate_chart_type(chart_type):
    return bool(re.fullmatch(r'[12]', chart_type))

# Create a function that checks user enters a whole number between 1 and 4
def validate_time_series(time_series):
    return bool(re.fullmatch(r'[1-4]', time_series))

# Create a function that checks user enters a valid date for the start date
def validate_start_date(start_date):
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Create a function that checks user enters a valid date for the end date
def validate_end_date(end_date):
    try:
        datetime.strptime(end_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Create class to run unit tests for Stock Symbol
class TestStockSymbol(unittest.TestCase):

    # Create a method that checks a few valid entries
    def test_valid_symbols(self):
        self.assertTrue(validate_symbol("IBM"))
        self.assertTrue(validate_symbol("AAPL"))
        self.assertTrue(validate_symbol("ABCDEFG"))

    # Create a method that checks a few invalid entries
    def test_invalid_symbols(self):
        self.assertFalse(validate_symbol("aapl"))
        self.assertFalse(validate_symbol("ABCDEFGH"))
        self.assertFalse(validate_symbol("ABC123"))
        self.assertFalse(validate_symbol("BRK.B"))

# Create class to run unit tests for entering chart type
class TestChartType(unittest.TestCase):

    # Create a method that checks a few valid entries
    def test_valid_chart_types(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))

    # Create a method that checks a few invalid entries
    def test_invalid_chart_types(self):
        self.assertFalse(validate_chart_type("3"))
        self.assertFalse(validate_chart_type("0"))
        self.assertFalse(validate_chart_type("12"))
        self.assertFalse(validate_chart_type("A"))

# Create class to run unit tests for picking a time series
class TestTimeSeries(unittest.TestCase):

    # Create a method that checks a few valid entries
    def test_valid_time_series(self):
        self.assertTrue(validate_time_series("1"))
        self.assertTrue(validate_time_series("2"))
        self.assertTrue(validate_time_series("3"))
        self.assertTrue(validate_time_series("4"))

    # Create a method that checks a few invalid entries
    def test_invalid_time_series(self):
        self.assertFalse(validate_time_series("0"))
        self.assertFalse(validate_time_series("5"))
        self.assertFalse(validate_time_series("12"))
        self.assertFalse(validate_time_series("A"))

# Create class to run unit tests for checking the start date is valid
class TestStartDate(unittest.TestCase):

    # Create a method that checks a few valid entries
    def test_valid_start_dates(self):
        self.assertTrue(validate_start_date("2026-11-19"))
        self.assertTrue(validate_start_date("2025-01-15"))

    # Create a method that checks a few invalid entries
    def test_invalid_start_dates(self):
        self.assertFalse(validate_start_date("11/19/2026"))
        self.assertFalse(validate_start_date("2026-13-19"))
        self.assertFalse(validate_start_date("2026-02-30"))
        self.assertFalse(validate_start_date("not-a-date"))

# Create class to run unit tests for checking the end date is valid
class TestEndDate(unittest.TestCase):

    # Create a method that checks a few valid entries
    def test_valid_end_dates(self):
        self.assertTrue(validate_end_date("2026-11-19"))
        self.assertTrue(validate_end_date("2025-01-15"))

    # Create a method that checks a few invalid entries
    def test_invalid_end_dates(self):
        self.assertFalse(validate_end_date("11/19/2026"))
        self.assertFalse(validate_end_date("2026-13-19"))
        self.assertFalse(validate_end_date("2026-02-30"))
        self.assertFalse(validate_end_date("not-a-date"))

# Run the unit tests
if __name__ == "__main__":
    unittest.main()