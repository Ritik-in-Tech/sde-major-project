import unittest
from unittest.mock import patch
from src.cloud_api import CloudAPI

class TestCloudAPI(unittest.TestCase):
    @patch("src.cloud_api.requests.get")
    def test_get_vm(self, mock_get):
        # Mock API response
        mock_get.return_value.json.return_value = {"id": "vm-12345", "name": "test-vm"}
        
        # Create CloudAPI instance
        cloud = CloudAPI({"url": "http://source-cloud.example.com", "api_key": "test-key"})
        
        # Test get_vm
        vm = cloud.get_vm("vm-12345")
        self.assertEqual(vm["id"], "vm-12345")
        mock_get.assert_called_once_with(
            "http://source-cloud.example.com/vms/vm-12345",
            headers={"API-Key": "test-key"}
        )

    @patch("src.cloud_api.requests.post")
    def test_import_vm_image(self, mock_post):
        # Mock API response
        mock_post.return_value.json.return_value = {"vm_id": "vm-67890"}
        
        # Create CloudAPI instance
        cloud = CloudAPI({"url": "http://target-cloud.example.com", "api_key": "test-key"})
        
        # Test import_vm_image
        vm_id = cloud.import_vm_image(b"mock-vm-image")
        self.assertEqual(vm_id, "vm-67890")
        mock_post.assert_called_once_with(
            "http://target-cloud.example.com/vms/import",
            data=b"mock-vm-image",
            headers={"API-Key": "test-key"}
        )

if __name__ == "__main__":
    unittest.main()
