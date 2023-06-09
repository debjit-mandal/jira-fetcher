# Jira Fetcher
**Jira Data Extraction using Python**

Jira is a software application developed by the Australian software company Atlassian that allows teams to track issues, manage projects, and automate workflows. You can read more about Jira in https://en.wikipedia.org/wiki/Jira_(software)

Data can be fetched from Jira by using the Jira Python library, which provides a convenient interface for interacting with Jira's REST API. 

The configuration, required, in the Jira software tool, is as follows:

- Create a [Jira user account](https://id.atlassian.com/login/authorize?token=eyJraWQiOiJtaWNyb3NcL2FpZC1zaWdudXBcL29zaGlrcDM4ZjNxMDJwc2ciLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJsaW5rLXNpZ25hdHVyZS12YWxpZGF0b3IiLCJtYXJrZWRWZXJpZmllZCI6ImZhbHNlIiwiY3NyZlRva2VuIjoiMDVhZmRlZWM0YjI4YWUzM2JkZWFlN2JjNWUxMzYyOWZkMWQ5ZGE3NSIsIm5iZiI6MTYyMTY3MTY0MCwibG9naW5UeXBlIjoic2Vzc2lvblJlZnJlc2giLCJzY29wZSI6IkxvZ2luIiwiaXNzIjoibWljcm9zXC9haWQtc2lnbnVwIiwiZXhwIjoxNjIxNjcxNzYwLCJ1c2VySWQiOiI2MGE1ZDlkMjliMzYyZjAwNjkxNjRmMzMiLCJpYXQiOjE2MjE2NzE2NDAsImp0aSI6ImU0MWQ0NWQ1LTM4M2QtNGVmYS1iZWJmLWM2Zjc1YzkzNzk1ZSJ9.iBKybIHmEfsSqN9o5likCULZJq6F8hMNDPw7YDSvnBa5ChBCf8WXqVo64bVqIyrnV8miH-jo2JqdDLYaOzIdu2fe0MLt7P8MnaCI41_YvNJWeCSziAmDOCZgcAh8dDstAnLiaJo-kL9i9-Lsq8GLGKcOPWOet4FBqT_XdpoiAHfkqOvuz_khoFy74O6zfu-CgFa3VuCef1iAj0W-7uiI_iexBj7rTGJPN0UeKmsnBZGhqUPF7pgnKKlKTIioYrDrRJJvO_KTOQtfh1D2lA07-HPsfKOkWFV5LVEHgLaM3CtzSKwTm4YplaZJLPi7Kd79dzDKajezp6ADkySvBJCY1g).

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



