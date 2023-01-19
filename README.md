# Sample ETL Pipeline for Updating London Bike Dock Information

## Introduction
This project is to demonstrate a method to create a quick ETL process for collecting and storing data.
I've used a TfL API endpoint for "Boris" Bike locations as an initial data collection, the next steps
will be to use more data to collect realtime data usage and store.

## Layout
- ***oa_extract***
    : Docker Container that makes requests to TfL endpoints, parses data using datatransformer class
      and simplemysql class to save data to another mariadb Docker image.
- ***oa_datalake***
    : Docker container with MariaDB loaded to store TfL data.

Currently this is proof of concept, there is no persisted Docker storage and no automated data collection.

## How To Start Docker Images
There's a bash script to build both docker images

    bash build_docker_images.sh

If you're not on Unix, you can run

    docker build -t oa/datalake oa_datalake/
    docker build -t oa/extract oa_extract/

Then you can run the docker compose in the main directory

    docker-compose up

## How to Test
In two seperate terminals start exec into both containers

    docker exec -it sample_etl_pipeline_mariadb_1 /bin/bash
    docker exec -it sample_etl_pipeline_python_1 /bin/bash

In Python container run run.py

    python3 run.py

In MariaDB container check the core database

    mysql -u root
    SELECT * FROM Core.locations;

## Open Source Use
- Bitnami MariaDB & Python Containers https://github.com/bitnami/containers
- simplemysql package https://github.com/bitnami/containers

## Next Steps
- Add Further Functionality (multiple tables in MariaDB)
- Automate updating of data feed (Cronjobs/MariaDB events)
- Creating Reporting environment