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
    git clone https://github.com/chadlopez92/Site_Scan_API_Automation.git
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

