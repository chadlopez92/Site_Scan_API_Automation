# SiteScan API Automation Scripts

## Overview

This repository contains Python scripts that interact with the [SiteScan API](https://www.esri.com/en-us/arcgis/products/arcgis-reality/products/site-scan-for-arcgis) to automate various tasks. To  These scripts were conceptualized and integrated by Chad Lopez, with code generation assistance from ChatGPT. Note: A SiteScan custom subscription is required to access the API token. Some scripts may also require an [ArcGIS Professional](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview) subscription.

## Features and Functionality

1. **Create, Upload, and Process Missions**:
    - Automatically creates new missions with names based on the current date and time.
    - Uploads images from a specified directory, supporting various image formats.
    - Initiates mission processing automatically after the images are uploaded.

2. **Retrieve and Download Recent Orthomosaic**:
    - Automatically fetches the URL of the most recent orthomosaic for a given project.
    - Downloads the orthomosaic file to a specified directory.

3. **Retrieve Usage Statistics**:
    - Fetches usage statistics for an organization from the SiteScan API.
    - Supports filtering statistics by a specified start and end date.
    - Optionally group statistics by project or user.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/chadlopez92/SiteScan_API_Automation.git
    cd SiteScan_API_Automation
    ```

2. **Install Required Libraries:**
    ```bash
    pip install requests
    ```

## Configuration

### Create, Upload, and Process Missions

Set your Project ID, Directory Path, and API Token in the `create_upload_process.py` script:
```python
api_token = 'Your_API_Token'
project_id = 'Your_Project_ID'
directory_path = 'Your_Directory_Path'
