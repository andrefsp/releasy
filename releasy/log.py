import os
import re


class DetailedLog:

    @property
    def github_pull_request_url(self):
        return "%spull/%s" % (self.github_url, self.pull_request)

    @property
    def jira_ticket_url(self):
        return "%s%s" % (self.jira_browse_url, self.project_ticket)

    @property
    def pull_request(self):
        for line in self.commit_message:
            match = re.match(r".*pull request \#(?P<pull_request>\d+)", line)
            if match:
                return match.groupdict()['pull_request']

    @property
    def project_ticket(self):
        for line in self.commit_message:
            match = re.match(r".*(?P<project_ticket>%s)" % self.project_regex, line)
            if match:
                return match.groupdict()['project_ticket']

    def to_map(self):
        map = {
            'commit_message': self.commit_message
        }
        if self.pull_request:
            map['github_pull_request_url'] = self.github_pull_request_url
        if self.project_ticket:
            map['jira_ticket_url'] = self.jira_ticket_url

        return map

    def __init__(self, commit_message, project_regex=os.environ.get('PROJECT_TICKET_REGEX')):
        self.commit_message = [line for line in filter(lambda line: bool(line),  commit_message)]
        self.project_regex = project_regex
        self.jira_browse_url = os.environ.get('JIRA_BROWSE_URL', "https://jira.made.com/browse/")
        self.github_url = os.environ.get('GITHUB_URL', 'https://github.com/madedotcom/warehouse/')


class PrettyLog:

    @property
    def detailed_log_map(self):
        return {commit: DetailedLog(message).to_map() for commit, message in self.commit_message_map.items()}

    @property
    def commit_message_map(self):
        return {str(commit): commit.message.split('\n') for commit in self.commits}

    def __init__(self, commits):
        self.commits = commits

