import requests

def get_usage_statistics(api_token, organization_id, start_date=None, end_date=None, group_by=None):
    # Site Scan API endpoint for aggregate usage statistics
    url = f"https://sitescan-api.arcgis.com/api/v2/organizations/{organization_id}/usage/photos"

    # Set up the headers with the API token
    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    # Set up parameters
    params = {}
    if start_date:
        params['start'] = start_date
    if end_date:
        params['end'] = end_date
    if group_by:
        params['by'] = group_by

    # Make the request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON (it's a list)
        usage_statistics_list = response.json()

        # Calculate aggregated usage statistics
        total_photos = 0
        total_bytes = 0
        total_pixels = 0
        total_ndays = 0

        for usage_statistics in usage_statistics_list:
            total_photos += usage_statistics.get('photos', 0)
            total_bytes += usage_statistics.get('bytes', 0)
            total_pixels += usage_statistics.get('pixels', 0)
            total_ndays += usage_statistics.get('ndays', 0)

        # Return the aggregated usage statistics as a dictionary
        return {
            "total_photos": total_photos,
            "total_bytes": total_bytes,
            "total_pixels": total_pixels,
            "total_ndays": total_ndays
        }
    else:
        # If the request fails, print an error message and return None
        print(f"Failed to retrieve usage statistics. Status Code: {response.status_code}")
        print(response.text)  # Print the response text for debugging purposes
        return None

# Enter Credentials and desired start and end date:
api_token = "Your_API_Token"
organization_id = "Your_Organization_ID"
start_date = "2023-01-01"
end_date = "2023-12-31"
group_by = "project"  # or "user" for grouping by user

# Call the function and save the result as a variable
usage_statistics_result = get_usage_statistics(api_token, organization_id, start_date, end_date, group_by)

# Check if the result is not None before using the values
if usage_statistics_result:
    total_photos = usage_statistics_result["total_photos"]
    total_bytes = usage_statistics_result["total_bytes"]
    total_pixels = usage_statistics_result["total_pixels"]
    total_ndays = usage_statistics_result["total_ndays"]
    total_gigabytes = total_bytes / (1024 ** 3)

    # Print the aggregated usage statistics
    print("Aggregated Usage Statistics:")
    print(f"Total Photos: {total_photos}")
    print(f"Total Bytes: {total_bytes}")
    print(f"Total Gigabytes: {total_gigabytes}")
    print(f"Total Pixels: {total_pixels}")
    print(f"Total Number of Days: {total_ndays}")