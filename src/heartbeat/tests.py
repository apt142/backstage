from django.test import TestCase


class ViewTests(TestCase):
    def test_heartbeat(self):
        """Up should respond with a success 200."""
        response = self.client.get("/heartbeat/", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_heartbeat_databases(self):
        """Up databases should respond with a success 200."""
        response = self.client.get("/heartbeat/databases", follow=True)
        self.assertEqual(response.status_code, 200)
