"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: Raven Manalastas
Date: 20 March 2024
"""

### REQUIREMENT
### ADD IMPORT STATEMENT FOR THE MORTGAGE CLASS
from mortgage.mortgage import Mortgage
import traceback

### REQUIREMENT
### ADD IMPORT STATEMENT FOR THE MORTGAGE CLASS
def insecure_eval(val):
    return eval(f'"{val}"')

### REQUIREMENT
### ENCLOSE THE FOLLOWING 'WITH OPEN' BLOCK IN A 'TRY-EXCEPT' BLOCK WHICH 
### WILL CATCH A 'FILENOTFOUNDERROR' EXCEPTION
try:
    with open("data\\pixell_river_mortgages.txt", "r") as input:
        print("**************************************************")

        for data in input:
            items = data.split(",")

            try:
                amount = float(items[0])
                rate = insecure_eval(items[1])
                amortization = int(items[2])
                frequency = insecure_eval(items[3])

            ### REQUIREMENT:
            ### INSTANTIATE A MORTGAGE OBJECT USING THE VALUES
            ### FOR AMOUNT, RATE, FREQUENCY AND AMORTIZATION ABOVE.
                mortgage = Mortgage(amount, rate, frequency, amortization)
            
            ### REQUIREMENT:
            ### PRINT THE MORTGAGE OBJECT
                print(mortgage)

            except ValueError as e:
                # This except block will catch Explicit exceptions: 
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: {data.strip()} caused Exception: {e}")

            except Exception as e:
                # This except block will catch Implicit exceptions:  
                # Those raised through normal execution.
                  print(f"Data: {data.strip()} caused Exception: {e}")
                traceback.print_exc()

except FileNotFoundError as e:
    # This except block will catch the specified exception
    print(f"File: {e} not found.")

finally:
    print("**************************************************")
