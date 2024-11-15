import unittest
from unittest.mock import patch
from src.sdn_controller import SDNController

class TestSDNController(unittest.TestCase):
    @patch("src.sdn_controller.requests.post")
    def test_update_network_success(self, mock_post):
        # Mock successful response
        mock_post.return_value.status_code = 200
        
        # Create SDNController instance
        sdn = SDNController({"url": "http://sdn-controller.example.com", "auth_token": "test-token"})
        
        # Run update_network
        sdn.update_network("vm-12345", "vm-67890")
        
        # Assertions
        mock_post.assert_called_once_with(
            "http://sdn-controller.example.com/update",
            json={"old_vm_id": "vm-12345", "new_vm_id": "vm-67890"},
            headers={"Authorization": "Bearer test-token"}
        )

    @patch("src.sdn_controller.requests.post")
    def test_update_network_failure(self, mock_post):
        # Mock failure response
        mock_post.return_value.status_code = 500
        mock_post.return_value.text = "Internal Server Error"
        
        # Create SDNController instance
        sdn = SDNController({"url": "http://sdn-controller.example.com", "auth_token": "test-token"})
        
        # Test update_network
        with self.assertLogs(level="INFO") as log:
            sdn.update_network("vm-12345", "vm-67890")
        self.assertIn("Failed to update network", log.output[0])

if __name__ == "__main__":
    unittest.main()
