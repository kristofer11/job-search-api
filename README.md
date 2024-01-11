# Job Application API

## Overview
The overall idea of this application is for the user to be able to track job applications they have submitted. It is built with Flask and connects to a PostgreSQL database with SQLAlchemy.

## Endpoint Paths, Methods and Parameters

| Endpoint                       | HTTP Method | Description                                       | Parameters                          |
|--------------------------------|--------------|---------------------------------------------------|-----------------------------------|
| `/users`                       | GET         | Retrieve a list of all users                       |                              |
| `/users/<int:id>`              | GET         | Retrieve a specific user by ID                     | `id` (integer, required)       |
| `/users`                       | POST        | Create a new user                                  | `username` (string, required), `password` (string, required), `email` (string, required) |
| `/users/<int:id>`              | PUT         | Update an existing user                            | `id` (integer, required), `username` (string, optional), `password` (string, optional), `email` (string, optional) |
| `/users/<int:id>`              | DELETE      | Delete a user                                      | `id` (integer, required)       |
| `/applications`               | GET         | Retrieve a list of all applications                |                              |
| `/applications/<int:id>`       | GET         | Retrieve a specific application by ID               | `id` (integer, required)       |
| `/applications`               | POST        | Create a new application                           | `user_id` (integer, required), `position` (string, required), `notes` (string, optional), `created_at` (string, required, ISO 8601 format) |
| `/applications/<int:id>`       | PUT         | Update an existing application                     | `id` (integer, required), `position` (string, optional), `notes` (string, optional), `company_id` (integer, optional) |
| `/applications/<int:id>`       | DELETE      | Delete an application                              | `id` (integer, required)       |
| `/companies`                   | GET         | Retrieve a list of all companies                   |                              |
| `/companies/<int:id>`          | GET         | Retrieve a specific company by ID                  | `id` (integer, required)       |
| `/companies`                   | POST        | Create a new company                               | `company_name` (string, required), `notes` (string, optional), `contact_name` (string, optional), `contact_email` (string, optional) |
| `/companies/<int:id>`          | PUT         | Update an existing company                         | `id` (integer, required), `company_name` (string, optional), `notes` (string, optional), `contact_name` (string, optional), `contact_email` (string, optional) |
| `/companies/<int:id>`          | DELETE      | Delete a company                                   | `id` (integer, required)       |

## Retrospective
1. Over time I simplified the project to make sure it was doable. In hindsight I could have made it a little more complex because once I was on a roll building out the endpoints it would have been easy to add other features that I originally wanted.
2. I chose to use an ORM because I like coding in Python more than raw SQL. Even though it is an abstraction of the SQL queries that are being made, it feels more natural to me.
3. In the future I will build a frontend that uses this API. There is a lot that needs to be amended before that is a possibility such as: tables that store other kinds of inquiries besides applications, validation and authentication. 



