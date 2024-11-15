import requests
from src.utils import log

class CloudAPI:
    def __init__(self, config):
        self.url = config["url"]
        self.api_key = config["api_key"]

    def get_vm(self, vm_id):
        log(f"Fetching VM details for {vm_id}")
        response = requests.get(f"{self.url}/vms/{vm_id}", headers={"API-Key": self.api_key})
        return response.json()
    
    def export_vm_image(self, vm_id):
        log(f"Exporting VM image for {vm_id}")
        response = requests.get(f"{self.url}/vms/{vm_id}/export", headers={"API-Key": self.api_key})
        return response.content

    def import_vm_image(self, vm_image):
        log("Importing VM image to target cloud.")
        response = requests.post(f"{self.url}/vms/import", data=vm_image, headers={"API-Key": self.api_key})
        return response.json()["vm_id"]
