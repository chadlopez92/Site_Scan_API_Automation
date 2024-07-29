Overview
This Python script retrieves the URL of the most recent orthomosaic from the SiteScan API and downloads the orthomosaic file to a specified directory. The script was conceptualized and integrated by Chad Lopez, with code generation assistance from ChatGPT.

Features
Retrieve Recent Orthomosaic URL: Automatically fetches the URL of the most recent orthomosaic for a given project.
Download Orthomosaic: Downloads the orthomosaic file to a specified directory.
Requirements
Python 3.8 or higher
Required Python libraries:
bash
Copy code
pip install requests
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/chadlopez92/SiteScan_API_Orthomosaic.git
cd SiteScan_API_Orthomosaic
Install Required Libraries:

bash
Copy code
pip install requests
Configuration
Set Your Project ID and API Token: Edit the script to set your project_id, directory_path, and api_token:

python
Copy code
api_token = 'Your_API_Token'
project_id = 'Your_Project_ID'
directory_path = 'Your_Directory_Path'
Usage
Run the Script:

bash
Copy code
python get_recent_ortho_url.py
Monitor the Output:

The script will retrieve the most recent orthomosaic URL for the specified project.
It will then download the orthomosaic file to the specified directory.
Finally, it will print the file path of the downloaded orthomosaic or an error message if something goes wrong.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
This script was created with the assistance of ChatGPT, developed by OpenAI. Special thanks to OpenAI for providing the AI tools that made this project possible.

You can further customize the README as needed, including adding your contact information and any additional details relevant to your project.






