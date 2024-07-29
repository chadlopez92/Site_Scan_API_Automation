# Retrieve and Download Recent Orthomosaic

## Overview

This Python script retrieves the URL of the most recent orthomosaic from the SiteScan API and downloads the orthomosaic file to a specified directory. The script was conceptualized and integrated by Chad Lopez, with code generation assistance from ChatGPT.

## Features

- **Retrieve Recent Orhtomoasic URL** Automatically fetches the URL of the most recent orthomosaic for a given project.
- **Download Orthomosaic** Downloads the orthomosaic file to a specified directory.

## Requirements

- Python 3.8 or higher
- Required Python libraries:
    ```bash
    pip install requests
    ```

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/chadlopez92/Site_Scan_API_Automation.git
    cd Site_Scan_API_Automation
    ```

2. **Install Required Libraries:**
    ```bash
    pip install requests
    ```

## Configuration

1. **Set Your Project ID and API Token:**
    Edit the script to set your `project_id`, `directory_path`, and `api_token`:
    ```python
    api_token = 'Your_API_Token'
    project_id = 'Your_Project_ID'
    directory_path = 'Your_Directory_Path'
    ```

## Usage

1. **Run the Script:**
    ```bash
    python Create_Mission_Upload_Images_Process_Mission.py
    ```

2. **Monitor the Output:**
   -The script will retrieve the most recent orthomosaic URL for the specified project.
   -It will then download the orthomosaic file to the specified directory.


## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/chadlopez92/Site_Scan_API_Automation/blob/main/LICENSE) file for details.

## Acknowledgements

This script was created with the assistance of ChatGPT, developed by OpenAI. Special thanks to OpenAI for providing the AI tools that made this project possible.


