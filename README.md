
**Overview  **
This project automates interactions with the Table Sort and Search Demo page on the LambdaTest Selenium Playground website. It contains three test cases that sequentially perform specific tasks.

---

## Prerequisites  
1. Development Environment: 
   - Install and configure your preferred IDE (e.g., PyCharm, Eclipse, or Visual Studio Code).  
   - Ensure Selenium WebDriver is installed and added to your project's dependencies.  
   - Set up the browser driver (e.g., ChromeDriver, GeckoDriver).

2. Dependencies:  
   - Selenium Library: Ensure you have Selenium installed using `pip install selenium`.  
   - WebDriver: Use the latest version that is compatible with your browser.

3. Test Execution Tool: 
   - If using a test framework (e.g., PyTest,pycharm, python), ensure it is configured properly.

---

Test Cases

Test Case 1: Log in to the Website  
Description:  
Log into the website [Table Sort and Search Demo](https://www.lambdatest.com/selenium-playground/table-sort-search-demo).  

Steps:  
1. Open the browser and navigate to the URL.  
2. Perform any required authentication (if applicable).  

Expected Outcome: 
- Successful login and navigation to the webpage.

---

Test Case 2: Search for "New York"  
Description:  
Automates entering the text "New York" in the search box on the table.  

Steps: 
1. Locate the search box element.  
2. Input the text "New York" into the search box.  
3. Verify that the table dynamically filters results based on the search query.  

Expected Outcome:  
- The table displays rows related to "New York."

---

Test Case 3: Count Rows in the "Office" Column  
Description:  
Counts the rows in the Office column after filtering and checks if only 5 rows are displayed.  

Steps:  
1. Identify the table and locate rows under the Office column.  
2. Count the visible rows.  
3. Compare the count to ensure it does not exceed 5 rows.  

Expected Outcome: 
- The test verifies that the number of rows in the Office column is 5 or fewer.

---

How to Run the Tests  
1. Clone the repository or download the project files.  
2. Open the project in your IDE.  
3. Ensure the WebDriver path is configured correctly.  
4. Execute the test cases sequentially using your test framework or directly from the script.

---

Notes  
- Make sure the browser driver is up-to-date.  
- If the website changes, update the locators (XPath, CSS selectors) in the test script accordingly.  
- Ensure a stable internet connection while running tests.  

--- 

Troubleshooting  
- Issue: Locators not found.  
  -Solution: Verify the element XPath or CSS selector using the browser's developer tools.  
- Issue: WebDriver version mismatch.  
  Solution: Update the WebDriver to match your browser version.  

--- 

## Contact  
If you have any questions or need any help, please contact [Email= aditya1993tue@gmail.com].
