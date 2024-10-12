from pyspark.sql import SparkSession


def run_sample_job(spark: SparkSession) -> None:
    """Example Spark job."""
    data = [("Viktor", 34), ("Josh", 45), ("Flo", 29)]
    df = spark.createDataFrame(data, ["name", "age"])
    df.show()
