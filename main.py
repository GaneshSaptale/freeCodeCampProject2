# Import the add_time function from time_calculator module and main function from unittest module
from time_calculator import add_time
from unittest import main

# Call the add_time function and print the output
print(add_time("11:06 PM", "2:02"))

# Run the unit tests from test_module and prevent the test runner from exiting
# so that the result of the tests can be examined
main(module='test_module', exit=False)
