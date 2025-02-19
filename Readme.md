# Non-covalent Lasso Entanglement in IDPs

This repository contains code and data related to the study of non-covalent lasso entanglement (NCLE) in intrinsically disordered proteins (IDPs). The repository is organized into the following sections:

## Protein Ensemble Database (PED) Statistics
- Analysis scripts and data for protein ensemble database statistics.
- Notebooks:
  - `Compile_fig1.ipynb`: Compiles Figure 1.
  - `Fig. 1_Count_number_of_entries.ipynb`: Counts the number of entries.
- Data files:
  - `fully_idp.pkl`, `fully_structure.pkl`, `long_idr.pkl`: Pickle files containing processed data.
  - `PED_all_exp_entries.xlsx`: Excel file with all experimental entries.
  - `PED2023/`: Code to retrive the disorder information from MobiDB and results of entanglement analyses of PED ensembles.

## Coarse-Grain Simulation of Synthetic Polymer Chains
- Scripts and data for simulating synthetic polymer chains with different residue lengths (N=100, 200, 300).
- Scripts:
  - `generate_synthetic_sequences.py`: Generates synthetic sequences for simulation.
- Data files:
  - `N100_results.pkl`, `N200_results.pkl`, `N300_results.pkl`: Pickle files containing simulation results.
- Notebooks:
  - `Plot_CG_simulations_superimpose_Phase_diagram_V2.ipynb`: Plots and superimposes phase diagrams of the simulations.

## Analysis of Human IDRs
- Analysis scripts and data for studying entanglement and functional enrichment in human intrinsically disordered regions (IDRs).
- Subdirectories:
  - `Entanglement/`: Contains scripts and data related to entanglement analysis.
  - `GO/`: Contains scripts and data related to functional enrichment analysis.

## Simulation Codes
- Code to perform CG simulations: [cosmo](https://github.com/vuqv/cosmo)

## Entanglement Code
- Code for entanglement analysis: [entanglement_analysis](https://github.com/vuqv/entanglement_analysis)