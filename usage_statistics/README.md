# Retrieve SiteScan Usage Statistics by Date

## Overview

This Python script retrieves usage statistics from the SiteScan API, including the total number of photos, bytes, pixels, and the number of days within a specified date range. The script was conceptualized and integrated by Chad Lopez, with code generation assistance from ChatGPT.

## Features

- **Retrieve Usage Statistics**: Fetches usage statistics for an organization from the SiteScan API.
- **Date Range Filtering**: Supports filtering statistics by a specified start and end date.
- **Grouping Options**: Optionally group statistics by project or user.

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
    cd SiteScan_API_Usage_Statistics
    ```

2. **Install Required Libraries:**
    ```bash
    pip install requests
    ```

## Configuration

1. **Set Your Organization ID, API Token, and Date Range:**
    Edit the script to set your `organization_id`, `api_token`, `start_date`, and `end_date`:
    ```python
    api_token = "Your_API_Token"
    organization_id = "Your_Organization_ID"
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    group_by = "project"  # or "user" for grouping by user
    ```

## Usage

1. **Run the Script:**
    ```bash
    python get_usage_statistics.py
    ```

2. **Monitor the Output:**
   - The script will retrieve usage statistics for the specified organization and date range.
   - It will print the aggregated usage statistics, including the total number of photos, bytes (and in gigabytes), pixels, and the number of days.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/chadlopez92/SiteScan_API_Usage_Statistics/blob/main/LICENSE) file for details.

## Acknowledgements

This script was created with the assistance of ChatGPT, developed by OpenAI. Special thanks to OpenAI for providing the AI tools that made this project possible.
