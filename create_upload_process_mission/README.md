Automated Image Upload and Mission Processing Script
Overview
This Python script automates the creation of missions, the uploading of images, and the initiation of mission processing using the SiteScan API. The script was conceptualized and integrated by Chad Lopez, with code generation assistance from ChatGPT.

Features
Dynamic Mission Creation: Automatically creates new missions with names based on the current date and time.
Efficient Image Upload: Uploads images from a specified directory, supporting various image formats.
Mission Processing: Initiates mission processing automatically after the images are uploaded.
Requirements
Python 3.8 or higher
Required Python libraries:
requests
datetime
os
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install Required Libraries:

bash
Copy code
pip install requests
Configuration
Set Your Project ID and API Token:
Edit the script to set your project_id, directory_path, and api_token:

python
Copy code
project_id = 'Your_Project_ID'
directory_path = r'Path_to_your_Image_directory'
api_token = 'your_API_token'
Ensure Your Directory Contains Supported Image Formats:
Supported formats include: .png, .jpg, .jpeg, .tiff, .bmp, .gif.

Usage
Run the Script:

bash
Copy code
python your_script_name.py
Monitor the Output:

The script will create a new mission and print the mission ID and name.
It will then upload each image from the specified directory.
Finally, it will initiate mission processing and print the status.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
This script was created with the assistance of ChatGPT, developed by OpenAI. Special thanks to OpenAI for providing the AI tools that made this project possible.
