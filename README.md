# Big Data Processing Using Hadoop and Spark
In this project, we implemented the following pipelines using Iowa Liquor Sale Dataset:
The pipeline reads unstructured data (e.g.: text in txt files), structures the data, processes the 
dataset and store the results into a Spark Delta table. 
When reruning the pipeline on another file, the pipeline shall update the existing Delta table. 
The resulting table cannot have duplicate records (e.g.: rows must be unique)

Pipeline steps:
Hadoop reads unstructured data from a text dataset
• Hadoop converts the unstructured data into a structured dataset.
• Hadoop saves the structured dataset into csv format in the HDFS.
• Spark create data schema and enforce schema. 
• Spark read the csv files into Spark dataframe.
• Spark transform text variables to proper types (timestamp, double, integer, etc)
• Spark implement algorithm to enhance the dataset
• Spark update the results in the Delta table and make sure that there are no duplicates.

We implemented the following Spark optimizations:
1. Caching
2. Repartitioning
3. Using countDistinct function
