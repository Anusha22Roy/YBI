Step 1 : import library
import pandas as pd
# Step 2 : import data
icecream = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/Ice%20Cream.csv')
# Step 3 : define target (y) and features (X)
icecream.columns
Index(['Temperature', 'Revenue'], dtype='object')
y = icecream['Revenue']
X = icecream[['Temperature']]
# Step 4 : train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=2529)
# check shape of train and test sample
X_train.shape, X_test.shape, y_train.shape, y_test.shape
((350, 1), (150, 1), (350,), (150,))
# Step 5 : select model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
# Step 6 : train or fit model
model.fit(X_train,y_train)
LinearRegression()
model.intercept_
42.444772590839705
model.coef_
array([21.54587147])
# Step 7 : predict model
y_pred = model.predict(X_test)
y_pred
array([645.7291738 , 380.7149547 , 180.33835001, 247.13055157,
       415.18834905, 283.75853308, 372.09660611, 671.58421957,
       675.89339386, 684.51174245, 531.536055  , 613.41036659,
       361.32367037, 303.1498174 , 158.79247854, 473.36220203,
       611.25577945, 615.56495374, 512.14477068, 805.16862269,
       268.67642305, 441.04339482, 436.73422053, 861.18788852,
       531.536055  , 216.96633151, 725.44889825, 311.76816599,
       505.68100924, 466.89844059, 684.51174245, 960.29889729,
       550.92733933, 615.56495374, 367.78743182, 404.41541332,
       413.03376191, 662.96587098, 876.26999855, 544.46357788,
       811.63238414, 686.6663296 , 486.28972491, 322.54110172,
       637.11082521, 798.70486125, 438.88880767, 790.08651266,
       684.51174245, 497.06266065, 380.7149547 , 479.82596347,
       479.82596347, 563.85486221, 665.12045813, 453.9709177 ,
       688.82091675, 647.88376095, 391.48789043, 662.96587098,
       507.83559638, 309.61357884, 397.95165188, 199.72963434,
       387.17871614, 658.65669669, 441.04339482, 395.79706473,
       652.19293524, 841.7966042 , 581.09155939, 352.70532179,
       734.06724684, 350.55073464, 253.59431301, 449.66174341,
       637.11082521, 135.09201992, 594.01908227, 669.42963242,
       699.59385248, 598.32825656, 469.05302773, 912.89798005,
       697.43926533, 835.33284275, 527.22688071, 902.12504432,
       352.70532179, 423.80669764, 591.86449512, 656.50210954,
       548.77275218, 188.9566986 , 641.41999951, 641.41999951,
       572.4732108 , 486.28972491, 469.05302773, 632.80165092,
       512.14477068, 292.37688166, 729.75807254, 477.67137632,
        63.99064406, 395.79706473, 591.86449512, 469.05302773,
       568.1640365 , 602.63743086, 736.22183398, 492.75348635,
       337.62321175, 656.50210954, 423.80669764, 313.92275314,
       458.280092  , 419.49752335, 456.12550485, 559.54568791,
       522.91770641, 206.19339578, 742.68559543, 673.73880672,
       367.78743182, 690.97550389, 712.52137536, 520.76311927,
       309.61357884, 626.33788948, 803.01403555, 576.78238509,
       738.37642113, 645.7291738 , 453.9709177 , 578.93697224,
       566.00944936, 589.70990798, 447.50715626, 434.57963338,
       555.23651362, 509.99018353, 641.41999951, 475.51678917,
       441.04339482, 703.90302678, 410.87917476, 462.58926629,
       410.87917476, 305.30440455])
# Step 8 : model accuracy
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
mean_absolute_error(y_test,y_pred)
19.138687444270737
mean_absolute_percentage_error(y_test,y_pred)
0.042214848219420134
mean_squared_error(y_test,y_pred)
583.7362763558341