import unittest
from unittest.mock import patch, MagicMock
from src.migration import migrate_vm

class TestMigration(unittest.TestCase):
    @patch("src.cloud_api.CloudAPI")
    @patch("src.sdn_controller.SDNController")
    def test_migrate_vm(self, MockSDNController, MockCloudAPI):
        # Mock cloud API behavior
        mock_source_cloud = MockCloudAPI.return_value
        mock_target_cloud = MockCloudAPI.return_value
        mock_source_cloud.get_vm.return_value = {"id": "vm-12345", "name": "test-vm"}
        mock_source_cloud.export_vm_image.return_value = b"mock-vm-image"
        mock_target_cloud.import_vm_image.return_value = "vm-67890"
        
        # Mock SDN controller behavior
        mock_sdn = MockSDNController.return_value
        mock_sdn.update_network.return_value = None
        
        # Run the migration
        new_vm_id = migrate_vm("vm-12345")
        
        # Assertions
        mock_source_cloud.get_vm.assert_called_once_with("vm-12345")
        mock_source_cloud.export_vm_image.assert_called_once_with("vm-12345")
        mock_target_cloud.import_vm_image.assert_called_once_with(b"mock-vm-image")
        mock_sdn.update_network.assert_called_once_with("vm-12345", "vm-67890")
        
        self.assertEqual(new_vm_id, "vm-67890")

if __name__ == "__main__":
    unittest.main()
