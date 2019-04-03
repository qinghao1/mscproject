# Default (Logistic Regression)

## With PoS, Sentiment
### -i
```
Confusion matrix:
=================
             for  against  observing
for        219.0      5.0       22.0
against     15.0     64.0       12.0
observing   70.0     12.0      105.0

Measures:
=========
accuracy: 0.7405

Per class:
           accuracy precision    recall        F1
for         0.78626  0.720395  0.890244  0.796364
against    0.916031  0.790123  0.703297  0.744186
observing  0.778626  0.755396  0.561497  0.644172
         accuracy-cv  accuracy-test
Q           0.519765       0.503817
BoW         0.706586       0.698473
W2V         0.706586       0.698473
PPDB        0.707980       0.715649
RootDep     0.734463       0.734733
NegAlgn     0.735516       0.734733
SVO         0.735894       0.734733
PoS         0.736080       0.736641
Sent        0.732952       0.740458
```

### Ablation
```
>> Training classifier <<

CV score: :0.732952
Test score: :0.740458
Ablating: ['Q']
Ablated feature set:['BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent']
>> Training classifier <<

Ablated CV score: 0.7211039486233365
Ablated test score: 0.7213740458015268
Ablating: ['BoW']
Ablated feature set:['Q', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent']
>> Training classifier <<

Ablated CV score: 0.7185801902279352
Ablated test score: 0.683206106870229
Ablating: ['W2V']
Ablated feature set:['Q', 'BoW', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent']
>> Training classifier <<

Ablated CV score: 0.7329515722195468
Ablated test score: 0.7442748091603053
Ablating: ['PPDB']
Ablated feature set:['Q', 'BoW', 'W2V', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent']
>> Training classifier <<

Ablated CV score: 0.7321378752953389
Ablated test score: 0.7213740458015268
Ablating: ['RootDep']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'NegAlgn', 'SVO', 'PoS', 'Sent']
>> Training classifier <<

Ablated CV score: 0.7118924054028202
Ablated test score: 0.7022900763358778
Ablating: ['NegAlgn']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'SVO', 'PoS', 'Sent']
>> Training classifier <<

Ablated CV score: 0.7331222348902094
Ablated test score: 0.7404580152671756
Ablating: ['SVO']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'PoS', 'Sent']
>> Training classifier <<

Ablated CV score: 0.7329515722195468
Ablated test score: 0.7404580152671756
Ablating: ['PoS']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'Sent']
>> Training classifier <<

Ablated CV score: 0.7325148909968393
Ablated test score: 0.7404580152671756
Ablating: ['Sent']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS']
>> Training classifier <<

Ablated CV score: 0.7360797393437981
Ablated test score: 0.7366412213740458

              accuracy-cv  accuracy-test
-['Q']           1.184762       1.908397
-['BoW']         1.437138       5.725191
-['W2V']         0.000000      -0.381679
-['PPDB']        0.081370       1.908397
-['RootDep']     2.105917       3.816794
-['NegAlgn']    -0.017066       0.000000
-['SVO']         0.000000       0.000000
-['PoS']         0.043668       0.000000
-['Sent']       -0.312817       0.381679
```
## With base
### -i
```
Confusion matrix:
=================
             for  against  observing
for        216.0      4.0       26.0
against     14.0     64.0       13.0
observing   72.0     10.0      105.0

Measures:
=========
accuracy: 0.7347

Per class:
           accuracy precision    recall        F1
for        0.778626  0.715232  0.878049  0.788321
against    0.921756  0.820513  0.703297  0.757396
observing  0.769084  0.729167  0.561497  0.634441
         accuracy-cv  accuracy-test
Q           0.519765       0.503817
BoW         0.706586       0.698473
W2V         0.706586       0.698473
PPDB        0.707980       0.715649
RootDep     0.734463       0.734733
NegAlgn     0.735516       0.734733
SVO         0.735894       0.734733
```
### ablation
```
>> Training classifier <<

CV score: :0.735894
Test score: :0.734733
Ablating: ['Q']
Ablated feature set:['BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO']
>> Training classifier <<

Ablated CV score: 0.7170656646890475
Ablated test score: 0.7213740458015268
Ablating: ['BoW']
Ablated feature set:['Q', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO']
>> Training classifier <<

Ablated CV score: 0.7181426913275086
Ablated test score: 0.6812977099236641
Ablating: ['W2V']
Ablated feature set:['Q', 'BoW', 'PPDB', 'RootDep', 'NegAlgn', 'SVO']
>> Training classifier <<

Ablated CV score: 0.7353441049217231
Ablated test score: 0.7347328244274809
Ablating: ['PPDB']
Ablated feature set:['Q', 'BoW', 'W2V', 'RootDep', 'NegAlgn', 'SVO']
>> Training classifier <<

Ablated CV score: 0.728041845175247
Ablated test score: 0.7175572519083969
Ablating: ['RootDep']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'NegAlgn', 'SVO']
>> Training classifier <<

Ablated CV score: 0.7104122712138394
Ablated test score: 0.7099236641221374
Ablating: ['NegAlgn']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'SVO']
>> Training classifier <<

Ablated CV score: 0.7348405190635844
Ablated test score: 0.7347328244274809
Ablating: ['SVO']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn']
>> Training classifier <<

Ablated CV score: 0.7355161969806077
Ablated test score: 0.7347328244274809
              accuracy-cv  accuracy-test
-['Q']           1.882789       1.335878
-['BoW']         1.775086       5.343511
-['W2V']         0.054945       0.000000
-['PPDB']        0.785171       1.717557
-['RootDep']     2.548128       2.480916
-['NegAlgn']     0.105304       0.000000
-['SVO']         0.037736       0.000000
```



