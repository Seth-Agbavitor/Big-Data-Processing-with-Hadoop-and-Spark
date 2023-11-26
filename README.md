Iowa Liquor Sales Data Pipeline

Overview

This project uses Hadoop and Spark to process the Iowa Liquor Sales dataset. It involves reading unstructured data, converting it to structured format, and storing it in a Spark Delta table without duplicates.

Pipeline steps:

1. Hadoop: Reads and converts unstructured text data to structured CSV format, stored in HDFS.

2. Spark:
   
Defines and enforces data schema.

Transforms data types and enhances the dataset.

Updates the Delta table ensuring no duplicates.

Optimizations:

Caching: Improves processing speed.

Repartitioning: Optimizes data distribution.

countDistinct: Ensures data uniqueness.



