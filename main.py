import logging
import os
import configparser
import argparse
from jira import JIRA

class JiraClient:
    def __init__(self, jira_server, username, api_token):
        self.jira = JIRA(
            server=jira_server,
            basic_auth=(username, api_token)
        )

    def fetch_issue(self, issue_key):
        try:
            issue = self.jira.issue(issue_key)
            return issue
        except Exception as e:
            logging.exception(f"Error fetching issue '{issue_key}': {str(e)}")
            return None

    def fetch_issues(self, jql_query, max_results=100):
        try:
            start_at = 0
            issues = []

            while True:
                fetched_issues = self.jira.search_issues(jql_query, startAt=start_at, maxResults=max_results)

                if not fetched_issues:
                    break

                issues.extend(fetched_issues)
                start_at += max_results

            return issues
        except Exception as e:
            logging.exception(f"Error fetching issues: {str(e)}")
            return []

def configure_logger(log_file):
    logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file,
        filemode='a'
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(message)s'))
    logging.getLogger('').addHandler(console_handler)

def main(issue_key, jql_query):
    try:
        # Load configuration from file
        config_file = 'config.ini'
        if not os.path.exists(config_file):
            raise FileNotFoundError(f"Configuration file '{config_file}' not found.")

        config = configparser.ConfigParser()
        config.read(config_file)

        # Configure logger
        log_file = config['Logging']['log_file']
        configure_logger(log_file)

        # Read Jira configuration
        jira_config = config['Jira']
        jira_server = jira_config['jira_server']
        username = os.environ.get('JIRA_USERNAME') or jira_config['username']
        api_token = os.environ.get('JIRA_API_TOKEN') or jira_config['api_token']

        # Initialize Jira client
        jira_client = JiraClient(jira_server, username, api_token)

        # Fetch an issue by its key
        issue = jira_client.fetch_issue(issue_key)
        if issue:
            logging.info(f"Key: {issue.key}")
            logging.info(f"Summary: {issue.fields.summary}")
            logging.info(f"Description: {issue.fields.description}")
            logging.info(f"Status: {issue.fields.status.name}")
            logging.info('---')

        # Fetch multiple issues using JQL (Jira Query Language)
        issues = jira_client.fetch_issues(jql_query)

        # Print issue details
        for issue in issues:
            logging.info(f"Key: {issue.key}")
            logging.info(f"Summary: {issue.fields.summary}")
            logging.info(f"Description: {issue.fields.description}")
            logging.info(f"Status: {issue.fields.status.name}")
            logging.info('---')

    except FileNotFoundError as e:
        logging.error(str(e))
    except Exception as e:
        logging.exception(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch data from Jira.')
    parser.add_argument('--issue', help='Jira issue key', required=True)
    parser.add_argument('--jql', help='JQL query', required=True)
    args = parser.parse_args()

    main(args.issue, args.jql)
