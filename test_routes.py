
import unittest

from service import create_app


class AccountRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        # Reset temporary in-memory storage before each test.
        from service import routes
        routes.accounts.clear()
        routes.next_id = 1

    def test_create_account(self):
        response = self.client.post(
            "/accounts",
            json={"name": "Test Account", "email": "test@example.com"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["name"], "Test Account")

    def test_list_accounts(self):
        self.client.post(
            "/accounts",
            json={"name": "Test Account", "email": "test@example.com"}
        )
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_read_account(self):
        self.client.post(
            "/accounts",
            json={"name": "Test Account", "email": "test@example.com"}
        )
        response = self.client.get("/accounts/1")
        self.assertEqual(response.status_code, 200)

    def test_update_account(self):
        self.client.post(
            "/accounts",
            json={"name": "Test Account", "email": "test@example.com"}
        )
        response = self.client.put("/accounts/1", json={"name": "Updated"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Updated")

    def test_delete_account(self):
        self.client.post(
            "/accounts",
            json={"name": "Test Account", "email": "test@example.com"}
        )
        response = self.client.delete("/accounts/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get("/accounts/1").status_code, 404)

    def test_create_requires_fields(self):
        response = self.client.post("/accounts", json={"name": "Missing email"})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
