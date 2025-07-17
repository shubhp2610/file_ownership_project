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
- `All endpoints require Basic Authentication. Django user managment is used.`
<img width="1368" height="254" alt="image" src="https://github.com/user-attachments/assets/5b449e48-b71f-4e28-953b-2e931ff07a40" />

### `[POST] /api/files/`
- Uploads a new file. The authenticated user becomes the owner.
- Example: User `one` adding a csv file with title `My ML dataset`.
<img width="1381" height="675" alt="image" src="https://github.com/user-attachments/assets/c55868c5-560c-420b-a7ae-812b8d922465" />

### `[GET] /api/files/`
- Lists all files currently in the system (for admin or general view).
- Example: User `one` listing all files in the system.
<img width="1380" height="844" alt="image" src="https://github.com/user-attachments/assets/24a5f95e-c6bb-4c68-8770-0aba143df6a4" />

### `[GET] /api/my-files/`
- Lists only the files currently owned by the authenticated user.
- Example: User `one` listing files owned by him.
<img width="1374" height="850" alt="image" src="https://github.com/user-attachments/assets/f61d10f7-9da7-46e2-95a3-ed66e4390b51" />

### `[POST] /api/transfer/`
- Transfers ownership of a file from the current owner to another user.
- Example: User `one` transfering ownership of file with id 1 to user `two`.
<img width="1380" height="709" alt="image" src="https://github.com/user-attachments/assets/63000bce-63f5-48ec-a382-4ebf169693e1" />

### `[POST] /api/revoke/`
- Allows the original owner of a file to revoke the transfer and reclaim ownership.
- Example: User `one` revoking ownership of file with id 1.
<img width="1390" height="714" alt="image" src="https://github.com/user-attachments/assets/e80af156-8845-463c-85ee-cc09fdc371b7" />

## Final DB snapshots
### Users
### Files
### TransferHistory
