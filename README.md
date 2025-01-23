Data Pipeline and Overview

This project leverages Hadoop and Spark to process the Iowa Liquor Sales dataset. The pipeline handles unstructured data, transforms it into a structured format, and stores it in a Spark Delta Table while ensuring data consistency and eliminating duplicates.

Pipeline Steps

1. Data Ingestion with Hadoop

Task: Reads raw, unstructured text data.
Output: Converts the data into a structured CSV format.
Storage: Writes the structured data into the Hadoop Distributed File System (HDFS).

2. Data Processing with Spark

Schema Definition:
Defines and enforces a strict schema to ensure data consistency.

Data Transformation:
Converts data types for compatibility and analysis.
Enhances the dataset by adding calculated fields or derived metrics (e.g., total sales, region-based aggregation).

Delta Table Management:
Writes the transformed data to a Spark Delta table.
Implements MERGE logic to ensure no duplicate records are inserted.

Optimizations Algorithms

1. Caching
Purpose: Speeds up repeated transformations by temporarily storing intermediate results in memory.

2. Repartitioning
Purpose: Balances data distribution across nodes for efficient processing.
Method: Reorganizes data based on key fields like date, region, or store ID to optimize queries.

2. Distinct Record Handling
Approach: Uses countDistinct and deduplication logic to eliminate redundancy and maintain dataset integrity.
