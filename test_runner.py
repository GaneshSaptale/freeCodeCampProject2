# Load the unit tests from the UnitTests class
suite = unittest.TestLoader().loadTestsFromTestCase(
    unit_tests.UnitTests)

# Open os.devnull to discard the test runner output
f = open(os.devnull,"w")

# Run the test suite with the TextTestRunner and capture the results
test_res = unittest.TextTestRunner(stream=f).run(suite)

# Merge the errors and failures and convert them into a normalized format of {name, stack}
failures = [
    {
        "name": r[0]._testMethodName,  # get the name of the failed test
        "stack": r[1],  # get the traceback of the error/failure
    } for r in test_res.errors + test_res.failures  # combine the errors and failures
]

# Print the test results in a JSON format
print('\n__GLOBAL_UNIT_TEST_RESULTS__')  # header
sleep(1)  # wait for 1 second to ensure the header is printed before the results
print(json.dumps({
    "passed": test_res.wasSuccessful(),  # check if all tests passed
    "failures": failures,  # list of failures and errors
}))
print()  # empty line for readability
