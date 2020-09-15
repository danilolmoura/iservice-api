# API documentation

## Description

IService API is a `HTTP REST` interface

## Headers

For each request, **it is necessary** to add the `Content-Type` to the application headers as shown in the example below:
```json
{
	"Content-Type": "application/json"
}
```

## The USER resource

#### CREATE

With this resoure it's possible to create a new `user`, considering the points below:

- It's not necessary to add `id` at creation.
- All fields are required, except for id
- It's not possible to create `users` with same document or same `email`

##### example

```json
POST /api/v1/user
{
	"email": "danilolmoura@gmail.com",
    "name": "Danilo da Silva",
    "document": "04.433.333/0031-44",
	"password": "123456"
}
```

In the response, the data of the newly created will be returned:
```json
HTTP Response 200
{
  "$id": 1,
  "document": "04.433.333/0031-44",
  "email": "danilolmoura@gmail.com",
  "name": "Danilo da Silva",
  "password": "123456"
}
```

Or, it will return an exception if the `document` or `email` is duplicated:
```json
HTTP Response 409
{
  "message": "Conflict",
  "status": 409
}
```

#### GET

With this resoure it's possible to get user info

##### example

```json
GET /api/v1/user/<user_id>
```

In the response, the data of the user returned:
```json
HTTP Response 200
{
  "$id": 1,
  "document": "04.433.333/0031-44",
  "email": "danilolmoura@gmail.com",
  "name": "Danilo da Silva",
  "password": "123456"
}
```

Or, it will return an exception if the `document` or `email` is duplicated:
```json
HTTP Response 404
{
  "item": {
    "$id": 2,
    "$type": "user"
  },
  "message": "Not Found",
  "status": 404
}
```

#### LIST

With this resoure it's possible to list users info

##### example

```json
GET /api/v1/user
```

```json
HTTP Response 200
[
  {
    "$id": 1,
    "document": "04.433.714/0031-44",
    "email": "danilolmoura@gmail.com",
    "name": "Danilo da Silva",
    "password": "123456"
  },
  {
    "$id": 2,
    "document": "04.433.333/0031-44",
    "email": "danilolmoura2@gmail.com",
    "name": "Danilo Moura",
    "password": "123456"
  }
]
```

Or, it will return an empty list if there are no users registered:
```json HTTP Response 200
[]
```

# References

* [Docker](https://www.docker.com/get-started)
* [Flask](http://flask.palletsprojects.com/en/1.1.x/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/en/latest/)
