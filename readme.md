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
<img width="835" height="500" alt="image" src="https://github.com/user-attachments/assets/f6eb7d65-0e6a-4333-a918-6d6b8c1b26ca" />
- Similarly user `two` adding a pdf file with title `My Report`.

### `[GET] /api/files/`
- Lists all files currently in the system (for admin or general view).
- Example: User `one` listing all files in the system.
<img width="845" height="567" alt="image" src="https://github.com/user-attachments/assets/9479fb38-3e4c-4115-aefa-a071d6348821" />

### `[GET] /api/my-files/`
- Lists only the files currently owned by the authenticated user.
- Example: User `one` listing files owned by him.
<img width="841" height="499" alt="image" src="https://github.com/user-attachments/assets/d5566ba4-3a26-4327-900c-b77e17fd9984" />

### `[POST] /api/transfer/`
- Transfers ownership of a file from the current owner to another user.
- Example: User `one` transfering ownership of file with id 4 to user `two` with user_id 3.
<img width="857" height="399" alt="image" src="https://github.com/user-attachments/assets/b9122905-6dc5-4676-91c7-8ed07d2ce0ff" />

- On same request it will throw error as user `one` is no longer the owner, `one` can only revoke the access.
<img width="842" height="411" alt="image" src="https://github.com/user-attachments/assets/1dcba026-651c-4663-bf2e-80347e232e2c" />

### `[POST] /api/revoke/`
- Allows the original owner of a file to revoke the transfer and reclaim ownership.
- Example: User `one` revoking ownership of file with id 4.
<img width="838" height="400" alt="image" src="https://github.com/user-attachments/assets/5a500ec5-d9ac-41d7-884e-7527a783591d" />

### Errors handeled
- **Authentication Errors:** User is not logged in.
- **Permission Errors:**
  - Trying to transfer a file you don't own.
  - Trying to revoke a file you didn't create.
- **Input Validation Errors:**
  - The `file_id` does not exist.
  - The `to_user_id` does not exist.
- **State Errors:**
  - Trying to transfer a file to its current owner.
  - Trying to revoke a file that's already been returned.
## Final DB snapshots
### Users
<img width="1158" height="439" alt="image" src="https://github.com/user-attachments/assets/aab9744a-1885-42e6-bf21-e2e75d5d762c" />

### Files
<img width="815" height="141" alt="image" src="https://github.com/user-attachments/assets/abd8a2be-baae-4c72-bf33-24c4b6ec72bd" />

### TransferHistory
<img width="758" height="151" alt="image" src="https://github.com/user-attachments/assets/4f0e3719-3449-458b-96ac-c2a6bec41be8" />

