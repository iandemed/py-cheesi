# py-cheesi

## Overview

I created the py-cheesi API using express, flask, and Beautfiul soup to scrape data on the various cheeses listed on [cheese.com](https://cheese.com/)

There are a lot of open-source APIs on wine, but I noticed that there were no APIs that covered cheese. I wanted to focus my efforts on a unique set of data that has not been covered extensively. The py-cheesi API also allows me to practice modeling many-to-many relationships in PostgreSQL.

## Table of Contents

- [Techincal Requirements](#techincal-requirements)
  - [Technologies Used](#technologies-used)
  - [Dependencies](#dependencies)
  - [Authentication](#authentication)
- [Resource List](#resource-list)
  - [Cheese](#cheese)
    - [Cheese](#cheese-1)
    - [GET by ID](#get-by-id)
  - [Milk](#milk)
    - [Milk](#milk-1)
  - [Texture](#texture)
    - [Texture](#texture-1)
    - [GET by ID](#get-by-id)
- [Additional Notes](#additional-notes)
  - [Future Expansions](#future-expansions)

## Techincal Requirements

### Technologies Used

1. Python - the language that the project and API are written in
2. PostgreSQL - the local database that houses the data scraped for the database

### Dependencies

1. peewee - to interact with the PostgreSQL database
2. psycopg2-binary - to connect with the PostgreSQL database
3. requests - to get the raw HTML
4. beautifulsoup4 - to parse through the HTML and scrape the data
5. flask - to set-up the routes to connect to my API

### Authentication

As of the most current release of this API, there is no documentation. The First Families API is a completely open API

## Resource List

![image](./cheese_db_structure.PNG)

Theere are currently currently two principal tables in the First Family API: the presidents themselves and the First Spouses.

The root directory for each collection (`/president` and `/firstSpouse` respectivley) provides a JSON containing all of the entries in the database. Below are examples of the HTTP requests that you can send into the API along with the output you may expect to recieve.

| **Route name** | **URL**           | **HTTP Verb** | **Description**                                                |
| -------------- | ----------------- | ------------- | -------------------------------------------------------------- |
| Index          | /{resource}       | GET           | Display a list of all Presidents or First Spouses              |
| Show ID        | /{resource}/{:id} | GET           | Display a specific President or First Spouse based on their ID |
| Create         | /{resource}       | POST          | Add new President or First Spouse to the database              |
| Edit By Id     | /{resource}/{:id} | PUT           | Update a particular President or First Spouse                  |
| Delete         | /{resource}/{:id} | DELETE        | Delete a particular President or First Spouse                  |

### Cheese

#### Cheese

| **Variable** | **Type**    | **Description**                                                                         |
| ------------ | ----------- | --------------------------------------------------------------------------------------- |
| `id`         | Primary Key | Key to the Milk collection, corresponds to the alphanumeric order of all of the cheeses |
| `rind`       | String      | type of rind (or casing) of the cheese                                                  |
| `colour`     | String      | Array of references to the president's previous partners                                |
| `vegetarian` | String      | Whether the cheese is vegetarian or not (the default is True)                           |

#### GET by ID

```JSON
{
    "colour": "yellow",
    "id": 1,
    "name": "abbaye de belloc ",
    "rind": "natural",
    "vegetarian": true
}
```

### Milk

#### Milk

| **Variable** | **Type**    | **Description**                                                               |
| ------------ | ----------- | ----------------------------------------------------------------------------- |
| `id`         | Primary Key | Key to the Milk collection, corresponds to the first time each milk is listed |
| `cheese_id`  | Foreign Key | Foreign Key to the Cheese table                                               |
| `milk`       | String      | The type of milk used to create each cheese                                   |

### Texture

#### Texture

| **Variable** | **Type**    | **Description**                                                                     |
| ------------ | ----------- | ----------------------------------------------------------------------------------- |
| `id`         | Primary Key | Key to the Texture collection, corresponds to the first time each texture is listed |
| `cheese_id`  | Foreign Key | Foreign Key to the Cheese table                                                     |
| `texture`    | String      | The type of texture used to create each cheese                                      |

#### GET by ID

```JSON
 {
        "cheese_id": {
            "colour": "yellow",
            "id": 1,
            "name": "abbaye de belloc ",
            "rind": "natural",
            "vegetarian": true
        },
        "id": 1,
        "texture": "creamy"
    }
```

## Additional Notes

### Future Expansions

1. Deploy the API remotely to Heroku
2. Refactor the code to periodically scrape the web-page for additonal cheeses and to prevent rescraping the data on load-up
3. Incorperate more characteristics of the cheese
