import unittest
from releasy.repo import Repository


class RepoTestCase(unittest.TestCase):

    def test_repo(self):
        repo = Repository()
        self.assertTrue(len([commit for commit in repo.commits]) > 1)
        self.assertTrue(True)

    def test_we_can_filter_commits_for_tags(self):
        repo = Repository()
        self.assertTrue(len(repo.get_commits_since_tag(repo.tags[0])) > 1)

    def test_we_can_get_latest_tag_for_a_prefix(self):
        repo = Repository()
        self.assertEqual(repo.tags[0], repo.get_latest_tag())
        self.assertEqual(repo.tags[0], repo.get_latest_tag(regex='v\d+'))


if __name__ == "__main__":
    unittest.main()
