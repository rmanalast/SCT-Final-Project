"""
Description: A class meant to manage Mortgage options.
Author: Raven Manalastas
Date: 20 March 2024
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    
    def __init__(self, loan_amt: float, rate: str, freq: str, amort: int):
        """
        Initialize a new Mortgage object with the given parameters.

        Parameters:
            loan_amount (float):
            The amount of the mortgage loan.

            rate (str):
            The annual interest rate string equivalent to enum value.

            frequency (str): 
            The number of payments per year string equivalent to enum value.

            amortization (int):
            The number of years to repay the mortgage loan.

        Return: 
            None

        Raises:
            ValueError: Loan Amount must be positive.
            ValueError: Rate provided is invalid:
            ValueError: Frequency provided is invalid:
            ValueError: Amortization providedis invalid.

        """
        self._loan_amt = loan_amt

        try:
            self._rate = MortgageRate[rate]
        except Exception as e:
            raise ValueError("Rate provided is invalid.")

        try:
            self._freq = PaymentFrequency[freq]
        except Exception as e:
            raise ValueError("Frequency provided is invalid.")

        if amort not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self._amort = amort

    @property
    def loan_amt(self):
        """
        Accessor for the lona_amount attribute
        """
        return self._loan_amt

    @loan_amt.setter
    def loan_amt(self, loan_amt):
        """
        Setter method for the 'loan_amount' attribute

        Args:
            Amount: a non-negative number reprsenting the loan amount

        Raises:
            ValueError: Loan Amount must be positive.
        """
        self._loan_amt = loan_amt

    
    @property
    def rate(self):
        """
        Accessor for the rate attribute
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Setter method for the 'rate' attribute

        Args:
            Rate: A string representing the rate value


        Raises:
            ValueError: Rate provided is invalid.
        """
        try:
            self._rate = MortgageRate[rate.upper()]
        except Exception as e:
            raise ValueError("Rate provided is invalid: ")
        
    
    @property
    def freq(self):
        """
        Accessor for the frequency attribute
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """
        Setter method for the 'frequency' attribute

        Args:
            Frequency: A string representing the payment frequency 

        Raises:
            ValueError: Frequency provided is invalid.
        """
        try:
            self._freq = PaymentFrequency[freq.upper()]
        except Exception as e:
            raise ValueError("Frequency provided is invalid: ")
        
    @property
    def amort(self):
        """
        Accessor for the frequency attribute
        """
        return self._amort

    @amort.setter
    def amort(self, amort):
        """
        Setter method for the 'frequency' attribute

        Args:
            Amortization: The number of years to repay the mortgage loan

        Raises:
            ValueError: Amortization provided is invalid.
        """
        if amort in VALID_AMORTIZATION:
            self._amort = amort
        else:
            raise ValueError("Amortization provided is invalid.")

    def calculate_payment(self) -> float:
        """
        Calculate the mortgage payment amount based on the mortgage details.
        """
        i = self._rate.value / self._freq.value
        n = self._amort * self._freq.value
        numer = i * (1 + i) ** n
        denom = (1 + i) ** n - 1
        loan_pay = self.loan_amt

        return loan_pay * numer / denom
    
    def __str__(self):
        """
        Return a string representation of the Mortgage object.
        """
        payment_amt = self.calculate_payment()
        
        return f"Mortgage Amount: ${self.loan_amt:,.2f} " \
               f"Rate: {self.rate.value * 100:.2f}% " \
               f"Amortization: {self._amort} " \
               f"Frequency: {self.freq.value} " \
               f"-- Calculated Payment: ${payment_amt:,.2f} "
               
    def __repr__(self):
        """
        Return a string representation of the Mortgage object in the format:
        [loan_amount, rate, amortization, frequency]
        """
        return (
            f"Mortgage("
            f"loan_amt={self.loan_amt}, "
            f"rate={self.rate}, "
            f"freq={self.freq}, "
            f"amort={self.amort})"
        )