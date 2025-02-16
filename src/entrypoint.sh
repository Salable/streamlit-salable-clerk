#!/bin/bash

# This script creates a secrets.toml file for Streamlit, using environment variables
# to populate the Snowflake connection details.

# Function to check if a required environment variable is set
check_var() {
    if [ -z "${!1}" ]; then
        echo "Error: $1 is not set. Please set all required environment variables."
        exit 1
    fi
}

# Check all required environment variables
# If any of these are not set, the script will exit with an error
echo "Checking required environment variables..."
check_var REDIRECT_URI
check_var COOKIE_SECRET
check_var CLIENT_ID
check_var CLIENT_SECRET
check_var SERVER_METADATA_URL

# If we've made it this far, all variables are set
echo "All required environment variables are set."

# Create .streamlit directory if it doesn't exist
echo "Creating .streamlit directory if it doesn't exist..."
mkdir -p .streamlit

# Create secrets.toml file with the Snowflake connection details
echo "Creating secrets.toml file..."
cat << EOF > .streamlit/secrets.toml
[auth]
redirect_uri = "${REDIRECT_URI}"
cookie_secret = "${COOKIE_SECRET}"
client_id = "${CLIENT_ID}"
client_secret = "${CLIENT_SECRET}"
server_metadata_url = "${SERVER_METADATA_URL}"
client_kwargs = { "prompt" = "login" }
EOF

# Confirm successful creation of the file
echo "secrets.toml file created successfully in .streamlit folder."

streamlit run home.py --server.port=8501 --server.address=0.0.0.0