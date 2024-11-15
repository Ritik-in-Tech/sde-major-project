# Virtual Machine Cluster Mobility in Inter-Cloud Platforms

## Overview

This project focuses on enabling seamless migration of Virtual Machine (VM) clusters across heterogeneous cloud platforms using Software-Defined Networking (SDN). The proposed solution minimizes downtime, maintains network connectivity, and ensures consistent performance during migrations.

## Features

#### Seamless VM Cluster Migration: Retain network connectivity and internal communication during migration.

#### SDN Integration: Use technologies like OpenFlow, VXLAN, and GRE tunneling for dynamic network reconfiguration.

#### OpenStack Integration: Tested on OpenStack, a widely used open-source cloud platform.

#### Performance Benchmarking: Metrics include migration time, downtime, and network reconfiguration time.

## Architecture

### Key Components

##### Inter-Cloud Bridge System:

1. Mediation Service: Manages API interactions and synchronizes configurations.
2. Migration Service: Transfers VMs and updates configurations in the destination cloud.

##### Application Layer:

1. Ensures static internal endpoints for uninterrupted application functionality.
1. Control Layer: Manages SDN-based dynamic network reconfiguration.
1. Cloud Platform Layer: Represents network infrastructure and enables seamless migration through SDN control.

## Migration Flow

#### Migration Initialization:

1. Authenticate with source and target clouds.
2. Collect and prepare VM configurations for migration.

#### Data Transfer and Reconfiguration:

1. Transfer VM images and dynamically update network settings using SDN.

#### Network Updates:

1. Use SDN controllers to adjust routing rules and ensure connectivity.

## Performance Metrics

1. Migration Time: Minimize the time required for VM transfer and setup.
2. Downtime: Achieve near-zero service interruptions.
3. Scalability: Efficiently handle simultaneous migrations of multiple VMs.

## Tools and Technologies

1. OpenStack: Primary cloud platform for implementation.
2. SDN Protocols: OpenFlow, VXLAN, GRE for network configuration.
3. Languages/Frameworks: Python, REST APIs for cloud interactions.

## Testing and Benchmarking

#### Test Scenarios:

1. Single VM migration.
2. Clustered VM migrations.

#### Performance Tests:

1. Measure migration time, downtime, and reconfiguration efficiency.

## Future Enhancements

1. Expand compatibility to additional cloud platforms.
2. Incorporate AI for predictive resource allocation.
3. Optimize migration for large-scale deployments.

## Getting Started

#### Prerequisites

1. OpenStack deployment.
2. SDN controller setup (OpenFlow-compatible).
3. Python 3.x and required libraries.

## Installation

1. Clone the repository

```bash
git clone https://github.com/Ritik-in-Tech/sde-major-project.git
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

3. Configure cloud API credentials and SDN settings in config.json.

4. Run migration scripts

```bash
python migrate.py --source <source-cloud> --target <target-cloud>
```

## How to run tests

1. Install unittest (usually pre-installed with Python).
2. Run the tests using the following command:

```bash
python -m unittest discover -s tests
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
