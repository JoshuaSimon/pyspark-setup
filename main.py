from utils import get_spark
from jobs.sample_job import run_sample_job


def main() -> None:
    """Main function to run Spark jobs."""
    spark, sc = get_spark()
    run_sample_job(spark)


if __name__ == "__main__":
    main()
    