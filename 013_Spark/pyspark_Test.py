import findspark
findspark.init("/home/fieldengineer/opt/spark-2.4.4")
import random
from pyspark import SparkContext
sc = SparkContext(appName="EstimatePi")
def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1
NUM_SAMPLES = 1000
count = sc.parallelize(range(0, NUM_SAMPLES)) \
             .filter(inside).count()
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))
sc.stop()
