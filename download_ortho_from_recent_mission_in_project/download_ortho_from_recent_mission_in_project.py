import os
import requests

def get_recent_ortho_url(api_token, project_id, directory_path):
    """
    Retrieves the URL of the most recent orthomosaic from the SiteScan API and downloads the orthomosaic file.
    
    Parameters:
    - api_token (str): The API token for authenticating with the SiteScan API.
    - project_id (str): The ID of the project to retrieve missions from.
    - directory_path (str): The local directory path where the downloaded file should be saved.
    
    Returns:
    - str: The file path of the downloaded orthomosaic, or an error message if something goes wrong.
    """
    print("Starting to retrieve the most recent orthomosaic URL...")
    
    # Set up headers for the API request
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }

    # Construct the URL to list missions for the given project
    list_missions_url = f'https://sitescan-api.arcgis.com/api/v2/projects/{project_id}/missions'
    try:
        # Make a GET request to retrieve the list of missions
        missions_response = requests.get(list_missions_url, headers=headers)
        missions_response.raise_for_status()
        missions = missions_response.json()
    except requests.RequestException as e:
        # Return an error message if the request fails
        return f"Error retrieving missions: {str(e)}"

    # Filter the missions to find completed ones (those with 'endTime')
    completed_missions = [m for m in missions if 'endTime' in m]
    if not completed_missions:
        return "No completed missions found for the given project."
    
    # Find the most recent completed mission based on 'endTime'
    most_recent_mission = max(completed_missions, key=lambda x: x['endTime'])
    mission_id = most_recent_mission['id']

    # Construct the URL to get details of the most recent mission
    mission_details_url = f'https://sitescan-api.arcgis.com/api/v2/missions/{mission_id}'
    try:
        # Make a GET request to retrieve mission details
        mission_details_response = requests.get(mission_details_url, headers=headers)
        mission_details_response.raise_for_status()
        mission_details = mission_details_response.json()
    except requests.RequestException as e:
        # Return an error message if the request fails
        return f"Error retrieving mission details: {str(e)}"

    # Extract the orthomosaic data from the mission details
    ortho_data = mission_details.get('data', {}).get('ortho', {}).get('current', {})
    if ortho_data:
        ortho_url = ortho_data.get('url')
        if ortho_url:
            # Construct the file path for saving the orthomosaic
            file_name = ortho_url.split('/')[-1]
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            file_path = os.path.join(directory_path, file_name)
            
            print("Starting to download the orthomosaic...")
            # Make a GET request to download the orthomosaic file
            response = requests.get(ortho_url)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print("Download complete.")
                return file_path
            else:
                return "Failed to download the file."
    return "Orthomosaic data not found in the mission details."

# Example usage
api_token = 'Your_API_Token'
project_id = 'Your_Project_ID'
directory_path = 'Your_Directory_Path'

# Retrieve and download the most recent orthomosaic file
tif_path = get_recent_ortho_url(api_token, project_id, directory_path)
if "Failed" not in tif_path and not tif_path.startswith("Error"):
    print(f"Downloaded orthomosaic to: {tif_path}")
else:
    print(tif_path)  # Handle download or API errors