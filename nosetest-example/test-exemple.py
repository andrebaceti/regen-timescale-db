"""Sets an example for nosetests using regen postgres image."""
import unittest
import requests


class TestExample(unittest.TestCase):
    """Unittest class that helps building pumpwood based systems test."""

    load_balancer_address = None
    'Ip of the load balancer'
    apps_to_regenerate = []
    'Name of the apps to be regenerated after the test is over'

    def setUp(self, *args, **kwargs):
        """Regen the database in the setUp calling reload end-point."""
        ######################
        # Regenerate database#
        for app in self.apps_to_regenerate:
            path = 'reload-db/' + app + '/'
            response = requests.get(self.load_balancer_address + path)
            if response.status_code != 200:
                raise Exception(app + ' regenerate: ', response.text)
        #####################
