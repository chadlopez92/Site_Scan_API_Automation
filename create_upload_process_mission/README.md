# Automated Image Upload and Mission Processing Script

## Overview

This Python script automates the creation of missions, the uploading of images, and the initiation of mission processing using the SiteScan API. The script was conceptualized and integrated by Chad Lopez, with code generation assistance from ChatGPT.

## Features

- Dynamic Mission Creation: Automatically creates new missions with names based on the current date and time.
- Efficient Image Upload: Uploads images from a specified directory, supporting various image formats.
- Mission Processing: Initiates mission processing automatically after the images are uploaded.

## Requirements

- Python 3.8 or higher
- Required Python libraries:
    ```python
    pip install requests
    ```

## Installation

1. Clone the Repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install Required Libraries:
    ```bash
    pip install requests
    ```

## Configuration

1. Set Your Project ID and API Token:
    ```python
    project_id = 'Your_Project_ID'
    directory_path = r'Path_to_your_Image_directory'
    api_token = 'your_API_token'
    ```

2. Ensure Your Directory Contains Supported Image Formats:
    - Supported formats include: `.png`, `.jpg`, `.jpeg`, `.tiff`, `.bmp`, `.gif`.

## Usage

1. Run the Script:
    ```bash
    python your_script_name.py
    ```

2. Monitor the Output:
    - The script will create a new mission and print the mission ID and name.
    - It will then upload each image from the specified directory.
    - Finally, it will initiate mission processing and print the status.

## Example Script

```python
import os
import requests
from datetime import datetime

project_id = 'Your_Project_ID'
directory_path = r'Path_to_your_Image_directory'
api_token = 'your_API_token'

# Get the current date and time
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Step 1: Create a new mission with a dynamic name
mission_name = f'Mission_upload_date_{current_time}'

create_mission_url = 'https://sitescan-api.arcgis.com/api/v2/missions'
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}
payload = {
    'name': mission_name,
    'projectId': project_id
}
response = requests.post(create_mission_url, headers=headers, json=payload)
response.raise_for_status()
mission_data = response.json()
mission_id = mission_data['id']
print(f'Created new mission with ID: {mission_id} and name: {mission_name}')

# Step 2: Upload images to the mission
url = f'https://sitescan-api.arcgis.com/api/v2/missions/{mission_id}/media'
headers = {
    'Authorization': f'Bearer {api_token}'
}
for filename in os.listdir(directory_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        print(f'Uploading {filename}...')
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'rb') as image_file:
            files = {'file': (filename, image_file, 'image/jpeg')}
            response = requests.post(url, headers=headers, files=files)
            if response.status_code == 200:
                print('Image uploaded successfully.')
            else:
                print('Image upload failed.')
                print(f'Status Code: {response.status_code}')
                print(f'Response: {response.text}')
    else:
        print(f'Skipping {filename}, not a supported image format.')

# Step 3: Process the mission
process_url = f'https://sitescan-api.arcgis.com/api/v2/missions/{mission_id}/process/default'
process_payload = {
    'meshEngine': 'off'
}
response = requests.post(process_url, headers=headers, json=process_payload)
if response.status_code == 200:
    print('Mission processing successfully initiated.')
else:
    print('Failed to initiate mission processing.')
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')
