from pyspark import SparkContext
from pyspark.sql import SparkSession


def get_spark(app_name: str = "PySparkApp", master: str = "local[*]") -> tuple[SparkSession, SparkContext]:
    """Wrapper function to start Spark for local tests or cluster jobs.

    Returns
    -------
    tuple[SparkSession, SparkContext]
        Current SparkSession and SparkContext
    """
    spark = SparkSession.builder.appName(app_name).master(master).getOrCreate()
    sc = spark.sparkContext
    return spark, sc
