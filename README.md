As a Machine Learning Research Intern at Design Innovation Centre (DIC) - Hub GTU, I have done a research project titled: 'Multimodal Alzheimer’s disease Classification Using MRI and Genetic Data' under the guidance of Dr.Neelesh Sharma, IIT Gandhinagar.
<br>
<br>

• Introduction:

Early detection of Alzheimer’s Disease is challenging because the biomarkers are often subtle, especially in the Mild Cognitive Impairment (MCI) stage. Models trained on a single modality (only MRI or only genetics) tend to miss parts of the underlying pathology.

The goal of this work is to:

Study how structural brain changes (MRI) and genetic variations (SNPs) complement each other

Evaluate whether multimodal fusion provides more reliable signals than single-modality approaches

Analyze not just performance, but also modality contribution and imbalance
<br>
<br>

• Dataset:

Source: Alzheimer’s Disease Neuroimaging Initiative (ADNI-1)

Subjects: 584 individuals

Modalities:

T1-weighted structural MRI scans

Genetic SNP data

Classes:

Cognitively Normal (CN)

Mild Cognitive Impairment (MCI)

Alzheimer’s Disease (AD)

Only subjects with both MRI and genetic data available were included to ensure proper multimodal alignment.

<br>
<br>
• Methodology Overview:
<br>
<br>
1. MRI Preprocessing and Feature Extraction

Tools: MONAI, NiBabel

Steps:

Intensity normalization

Resizing and standardization

Feature extraction:

Fine-tuned MedicalNet (3D-ResNet50) pre-trained on medical imaging datasets

Produces high-dimensional structural embeddings from T1 MRI volumes

2. Genetic SNP Processing

Tool: PLINK

Quality control steps:

Minor Allele Frequency (MAF) filtering

Removal of variants with high missingness

Linkage Disequilibrium (LD) pruning

Dimensionality reduction:

A Noisy Autoencoder trained in an unsupervised manner to compress SNP features into a lower-dimensional genetic embedding

Multimodal Fusion Strategies

Two fusion approaches were evaluated:

1. Feature-Level (Intermediate) Fusion

MRI and SNP embeddings are concatenated

Classification performed using ensemble models:

Random Forest

XGBoost

2. Gated Multimodal Units (GMU)

Uses learnable gates to dynamically weight each modality

Allows the model to adjust how much it relies on MRI vs genetics for different samples

Adds an interpretability layer by exposing modality importance

<br>
<br>
• Results and Observations:

Overall classification performance on ADNI-1 remained poor. This is likely due to:

Limited sample size after multimodal alignment

Sensitivity of models to preprocessing quality

However, some patterns were observed:
<br>
<img width="1188" height="685" alt="image" src="https://github.com/user-attachments/assets/1b3adfc4-fb78-4b66-99ef-30e80ff00441" />
<br>
AD & MCI Patients (median: 0.44): Show a stronger reliance on genetic data. The model likely identifies high-risk genetic markers as primary evidence for pathology. Whereas the normal group has  comparatively higher dependence.



<br>
<br>
• Future Work:

Planned extensions include:

Adding clinical variables (age, sex, cognitive scores) to provide context for imaging and genetic data

Exploring transformer-based cross-modal attention mechanisms

I identified that standard normalization is insufficient for capturing subtle structural atrophy. I am now motivated to explore robust neuroimaging pipelines, such as FastSurfer, to ensure high-fidelity inputs. This might have caused overreliance on genetic factors. I need to use methods like Grad-CAM and SHAP for further interpretability.

<br>
<br>
• References:

Chen, S., et al. (2019). Med3D: Transfer Learning for 3D Medical Image Analysis.

Venugopalan, J., et al. (2021). Multimodal deep learning models for early detection of Alzheimer’s disease stage.

Liu, S., et al. (2015). Multimodal neuroimaging feature learning for multiclass diagnosis of Alzheimer’s disease.

Johnston, B., et al. (2020). Gated Multimodal Units for Information Fusion.
