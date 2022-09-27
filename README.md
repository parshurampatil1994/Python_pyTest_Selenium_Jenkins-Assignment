
# Python_pyTest_Selenium_Jenkins-Assignment



## Assignment 1	

1. Create a VM using virtualbox and enable SSH to it

2. Create another python functions and use 'paramiko' python module to SSH to this VM
	
3. Fetch some attributes of the VM like CPU, memory, disk availability, etc and write/append it to a file along with timestamp. This should be done as separate pytest testcases.
	These testcases should pass only if the CPU, memory, disk space is below a certain threshold percentage (CPU is below 90% for example) otherwise the testcases should fail (use asserts here)

4. Add a marker as 'cli' to these tests.

5. Commit automation code on github (your own public repo)

6. Install Jenkins (on a VM or locally). Jenkins should be able to pull automation code from github and run it

7. Create a jenkins job to run the CLI test suite

8. Add logs to testcases	

## Alternate options to try out (after above assignment is done):
- Create VM on any of the Cloud provider's free tier (e.g. AWS/GCP)
- Try using any other module than paramiko for SSH (e.g. SSHLibrary, Exscript, netmiko etc.)
- Create a single Jenkins job for assignment-1 and 2, driven by tags/markers."
									This is optional for now.



## Assignment 2
1. Generate reports for above test suites using pytest-html
2. Integrate allure in jenkins to generate reports for the automated tests



## Assignment 3
1. Create Test suite (a test class with multiple test cases) using Pytest and Selenium framework. Use test parameterization to test the same testcase with multiple inputs. Add marker 'UI' to these testcases
2. Create jenkins job and schedule these jobs which will trigger the Test suite run
3. All results should be uploaded to jenkins
4. Add logs to all the testcases

## Alternate options to try out (after above assignment is done):
- Use Robot Framework instead of PyTest
- Install Jenkins on a VM (created through virtualbox or on any of the Cloud's free tier)
- Create Jenkins pipeline jobs instead of free-style jobs (using groovy scripts)"

