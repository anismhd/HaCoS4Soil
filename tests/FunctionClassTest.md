# Test of Function Class

## Testing of ContinuousPolynomialFunction Class

### Linear Function y=mx+c

		Consider m = 2, c = 5		Function usage, Fun1 = ContinuousPolynomialFunction(C=[5,2])

|NO |X value   |Y value   |Cmptd Y   |
| - | -------  | -------  | ------   |
|  1|   -1.0000|    3.0000|    3.0000|
|  2|    0.0000|    5.0000|    5.0000|
|  3|    1.0000|    7.0000|    7.0000|
|  4|    2.0000|    9.0000|    9.0000|
|  5|    3.0000|   11.0000|   11.0000|
|  6|    4.0000|   13.0000|   13.0000|

[Test 1](./tests/ContinuousPolynomialFunction_TF1.png)

### Bi-Linear Function 

	y = 2x if x<= 1, otherwise = x + 1
		Fun2 = PiecewiseContinousPolynomialFunction(num_pieces=2, limits=[1],C1=[0,2],C2=[1,1])

|NO |X value   |Y value   |Cmptd Y   |
| - | -------  | -------  | ------   |
|  1|   -1.0000|   -2.0000|   -2.0000|
|  2|    0.0000|    0.0000|    0.0000|
|  3|    1.0000|    2.0000|    2.0000|
|  4|    2.0000|    3.0000|    3.0000|
|  5|    3.0000|    4.0000|    4.0000|
|  6|    4.0000|    5.0000|    5.0000|

[Test 2](./tests/ContinuousPolynomialFunction_TF2.png)

### Tri-Linear Function 

		Fun3 = PiecewiseContinousPolynomialFunction(num_pieces=3, limits=[2,3],C1=[0,0.5],C2=[-1,1],C3=[8,-3])

|NO |X value   |Y value   |Cmptd Y   |
| - | -------  | -------  | ------   |
|  1|   -1.0000|   -0.5000|   -0.5000|
|  2|    0.0000|    0.0000|    0.0000|
|  3|    1.0000|    0.5000|    0.5000|
|  4|    2.0000|    1.0000|    1.0000|
|  5|    3.0000|    2.0000|    2.0000|
|  6|    4.0000|    0.0000|    0.0000|

[Test 2](./tests/ContinuousPolynomialFunction_TF3.png)

### Linear-Quadratic Function		Fun4 = PiecewiseContinousPolynomialFunction(num_pieces=2, limits=[1],C1=[0,1.0],C2=[3,-1,-1])

|NO |X value   |Y value   |Cmptd Y   |
| - | -------  | -------  | ------   |
|  1|   -1.0000|   -1.0000|   -1.0000|
|  2|    0.0000|    0.0000|    0.0000|
|  3|    1.0000|    1.0000|    1.0000|
|  4|    2.0000|   -3.0000|   -3.0000|
|  5|    3.0000|   -9.0000|   -9.0000|
|  6|    4.0000|  -17.0000|  -17.0000|

[Test 2](./tests/ContinuousPolynomialFunction_TF4.png)