# Random Forest

```
RandomForestClassifier(n_estimators=20, random_state=0
```

## With new features

### -i

```
Confusion matrix:
=================
             for  against  observing
for        217.0      2.0       27.0
against     21.0     59.0       11.0
observing   93.0      6.0       88.0

Measures:
=========
accuracy: 0.6947

Per class:
           accuracy precision    recall        F1
for        0.727099  0.655589  0.882114  0.752166
against    0.923664  0.880597  0.648352  0.746835
observing   0.73855  0.698413  0.470588    0.5623
            accuracy-cv  accuracy-test
Q              0.519765       0.503817
BoW            0.691460       0.687023
W2V            0.680286       0.679389
PPDB           0.686665       0.700382
RootDep        0.731372       0.723282
NegAlgn        0.729582       0.744275
SVO            0.748426       0.742366
PoS            0.718072       0.727099
Sent           0.718360       0.711832
AvgWordLen     0.719035       0.704198
LenRatio       0.718119       0.694656
Perc           0.717299       0.694656
```



### -a

```
>> Training classifier <<

CV score: :0.717299
Test score: :0.694656
Ablating: ['Q']
Ablated feature set:['BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent', 'AvgWordLen', 'LenRatio', 'Perc']
>> Training classifier <<

Ablated CV score: 0.7053722442929591
Ablated test score: 0.683206106870229
Ablating: ['BoW']
Ablated feature set:['Q', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent', 'AvgWordLen', 'LenRatio', 'Perc']
>> Training classifier <<

Ablated CV score: 0.6961320314645436
Ablated test score: 0.6793893129770993
Ablating: ['W2V']
Ablated feature set:['Q', 'BoW', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent', 'AvgWordLen', 'LenRatio', 'Perc']
>> Training classifier <<

Ablated CV score: 0.7115668048100802
Ablated test score: 0.700381679389313
Ablating: ['PPDB']
Ablated feature set:['Q', 'BoW', 'W2V', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent', 'AvgWordLen', 'LenRatio', 'Perc']
>> Training classifier <<

Ablated CV score: 0.7141502006642162
Ablated test score: 0.700381679389313
Ablating: ['RootDep']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'NegAlgn', 'SVO', 'PoS', 'Sent', 'AvgWordLen', 'LenRatio', 'Perc']
>> Training classifier <<

Ablated CV score: 0.6500147189426553
Ablated test score: 0.6793893129770993
Ablating: ['NegAlgn']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'SVO', 'PoS', 'Sent', 'AvgWordLen', 'LenRatio', 'Perc']
>> Training classifier <<

Ablated CV score: 0.7163324844810608
Ablated test score: 0.7080152671755725
Ablating: ['SVO']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'PoS', 'Sent', 'AvgWordLen', 'LenRatio', 'Perc']
>> Training classifier <<

Ablated CV score: 0.7262281752604963
Ablated test score: 0.6984732824427481
Ablating: ['PoS']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'Sent', 'AvgWordLen', 'LenRatio', 'Perc']
>> Training classifier <<

Ablated CV score: 0.7308563138461792
Ablated test score: 0.7270992366412213
Ablating: ['Sent']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'AvgWordLen', 'LenRatio', 'Perc']
>> Training classifier <<

Ablated CV score: 0.7254126072662327
Ablated test score: 0.7022900763358778
Ablating: ['AvgWordLen']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent', 'LenRatio', 'Perc']
>> Training classifier <<

Ablated CV score: 0.7189154136908354
Ablated test score: 0.7061068702290076
Ablating: ['LenRatio']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent', 'AvgWordLen', 'Perc']
>> Training classifier <<

Ablated CV score: 0.719565095281175
Ablated test score: 0.700381679389313
Ablating: ['Perc']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO', 'PoS', 'Sent', 'AvgWordLen', 'LenRatio']
>> Training classifier <<

Ablated CV score: 0.718118931549516
Ablated test score: 0.6946564885496184
                 accuracy-cv  accuracy-test
-['Q']              1.192703       1.145038
-['BoW']            2.116725       1.526718
-['W2V']            0.573247      -0.572519
-['PPDB']           0.314908      -0.572519
-['RootDep']        6.728456       1.526718
-['NegAlgn']        0.096679      -1.335878
-['SVO']           -0.892890      -0.381679
-['PoS']           -1.355703      -3.244275
-['Sent']          -0.811333      -0.763359
-['AvgWordLen']    -0.161613      -1.145038
-['LenRatio']      -0.226582      -0.572519
-['Perc']          -0.081965       0.000000
```

