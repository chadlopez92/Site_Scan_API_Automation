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

# Headers including the Authorization token
headers = {
    'Authorization': f'Bearer {api_token}'
}

# Go through each file in the directory
for filename in os.listdir(directory_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        print(f'Uploading {filename}...')

        # Full path to the image file
        file_path = os.path.join(directory_path, filename)

        # Open the file in binary-read mode
        with open(file_path, 'rb') as image_file:
            # The 'files' parameter is used to upload files in a multipart/form-data format.
            files = {'file': (filename, image_file, 'image/jpeg')}

            # Make a POST request to upload the file
            response = requests.post(url, headers=headers, files=files)

            # Check if the request was successful
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