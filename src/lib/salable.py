import os
import requests

BASE_URL = "https://api.salable.app"

# Retrieve credentials from environment variables
API_KEY = os.environ.get("SALABLE_API_KEY")
PRODUCT_UUID = os.environ.get("SALABLE_PRODUCT_UUID")
PLAN_UUID = os.environ.get("SALABLE_PLAN_UUID")
SUCCESS_URL = os.environ.get("SALABLE_SUCCESS_URL")

if not API_KEY or not PRODUCT_UUID or not PLAN_UUID or not SUCCESS_URL:
    raise EnvironmentError(
        "One or more required environment variables are missing: SALABLE_API_KEY, SALABLE_PRODUCT_UUID, SALABLE_PLAN_UUID, SUCCESS_URL"
    )

# Common headers for all requests
HEADERS = {
    "x-api-key": API_KEY,
    "version": "v2"
}

def check_license(license_uuid: str) -> dict:
    """
    Checks the status of a license.
    
    Endpoint: GET /licenses/{licenseUuid}
    """
    url = f"{BASE_URL}/licenses/{license_uuid}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_checkout_link(grantee_id: str) -> dict:
    """
    Initiates a purchase using Salable's pricing table session.
    
    Endpoint: GET /plans/{planUuid}/checkoutlink
    Payload includes the product and plan identifiers.
    """
    url = f"{BASE_URL}/plans/{PLAN_UUID}/checkoutlink?successUrl={SUCCESS_URL}&cancelUrl={SUCCESS_URL}&granteeId={grantee_id}&member={grantee_id}"

    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_subscription_status() -> dict:
    """
    Retrieves the current user's subscription status.
    
    Endpoint: GET /subscriptions/current
    """
    url = f"{BASE_URL}/subscriptions/current"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_licenses_for_grantee(grantee_id: str) -> dict:
    """
    Checks the license(s) associated with the grantee_id.
    
    Endpoint: GET /licenses
    Query Parameter:
      grantee_id - the ID of the current user
    """
    url = f"{BASE_URL}/licenses/granteeId/{grantee_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_capabilities_for_grantee(grantee_id: str) -> dict:
    """
    Retrieves the current capabilities that a grantee has for the current product.

    Endpoint: GET /licenses/check
    Query Parameter:
      granteeId - the unique identifier for the grantee.
    """
    url = f"{BASE_URL}/licenses/check?granteeIds={grantee_id}&productUuid={PRODUCT_UUID}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()["capabilities"]
    else:
        return []

if __name__ == "__main__":
    # For testing purposes only. This block will not run when imported as a library.
    try:
        print("Checking License:")
        print(check_license("example-license-uuid"))
    except Exception as e:
        print("Error checking license:", e)

    try:
        print("Initiating Purchase:")
        print(get_checkout_link())
    except Exception as e:
        print("Error initiating purchase:", e)

    try:
        print("Fetching Subscription Status:")
        print(get_subscription_status())
    except Exception as e:
        print("Error fetching subscription status:", e)

    try:
        print("Fetching Capabilities for Grantee:")
        # Replace 'example-grantee-id' with an actual grantee identifier when testing
        print(get_capabilities_for_grantee("example-grantee-id"))
    except Exception as e:
        print("Error fetching capabilities:", e)