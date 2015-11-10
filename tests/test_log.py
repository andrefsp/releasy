import unittest
from releasy.repo import Repository
from releasy.log import PrettyLog, DetailedLog


class DetailedLogTestCase(unittest.TestCase):

    def test_detail_message(self):
        log = DetailedLog([
                'Merge pull request #55 from madedotcom/OE-893-get-rid-of-lines-from-db',
                '', 'Removing the storage of item lines for pallets event'],
                project_regex='OE-\d+')
        self.assertEqual(log.pull_request, '55')
        self.assertEqual(log.project_ticket, 'OE-893')


class LogTestCase(unittest.TestCase):

    def test_get_pretty_log_message(self):
        repo = Repository()
        commits = repo.get_commits_since_tag(repo.get_latest_tag(regex='v\d+'))
        PrettyLog(commits).commit_message_map



if __name__ == "__main__":
    unittest.main()
