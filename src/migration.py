import json
from src.cloud_api import CloudAPI
from src.sdn_controller import SDNController
from src.utils import log

def migrate_vm(vm_id):
    # Load configuration
    with open("config/config.json") as f:
        config = json.load(f)

    source_cloud = CloudAPI(config["source_cloud"])
    target_cloud = CloudAPI(config["target_cloud"])
    sdn_controller = SDNController(config["sdn_controller"])

    log("Initializing migration for VM:", vm_id)

    # Retrieve VM details from source cloud
    vm_details = source_cloud.get_vm(vm_id)
    log("VM details retrieved:", vm_details)

    # Migrate VM to target cloud
    vm_image = source_cloud.export_vm_image(vm_id)
    new_vm_id = target_cloud.import_vm_image(vm_image)
    log(f"VM migrated to target cloud with ID: {new_vm_id}")

    # Update network configuration
    sdn_controller.update_network(vm_id, new_vm_id)
    log("Network reconfiguration completed.")

    log("Migration complete.")
    return new_vm_id

if __name__ == "__main__":
    vm_id = "vm-12345"
    migrate_vm(vm_id)
