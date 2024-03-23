import functions_framework
import requests


@functions_framework.http
def users(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    endpoint = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(endpoint)

    if response.status_code == 200:
        return response.content
    else:
        return "Failed to retrieve data from endpoint: " + endpoint + ". Status code: " + str(response.status_code)
