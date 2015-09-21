WARNING: Contains lengthy instructions on how to run some code.

This repository contains the souce code for my MSc Project: "For or Against? Assessing the evidence for news headline claims". The code is written in Python 2.7 and makes use of a number of external libraries, such as pandas, sklearn, gensim, munkres and others. To run the code from scratch, I suggest:

1. cloning the project in the normal way, i.e issuing the command: 
      
      **git clone https://github.com/willferreira/mscproject.git**, at the command prompt

2. creating a new folder, called *data*,  in the top directory of the project
3. copying the contents (folders and files) from this dropbox link to the new *data* folder: https://www.dropbox.com/sh/9t7fd7xfahb0e1v/AACtdXhZmaTU9QgxZ8jL5tyVa?dl=0
4. installing the excellent anaconda distribution of Python 2.7 from continuum.io, available here: http://continuum.io/downloads 
5. creating a new Python virtual environment, by issuing the following command at the prompt:

      **conda create -n XXX anaconda python=2.7** 
   
   (replacing XXX with whatever you want to call the environment, e.g. mscproject_py27)
6. activating the new virtual environment issuing the followingcommand at the prompt:

      **source activate XXX** 
      
   (replacing XXX with whatever you called your environment)
7. installing package: repoze.lru (provides a function memoize decorator) by issuing the following command at the 
   prompt (accept whatever package updates it proposes):

      **conda install repoze.lru**
      
8. installing package: gensim (provides a word2vec library) by issuing the following command at the prompt 
   (accept whatever package updates it proposes):

      **conda install gensim**
      
9. installing package: munkres 1.0.7 (provides an implementation of the Hungarian Algorithm, used for word alignment) by:
    1. downloading the package from https://pypi.python.org/pypi/munkres/
    2. unzipping the file somewhere
    3. cd munkres-1.0.7
    4. issuing the command: **python setup.py install**, at the prompt

You should now have all you need to run the code. The relevant scripts are in the project bin/ directory. From there you can run the following:

**python run_train_test.py**

    - trains the model on the EmergentLite training data-set, and then runs the trained model on the test data-set. 
      All the features are used in the model, namely: Q,BoWHed,BoWRef,I,BoW,AlgnW2V,AlgnPPDB,RootDist,NegAlgn,SVO. 
      The output should look something like this:
      
      Feature set: ['Q', 'BoWHed', 'BoWRef', 'I', 'BoW', 'AlgnW2V', 'AlgnPPDB', 'RootDist', 'NegAlgn', 'SVO']
      >> Training classifier <<
      >> Classifying test data <<
      
      Confusion matrix:
      =================
                 for  against  observing
      for        197       11         40
      against     10       72         11
      observing   54       11        103
      
      Measures:
      =========
      accuracy: 0.7308
      
      Per class:
                  accuracy  precision     recall         F1
      for        0.7740668  0.7547893  0.7943548  0.7740668
      against    0.9155206  0.7659574  0.7741935  0.7700535
      observing  0.7721022  0.6688312  0.6130952  0.6397516
      
**python run_train_test.py -i**

      As above, but the features are added incrementally, and the intermediate results of 10-fold cv are displayed 
      during the cv phase of training. The final output shows the changes in accuracy, averaged over the cv folds, 
      and on the test set, as each new feature is added to the model. The (final) output should look something like:
      
      >> Training classifier <<
      >> Classifying test data <<
      Confusion matrix:
      =================
                 for  against  observing
      for        197       11         40
      against     10       72         11
      observing   54       11        103
      
      Measures:
      =========
      accuracy: 0.7308
      
      Per class:
                  accuracy  precision     recall         F1
      for        0.7740668  0.7547893  0.7943548  0.7740668
      against    0.9155206  0.7659574  0.7741935  0.7700535
      observing  0.7721022  0.6688312  0.6130952  0.6397516
      
                accuracy-cv  accuracy-test
      Q            0.511414       0.524558
      BoWHed       0.601743       0.644401
      BoWRef       0.692385       0.728880
      I            0.693368       0.726916
      BoW          0.707527       0.721022
      AlgnW2V      0.706851       0.719057
      AlgnPPDB     0.713028       0.717092
      RootDist     0.725663       0.738703
      NegAlgn      0.726644       0.732809
      SVO          0.731760       0.730845
      
**python run_train_test.py -f <command-separated list of feaures>**

      Using the -f switch, the model can be run with any subset of the features, given as a comma-separated list, e.g.
      python run_train_test.py -f "Q,BoW,I".
      
**python run_train_test.py -i -f <command-separated list of feaures>**

      This case combines the others, so that a the incremental output for a given list of features is displayed.

To run the code for the MaxEntClassificationEDA classifier, do the following:

1. Follow the instructions to download an install EOP, which can be found here: https://github.com/hltfbk/EOP-1.2.3/wiki
2. Train the model with the English RTE-3 training data-set, and then test it with the EmergentLite test data-set: 

      1. cd into the following directory: <where you installed EOP>/Excitement-Open-Platform-1.2.3/target/EOP-1.2.3
      2. train the model: issue the following command at the prompt:
      
            java -Djava.ext.dirs=../EOP-1.2.3 eu.excitementproject.eop.util.runner.EOPRunner -train -trainFile ./eop-resources-1.2.3/data-set/English_dev.xml -config ./eop-resources-1.2.3/configuration-files/MaxEntClassificationEDA_Base+WN+VO+TP+TPPos_EN.xml
            
      3. test the model: issue the following command at the prompt:
      
            java -Djava.ext.dirs=../EOP-1.2.3 eu.excitementproject.eop.util.runner.EOPRunner -test -testFile <path to where mscproject was cloned>/mscproject/data/emergent/url-versions-2015-06-14-clean-test-rte.xml -config ./eop-resources-1.2.3/configuration-files/MaxEntClassificationEDA_Base+WN+VO+TP+TPPos_EN.xml -output <where you want the output to go>
            
3. Train the model with the EmergentLite training data-set, and then test it with the EmergentLite test data-set:

      1. cd into the following directory: <where you installed EOP>/Excitement-Open-Platform-1.2.3/target/EOP-1.2.3
      2. train the model: issue the following command at the prompt:
      
            java -Djava.ext.dirs=../EOP-1.2.3 eu.excitementproject.eop.util.runner.EOPRunner -train -trainFile <path to where mscproject was cloned>/mscproject/data/emergent/url-versions-2015-06-14-clean-train-rte.xml -config ./eop-resources-1.2.3/configuration-files/MaxEntClassificationEDA_Base+WN+VO+TP+TPPos_EN.xml
            
      3. test the model: same as step 3. above
      
In each case above, the output will consist of a number of files. The results files will be named: MaxEntClassificationEDA_Base+WN+VO+TP+TPPos_EN.xml_results.{txt or xml}; the contents are pretty self-explanatory.

The project comes complete with an ./output/eop/ directory containing pre-computed results:

      ./rte-clean-test/ - the results of training the model on English RTE-3, and testing it on EmergentLite (test data-set)
      
      ./rte-clean-test-fa/ - the results of training the model on English RTE-3, and testing it on EmergentLite (test data-set) with observing stance articles removed, i.e. only against the for and against stances
      
      ./emergent-clean-test/ - the results of training the model on EmergentLite (training data-set), and testing it on EmergentLite (test data-set)
      
      ./fold-X/ - the results of training the model on English RTE-3, and testing it on EmergentLite (test data-set fold X)
      
Running the following script:

**python run_train_test.py**

compares the (pre-computed) output of the MaxEntClassificationEDA classifier for the scenarios decribed above, and outputs accuracy results.

      






