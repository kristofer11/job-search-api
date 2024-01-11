# Job Application API

## Overview
The overall idea of this application is for the user to be able to track job applications they have submitted. It is built with Flask and connects to a PostgreSQL database with SQLAlchemy.

## Endpoint Paths, Methods and Parameters
## API Reference

This API allows you to manage users, applications, and companies.

| Endpoint                       | HTTP Method | Description                                       | Parameters                          |
|--------------------------------|--------------|---------------------------------------------------|-----------------------------------|
| `/users`                       | GET         | Retrieve a list of all users                       |                              |
| `/users/<int:id>`              | GET         | Retrieve a specific user by ID                     | `id` (integer, required)       |
| `/users`                       | POST        | Create a new user                                  | `username` (string, required), `password` (string, required), `email` (string, required) |
| `/users/<int:id>`              | PUT         | Update an existing user                            | `id` (integer, required), `username` (string, optional), `password` (string, optional), `email` (string, optional) |
| `/users/<int:id>`              | DELETE      | Delete a user                                      | `id` (integer, required)       |
| `/applications`               | GET         | Retrieve a list of all applications                |                              |
| `/applications/<int:id>`       | GET         | Retrieve a specific application by ID               | `id` (integer, required)       |
| `/applications`               | POST        | Create a new application                           | `user_id` (integer, required), `position` (string, required), `notes` (string, optional), `created_at` (string, optional, ISO 8601 format) |
| `/applications/<int:id>`       | PUT         | Update an existing application                     | `id` (integer, required), `position` (string, optional), `notes` (string, optional), `company_id` (integer, optional) |
| `/applications/<int:id>`       | DELETE      | Delete an application                              | `id` (integer, required)       |
| `/companies`                   | GET         | Retrieve a list of all companies                   |                              |
| `/companies/<int:id>`          | GET         | Retrieve a specific company by ID                  | `id` (integer, required)       |
| `/companies`                   | POST        | Create a new company                               | `company_name` (string, required), `notes` (string, optional), `contact_name` (string, optional), `contact_email` (string, optional) |
| `/companies/<int:id>`          | PUT         | Update an existing company                         | `id` (integer, required), `company_name` (string, optional), `notes` (string, optional), `contact_name` (string, optional), `contact_email` (string, optional) |
| `/companies/<int:id>`          | DELETE      | Delete a company                                   | `id` (integer, required)       |

**Additional notes:**

* All responses are returned in JSON format.
* Authentication is not currently implemented.
* Error handling follows standard HTTP response codes.

Feel free to further customize this table with additional information or adjust the format to your liking.

I hope this is what you were looking for!



