"""Sets an example for nosetests using regen postgres image."""
import unittest
import requests


class TestExample(unittest.TestCase):
    """Unittest class that helps building pumpwood based systems test."""

    def setUp(self, *args, **kwargs):
        """Regen the database in the setUp calling reload end-point."""
        ######################
        # Regenerate database#
        for app in self.apps_to_regenerate:
            response = requests.get(
                "http://0.0.0.0:5000/reload-db/regen-test/")
            if response.status_code != 200:
                raise Exception(app + ' regenerate: ', response.text)
        #####################
