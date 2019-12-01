# timeoff_backend

## Getting started

1.  `virtualenv myenv --python=python3`
2.  `. myenv/bin/activate`
3.  `pip install -r requirements.txt`
4.  `./manage.py migrate`
5.  `./manage.py runserver`

Endpoints:
------

All protected reuqest are marked with __authentication required__ - pass Authorization: "Bearer <access_token>" with a valid access_token.

### Authentication:

`POST /api/auth/token`

Generates new pair of access & refresh tokens.

Example request body:

```
{
  "email": "user@example.com",
  "password: "password"
}
```

No authentication required
Required fields: `email`, `password`

Returns __auth payload__
```
{
  "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
  "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}
```

`access` is a short-lived token, once it expires use `refresh` token to obtain another access token


`POST /api/auth/token/refresh`

Generates new short-lived access token.

Example request body:

```
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}
```

Required fields: `refresh`

Returns __new access token__
```
{"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNTY3LCJqdGkiOiJjNzE4ZTVkNjgzZWQ0NTQyYTU0NWJkM2VmMGI0ZGQ0ZSJ9.ekxRxgb9OKmHkfy-zs1Ro_xs1eMLXiR17dIDBVxeT-w"}
```


`POST /api/auth/forgot-password/`

Sends an email with reset password link to the user.

Example request body:
```
{
  "email": "user@example.com"
}
```


Required fields: `email`

Returns __204 NO_CONTENT__


`POST /api/auth/reset-password/`

Resets user password.

Example request body:
```
{
  "reset_token": "en1rZSJ4Wo21SCJh2VWTvdGtR0TkIFdj",
  "password": "new_password123",
  "confirm_password": "new_password123"
}
```

Returns __204 NO_CONTENT__

Required fields: `reset_token`, `password`, `confirm_password`

Returns __204 NO_CONTENT__


### Leave Requests


## LeaveRequest
```
{
    "id": 1,
    "start": "2019-12-02T10:00:00.000Z",
    "end": "2019-12-03T19:00:00.000Z",
    "description": "",
    "type": "VACATION",
    "status": "PENDING"
}
```

`GET /api/leave-requests/`

__authentication required__

List of leave requests for user


`GET /api/leave-requests/<id>`

__authentication required__

Retrieves leave request instance


`POST /api/leave-requests/`

__authentication required__

Creates a new Leave Request


`PUT /api/leave-requests/<id>`

__authentication required__

Updates a Leave Request


`DELETE /api/leave-requests/<id>`

__authentication required__

Deletes a Leave Request