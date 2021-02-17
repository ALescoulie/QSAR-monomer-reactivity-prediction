# QSAR-monomer-reactivity-prediction
Repository for rescearch project on predicting monomer pair reactivity ratios with QSAR models of the U-V scheme values based on quantumchemical descriptors.

## Data Set

Monomer molecules are stored as .mol2 files in the mol2files directory. The files and were drawn in [Avogadro](https://avogadro.cc) an open source molecular editor.

The U V scheme values were recorded each in their own .csv file with the values coorisponding to their molecule in alphabetical order. 

Descriptors were computed in [Dragon 7](https://chm.kode-solutions.net/products_dragon.php) by Kode Chemioinformatics. The .mol2 files along with external varriables were imported to compute descriptors, and output a tab delinated text file of the values about a specified threshold. The Dragon outputs are in the dragon_out directory.

## Intercorelation Analysis

Dragon when exporting varriables has the functionality to screen for intercorrelation. This was done with the outputs in the dragon_out directory.

descriptor intercorrelation was also assesed with the script intercor.py in the main directory. The script accepts a dab delineated text dragon output and returns a table of the pearson r coefficients for each descriptor. It additionally returns a table with the values above 0.4 removed.

'''bash
python intercor.py dragon_out\U_data.txt
'''
## Prediction Model

U and V models were build using [keras](https://keras.io) with an itterted k-fold approach in jupyter notebook. The files in the respoitory itterte throught epoch values from 0 to 490 to evaluate the optmal setting.

An additional dependence for the models is [scikit](https://scikit-learn.org/stable/) for the shuffle function used in implimenting the itterated k-fold.
## Acknowledgments

This work was supported by the Bill and Linda Frost Fund at Cal Poly San Luis Obispo.
