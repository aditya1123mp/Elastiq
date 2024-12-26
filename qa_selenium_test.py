import test_case_001_for_Elastiq
import test_case_002_for_Elastiq
import test_case_003_for_Elastiq

def run_all_scripts():
    # Load the webpage using the first test case
    print("Loading the webpage...")
    driver = test_case_001_for_Elastiq.main()  # Ensure this function returns a WebDriver instance

    # Run the second test case, passing the driver if needed
    print("Running test_case_002_for_Elastiq...")
    test_case_002_for_Elastiq.main(driver)  # Ensure this accepts the driver argument

    # Run the third test case
    print("Running test_case_003_for_Elastiq...")
    test_case_003_for_Elastiq.main(driver)  # Ensure this accepts the driver argument

if __name__ == "__main__":
    run_all_scripts()