## With base

### -i

```
Confusion matrix:
=================
             for  against  observing
for        224.0      3.0       19.0
against     13.0     64.0       14.0
observing   80.0      6.0      101.0

Measures:
=========
accuracy: 0.7424

Per class:
           accuracy precision    recall        F1
for        0.780534  0.706625  0.910569  0.795737
against    0.931298  0.876712  0.703297  0.780488
observing  0.772901  0.753731  0.540107  0.629283
         accuracy-cv  accuracy-test
Q           0.519765       0.503817
BoW         0.691460       0.687023
W2V         0.680286       0.679389
PPDB        0.686665       0.700382
RootDep     0.731372       0.723282
NegAlgn     0.729582       0.744275
SVO         0.748426       0.742366
```

### -a

```
>> Training classifier <<

CV score: :0.748426
Test score: :0.742366
Ablating: ['Q']
Ablated feature set:['BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO']
>> Training classifier <<

Ablated CV score: 0.7088271107263633
Ablated test score: 0.7290076335877863
Ablating: ['BoW']
Ablated feature set:['Q', 'W2V', 'PPDB', 'RootDep', 'NegAlgn', 'SVO']
>> Training classifier <<

Ablated CV score: 0.6625410934795635
Ablated test score: 0.6469465648854962
Ablating: ['W2V']
Ablated feature set:['Q', 'BoW', 'PPDB', 'RootDep', 'NegAlgn', 'SVO']
>> Training classifier <<

Ablated CV score: 0.7321369052477629
Ablated test score: 0.7156488549618321
Ablating: ['PPDB']
Ablated feature set:['Q', 'BoW', 'W2V', 'RootDep', 'NegAlgn', 'SVO']
>> Training classifier <<

Ablated CV score: 0.7256505818822319
Ablated test score: 0.7118320610687023
Ablating: ['RootDep']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'NegAlgn', 'SVO']
>> Training classifier <<

Ablated CV score: 0.6848785254987237
Ablated test score: 0.6755725190839694
Ablating: ['NegAlgn']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'SVO']
>> Training classifier <<

Ablated CV score: 0.7313864026731862
Ablated test score: 0.7213740458015268
Ablating: ['SVO']
Ablated feature set:['Q', 'BoW', 'W2V', 'PPDB', 'RootDep', 'NegAlgn']
>> Training classifier <<

Ablated CV score: 0.7295820758465199
Ablated test score: 0.7442748091603053
              accuracy-cv  accuracy-test
-['Q']           3.959889       1.335878
-['BoW']         8.588490       9.541985
-['W2V']         1.628909       2.671756
-['PPDB']        2.277541       3.053435
-['RootDep']     6.354747       6.679389
-['NegAlgn']     1.703959       2.099237
-['SVO']         1.884392      -0.190840
```

