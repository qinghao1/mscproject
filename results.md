# Default (Logistic Regression)

## With PoS, Sentiment
### Normal
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
