# Default (Logistic Regression)

## With PoS, Sentiment
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
