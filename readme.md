# Data Engineering Crash Course

This is a crash course on data engineering. It is intended to be a quick introduction to the field of data engineering. It is not intended to be comprehensive, but rather to provide a high-level overview of the field and its key concepts.

## Introduction

- What is data engineering?

Data engineering is the practice of designing, building, and maintaining systems for collecting, storing, and processing data. Data engineers are responsible for creating the infrastructure that enables data scientists and analysts to access and analyze data.

- What is the role of a data engineer?

The role of a data engineer is to build and maintain the infrastructure that enables data scientists and analysts to access and analyze data. This includes designing and building data pipelines, creating and maintaining databases, and developing tools for data processing and analysis.

- What are the key skills required to be a data engineer?

The key skills required to be a data engineer include:

- Programming: Data engineers need to be proficient in programming languages such as Python, Java, or Scala.
- Database management: Data engineers need to be familiar with database management systems such as SQL and NoSQL databases.
- Data processing: Data engineers need to be familiar with tools and frameworks for data processing such as Apache Spark, Apache Flink, and Apache Kafka.
- Cloud computing: Data engineers need to be familiar with cloud computing platforms such as Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure.

## Setting Up The Environment

We will need docker to run the environment. We will use docker-compose to run the environment.

## SQL

SQL stands for Structured Query Language. It is a standard language for accessing and manipulating databases. It is used to create and manage databases, as well as to query and update data. It is a powerful and flexible language that is widely used in the field of data engineering.

[SQL](/0_sql-crash-course/sql.md)

## Data Pipeline

A data pipeline is a series of data processing elements that are connected in sequence. The output of one element is the input of the next one. The elements of a pipeline are often executed in parallel or in time-sliced fashion.

- Extract, Transform, Load (ETL)
- Extract, Load, Transform (ELT)
- Data Ingestion
- Data Processing (Batch and Stream Processing)
- Data Storage
- Data Analysis

[Data Pipeline](1_basic-elt/data-pipeline.md)

## DBT (Data Build Tool)

DBT is a command-line tool that enables data analysts and engineers to transform data in their warehouse more effectively. It is a powerful tool for building and managing data pipelines.

[DBT](2_dbt/dbt.md)

## Apache Airflow

Apache Airflow is a platform to programmatically author, schedule, and monitor workflows. Use airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed. When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.

[Apache Airflow](3_airflow/airflow.md)
