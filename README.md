# QSAR-monomer-reactivity-prediction
Repository for research project on predicting monomer pair reactivity ratios with QSAR models of the U-V scheme values based on quantum chemical descriptors.

## Data Set

Monomer molecules are stored as .mol2 files in the mol2files directory. The files and were built in [Avogadro](https://avogadro.cc) an open-source molecular editor.

The U V scheme values were recorded each in their own .csv file with the values corresponding to their molecule in alphabetical order. 

Descriptors were computed in [Dragon 7](https://chm.kode-solutions.net/products_dragon.php) by Kode Chemioinformatics. The .mol2 files along with external variables were imported to compute descriptors, and output a tab delineated text file of the values about a specified threshold. The Dragon outputs are in the dragon_out directory.

## Intercorrelation  Analysis

Dragon when exporting variables has the functionality to screen for intercorrelation. This was done with the outputs in the dragon_out directory.

Descriptor intercorrelation was also assessed with the script intercor.py in the main directory. The script accepts a dab delineated text dragon output and returns a table of the Pearson r coefficients for each descriptor. It additionally returns a table with the values above 0.4 removed.

```bash
python intercor.py dragon_out\U_data.txt
```
## Prediction Model

U and V models were build using [keras](https://keras.io) with an iterted k-fold approach in jupyter notebook. The files in the repository iterte through epoch values from 0 to 490 to evaluate the optimal setting.

An additional dependence for the models is [scikit](https://scikit-learn.org/stable/) for the shuffle function used in imppementing the iterated k-fold.
## Acknowledgments

This work was supported by the Bill and Linda Frost Fund at Cal Poly San Luis Obispo.
