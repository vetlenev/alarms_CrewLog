import os
from cognite.client import CogniteClient
from cognite.client.config import ClientConfig
from cognite.client.credentials import OAuthInteractive, OAuthClientCredentials
from cognite_authentication import set_cdf_client_connection

from dotenv import load_dotenv


def initialize_client(cdf_env: str, cache_token: bool):
    """Initialize Cognite client for provided project

    Args:
        cdf_env (str): What CDF environment to connect to
    Raises:
        Exception: No project assigned to this client

    Returns:
        CogniteClient: instantiated Cognite client
        TokenInspection: dictionary with status of client
    """
    # TENANT_ID = "3b7e4170-8348-4aa4-bfae-06a3e1867469"#"48d5043c-cf70-4c49-881c-c638f5796997"
    # CLIENT_ID = "779f2b3b-b599-401a-96aa-48bd29132a27"#"fab52bb5-9de2-4f9e-aefa-712da4b5fe00"
    load_dotenv("../authentication-ids.env")

    CLIENT_NAME = "akerbp"  # "Cognite Academy course taker"
    CDF_CLUSTER = "api"  # "westeurope-1"
    if cdf_env == "dev":
        COGNITE_PROJECT = "akerbp-dev"
    elif cdf_env == "test":
        COGNITE_PROJECT = "akerbp-test"
    elif cdf_env == "prod":
        COGNITE_PROJECT = "akerbp"
    else:
        COGNITE_PROJECT = "akerbp-sandbox"  # "ds-basics"

    SCOPES = [f"https://{CDF_CLUSTER}.cognitedata.com/.default"]

    AUTHORITY_HOST_URI = "https://login.microsoftonline.com"
    AUTHORITY_URI = AUTHORITY_HOST_URI + "/" + \
        str(os.getenv("TENANT_ID"))  # TENANT_ID
    PORT = 53000

    # creds = OAuthInteractive(client_id=CLIENT_ID, authority_url=AUTHORITY_URI, scopes=SCOPES)
    if cache_token:
        client = set_cdf_client_connection(
            client_name=CLIENT_NAME,
            project=COGNITE_PROJECT,
            client_id=str(os.getenv("CLIENT_ID")),
            tenant_id=str(os.getenv("TENANT_ID")),
        )
    else:
        creds = OAuthClientCredentials(
            token_url=AUTHORITY_URI + "/oauth2/v2.0/token",
            client_id=str(os.getenv("CLIENT_ID")),
            scopes=SCOPES,
            client_secret=str(os.getenv("CLIENT_SECRET")),
        )

        client_cnf = ClientConfig(
            client_name=CLIENT_NAME,
            base_url=f"https://{CDF_CLUSTER}.cognitedata.com",
            project=COGNITE_PROJECT,
            credentials=creds,
        )

        client = CogniteClient(client_cnf)

    status = client.iam.token.inspect()  # verify your client token and status
    # print(status)
    if "projects" not in vars(status):
        raise Exception("Token Error!")

    return client  # , status
