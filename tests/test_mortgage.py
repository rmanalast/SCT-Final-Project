"""
Description: A class used to test the Mortgage class.
Author: Raven Manalastas
Date: 20 March 2024
Usage: Use the tests encapsulated within this class 
to test the Mortgage Payment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage 
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    def test_init_invalid_amount(self):
        # Arrange
        loan_amt = 0.0
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10 
        except_error = "Loan Amount must be positive."

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(loan_amt, rate, freq, amort)

        # Assert
        self.assertEqual(str(context.exception), except_error)

    def test_init_invalid_rate(self):
        # Arrange
        loan_amt = 1000
        rate = "VARIABLE_6"
        freq = "MONTHLY"
        amort = 10
        except_error = "Rate provided is invalid: "

        # Act 
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(loan_amt, rate, freq, amort)

        # Assert
        self.assertEqual(str(context.exception), except_error)
    
    def test_init_invalid_frequency(self):
        # Arrange
        loan_amt = 1000
        rate = "VARIABLE_5"
        freq = "YEARLY"
        amort = 10
        except_error = "Frequency provided is invalid: "

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(loan_amt, rate, freq, amort)

        # Assert
        self.assertEqual(str(context.exception), except_error)        
        
    def test_init_invalid_amortization(self):
        # Arrange
        loan_amt = 1000
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 100
        except_error = "Amortization provided is invalid."

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(loan_amt, rate, freq, amort)

        # Assert
        self.assertEqual(str(context.exception), except_error)

    def test_valid_inputs(self):
        # Arrange
        loan_amt = 1000
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10
        
        # Act
        mortgage = Mortgage(loan_amt, rate, freq, amort)

        # Assert
        self.assertEqual(mortgage.loan_amt, loan_amt)
        self.assertEqual(mortgage.rate, MortgageRate[rate])
        self.assertEqual(mortgage.freq, PaymentFrequency[freq])
        self.assertEqual(mortgage.amort, amort)

##Loan Amount:
    def test_negative_loan_amount(self):
        # Arrange
        loan_amt = 30.0
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10
        new_loan = -1000.0
        except_error = "Loan Amount must be positive."
        mortgage = Mortgage(loan_amt, rate, freq, amort)

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amt = new_loan
        self.assertEqual(str(context.exception), except_error)

    def test_zero_loan_amount(self):
        # Arrange
        loan_amt = 30.0
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10
        new_loan = 0.0
        except_error = "Loan Amount must be positive."
        mortgage = Mortgage(loan_amt, rate, freq, amort)

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amt = new_loan
        self.assertEqual(str(context.exception), except_error)

    def test_positive_loan_amount(self):
        # Arrange
        loan_amt = 30.0
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10 
        new_loan_amt = 100

        # Act & Assert
        mortgage = Mortgage(loan_amt, rate, freq, amort)
        mortgage.loan_amt = new_loan_amt
        self.assertEqual(new_loan_amt, mortgage.loan_amt)

## Rate:
    def test_valid_rate(self):
        # Arrange
        loan_amt = 1000
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10
        new_rate = "VARIABLE_1"        
        excepted = MortgageRate[new_rate]

        # Act & Assert
        mortgage = Mortgage(loan_amt, rate, freq, amort)
        mortgage.rate = new_rate
        self.assertEqual(excepted, mortgage.rate)

    def test_invalid_rate(self):
        # Arrange
        loan_amt = 1000
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10
        except_error = "Rate provided is invalid: "
        new_rate = "VARIABLE_6"

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(loan_amt, rate, freq, amort)
            mortgage.rate = new_rate
        self.assertEqual(str(context.exception), except_error)
        
## Frequency:
    def test_valid_frequency(self):
        # Arrange
        loan_amt = 1000
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10
        new_freq = "WEEKLY"
        excepted = PaymentFrequency[new_freq]

        # Act & Assert
        mortgage = Mortgage(loan_amt, rate, freq, amort)
        mortgage.freq = new_freq
        self.assertEqual(excepted, mortgage.freq)

    def test_invalid_frequency(self):
        # Arrange
        loan_amt = 1000
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10
        except_error = "Frequency provided is invalid: "
        new_freq = "YEARLY"

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(loan_amt, rate, freq, amort)
            mortgage.freq = new_freq
        self.assertEqual(str(context.exception), except_error)

## Amortization:
    def test_valid_amortization(self):
        # Arrange
        loan_amt = 1000
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10
        new_amort = 5
        
        # Act & Assert
        mortgage = Mortgage(loan_amt, rate, freq, amort)
        mortgage.amort = new_amort
        self.assertEqual(mortgage.amort, new_amort)

    def test_invalid_amortization(self):
        # Arrange
        loan_amt = 1000
        rate = "VARIABLE_5"
        freq = "MONTHLY"
        amort = 10
        new_amort = 100
        except_error = "Amortization provided is invalid."

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            mortgage = Mortgage(loan_amt, rate, freq, amort)
            mortgage.amort = new_amort
        self.assertEqual(str(context.exception), except_error)

## Calculate Payment:
    def test_calculate_payment_return(self):
        # Arrange
        expected_payment = 7578.30
        ## Adjusted expected value based on the corrected calculation

        # Act 
        mortgage = Mortgage(682912.43, "FIXED_1", "MONTHLY", 10)
        actual_payment = mortgage.calculate_payment()

        # Assert
        self.assertAlmostEqual(expected_payment, actual_payment, 2)

## Monthly Payment:
    def test_mortgage_monthly_string(self):
        # Arrange
        mortgage = Mortgage(682912.43, "FIXED_1", "MONTHLY", 10)

        expected_string = (
            "Mortgage Amount: $682,912.43 "
            "Rate: 5.99% "
            "Amortization: 10 "
            "Frequency: 12 "
            "-- Calculated Payment: $7,578.30 "
        )

        # Act
        actual_string = str(mortgage)

        # Assert
        self.assertEqual(actual_string, expected_string)

## Bi_Weekly Payment:
    def test_mortgage_biweekly_string(self):
        # Arrange
        mortgage = Mortgage(682912.43, "FIXED_1", "BI_WEEKLY", 10)

        expected_string = (
            "Mortgage Amount: $682,912.43 "
            "Rate: 5.99% "
            "Amortization: 10 "
            "Frequency: 26 "
            "-- Calculated Payment: $3,494.25 "
        )

        # Act
        actual_string = str(mortgage)

        # Assert
        self.assertEqual(actual_string, expected_string)

## Weekly Payment:
    def test_mortgage_weekly_string(self):
        # Arrange
        mortgage = Mortgage(682912.43, "FIXED_1", "WEEKLY", 10)

        expected_string = (
            "Mortgage Amount: $682,912.43 "
            "Rate: 5.99% "
            "Amortization: 10 "
            "Frequency: 52 "
            "-- Calculated Payment: $1,746.39 "
        )

        # Act
        actual_string = str(mortgage)

        # Assert
        self.assertEqual(actual_string, expected_string)

    def test_mortgage_repr(self):
        # Arrange
        mortgage = Mortgage(100000.01, "VARIABLE_5", "MONTHLY", 30)

        # Act
        mortgage_repr = repr(mortgage)

        # Assert
        expected_repr = (
            "Mortgage("
            "loan_amt=100000.01, "
            "rate=MortgageRate.VARIABLE_5, "
            "freq=PaymentFrequency.MONTHLY, "
            "amort=30)"
        )
        self.assertEqual(mortgage_repr, expected_repr)