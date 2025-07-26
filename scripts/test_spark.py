import pyspark

spark = pyspark.sql.SparkSession.builder.getOrCreate()
sc = spark.sparkContext
print(sc._jvm.org.apache.hadoop.util.VersionInfo.getVersion())
