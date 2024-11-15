import requests
from src.utils import log

class SDNController:
    def __init__(self, config):
        self.url = config["url"]
        self.token = config["auth_token"]

    def update_network(self, old_vm_id, new_vm_id):
        log(f"Updating network for VM {old_vm_id} -> {new_vm_id}")
        response = requests.post(
            f"{self.url}/update",
            json={"old_vm_id": old_vm_id, "new_vm_id": new_vm_id},
            headers={"Authorization": f"Bearer {self.token}"}
        )
        if response.status_code == 200:
            log("Network updated successfully.")
        else:
            log("Failed to update network:", response.text)
