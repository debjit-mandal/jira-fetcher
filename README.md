# Jira Fetcher
**Data fetcher from Jira using Python**

Jira is a software application developed by the Australian software company Atlassian that allows teams to track issues, manage projects, and automate workflows. You can read more about Jira in https://en.wikipedia.org/wiki/Jira_(software)

Data can be fetched from Jira by using the Jira Python library, which provides a convenient interface for interacting with Jira's REST API. 

The configuration, required, in the Jira software tool, is as follows:

- Create a Jira user account.

- Create a domain name, add a project, and, record some issues, or, bugs. The code will fetch, issues data, using Python code.

- You need to have, a valid token, for authentication, which can be obtained, from link  https://id.atlassian.com/manage/api-tokens.

Make sure you have the `jira` library installed. You can install it using pip:

`pip install jira`


Make sure to replace 'https://your-jira-instance.com' with the URL of your Jira instance. Set 'your-username' and 'your-api-token' to your Jira username and API token respectively. 

To run this code locally:

`git clone https://github.com/debjit-mandal/jira-fetcher`

`cd jira-fetcher`

`python main.py`

Feel free to suggest any kind of improvements.



