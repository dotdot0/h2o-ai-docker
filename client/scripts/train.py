import h2o
import time

time.sleep(10)

h2o.init(ip="server", port=54321)

iris = h2o.import_file("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
summary = iris.describe()
print(summary)

model = h2o.estimators.H2ORandomForestEstimator()
model.train(x=list(range(0, 4)), y=4, training_frame=iris)

print(model)