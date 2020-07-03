from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
from turkish.deasciifier import Deasciifier
import os

os.environ["PYSPARK_PYTHON"] = "/usr/local/bin/python3"
sc = SparkContext('local[*]')
spark = SparkSession(sc)
df = spark.read.csv('../datasets/hepsiburada_review.csv', header=True)
df.show()

__remove_digits = str.maketrans('', '', '0123456789')


def remove_digits(text):
    text = str(text)
    return text.translate(__remove_digits).strip()


def deasciify(text):
    deasci = Deasciifier(text)
    result = deasci.convert_to_turkish()
    return result


df_rem_puc = udf(lambda df: remove_digits(df), StringType())
df_deasciify = udf(lambda df: deasciify(df), StringType())

df.select('texts', df_rem_puc('texts')).show(100)
