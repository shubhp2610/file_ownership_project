# Django File Transfer and Ownership API
This project is a Django REST API system designed to manage file ownership between users. It allows for the transfer of file ownership from one user to another and provides a mechanism for the original owner to revoke the transfer and reclaim ownership. All actions are logged for auditing purposes.

## Requirements
This project is built with Python and requires the following modules:
- `django`: The core web framework.
- `djangorestframework`: The toolkit for building the REST API.

You can install them using pip:

```
pip install django djangorestframework
```
## API Folder Overview
The core logic of the application is contained within the `api` folder.
- `models.py`: Defines the database schema. It includes the File model to store file information (including current and original owners) and the TransferHistory model to log all transfer and revoke actions.
- `serializers.py`: Contains the serializers that convert model instances to JSON (and vice-versa) and validate incoming data for the API endpoints.
- `views.py`: Holds the business logic for the API. It processes requests, interacts with the models, and returns responses for each endpoint.
- `urls.py`: Maps the API endpoints (URLs) to their corresponding views.

## API Endpoints
`All endpoints require Basic Authentication.`

### `[POST] /api/files/`
Uploads a new file. The authenticated user becomes the owner.

### `[GET] /api/files/`
Lists all files currently in the system (for admin or general view).

### `[GET] /api/my-files/`
Lists only the files currently owned by the authenticated user.

### `[POST] /api/transfer/`
Transfers ownership of a file from the current owner to another user.

### `[POST] /api/revoke/`

Allows the original owner of a file to revoke the transfer and reclaim ownership.

## Final DB snapshots
### Users
### Files
### TransferHistory