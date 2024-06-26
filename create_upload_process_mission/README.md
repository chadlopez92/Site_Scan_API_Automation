# Automated Image Upload and Mission Processing Script

## Overview

This Python script automates the creation of missions, the uploading of images, and the initiation of mission processing using the SiteScan API. The script was conceptualized and integrated by Chad Lopez, with code generation assistance from ChatGPT.

## Features

- **Dynamic Mission Creation:** Automatically creates new missions with names based on the current date and time.
- **Efficient Image Upload:** Uploads images from a specified directory, supporting various image formats.
- **Mission Processing:** Initiates mission processing automatically after the images are uploaded.

## Requirements

- Python 3.8 or higher
- Required Python libraries:
  - `requests`
  - `datetime`
  - `os`

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

