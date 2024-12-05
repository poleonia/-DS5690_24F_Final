# **Glomeruli Segmentation with SwinUnetr**

Glomeruli segmentation is a specialized field in medical imaging, particularly in nephrology and kidney pathology. It involves identifying and delineating glomeruli structures within histological images of kidney tissue. 
This project is to implement of glomeruli segmentation using the **Swin UNETR** model. Swin UNETR combines the strengths of the Swin Transformer architecture and the UNETR model to provide efficient and accurate segmentation in medical imaging tasks.

Key Highlights:
- Transformer-based model for effective feature extraction.
- Handles high-resolution medical imaging tasks.
- Robust to variations in tissue morphology and imaging conditions.

## **Data & Performance Information**

### Dataset

The training data for this project is sourced from the Kidney Precision Medicine Project (KPMP) 
(https://www.kpmp.org/available-data), 
a large-scale initiative aimed at understanding and treating kidney diseases. The KPMP pathology 
dataset contains high-resolution histological images, accompanied by expert-annotated labels that 
highlight glomerular structures.

Split patches extracted from 222 Whole Slide images,
- Training set : 3451 glomeruli patches. 
- Validation set : 659 glomeruli patches.
- Testing set : 1976 glomeruli patches.


## **Performance**
### Metric
- Dice similarity coefficient (Dice) 
- Hausdorff distance (HD)
- Mean Surface Distance (MSD). 
### Result
- Dice: 95.3
- HD: 66.4
- MSD: 10.1
---

## **Installation and Usage**
### Prerequisites
- Python 3.7+
- CUDA-capable GPU
- 8GB+ RAM

### Installation Steps
1. [Optional but recommended] Create a new Conda environment.
    ~~~
    conda create --name myenv python=3.7
    ~~~ 
    And activate the environment. 
    ~~~
    conda activate myenv
    ~~~
2. Clone this repo

3. Install the [requirements](requirements.txt)

### Running the Application

```bash
python testing.py --dataset_dir [Your Patch Folder] --reload_path .[Your PTH Folder] --result_folder [Your Output Folder]
```

## **Critical Analysis**

### Strengths
#### 1. Decent performance on glomeruli segmentation task
The model achieves high accuracy in segmenting glomeruli structures,
#### 2. Transformer-Based Features
Swin UNETR leverages self-attention mechanisms to capture long-range dependencies in the images, a critical feature for identifying structures like glomeruli amidst surrounding tissues.
#### 3. Automation
Automates a traditionally manual and labor-intensive task, reducing the workload of pathologists and ensuring consistency in segmentation across datasets.

### Limitation
#### 1. Dataset Limitations:
The current dataset primarily focuses on glomeruli segmentation, which, while valuable, imposes several limitations on the broader applicability of the model 
and its utility in kidney pathology research and diagnostics.
#### 1. Only Focus on Supervise learning:
Supervised learning requires large amounts of high-quality annotated data. In medical imaging, such annotations must be created by domain experts (e.g., pathologists), 
which is time-consuming, expensive, and prone to inter-observer variability.
The reliance on annotated data limits the scalability of the approach, especially when attempting to apply the model to new datasets or imaging modalities.

### Future Work
#### 1. More classes for segmentation tasks
Extend segmentation to classify glomeruli into more detailed categories, such as:Normal, Sclerotic ,Inflamed ,Fibrotic.
Expand beyond glomeruli to include surrounding kidney structures, such as tubules, interstitial regions, and blood vessels, for a holistic tissue analysis.
#### 2. Model improvements
- Self-Supervised Learning: Use self-supervised learning to pre-train models on large unlabeled datasets, improving performance with limited labeled data.
- Multi-Modal Models: Integrate imaging data with clinical metadata or molecular profiles using multi-modal transformer architectures for richer insights.
- Cross-Domain Transfer Learning:
Train the model on datasets from related domains (e.g., other organ histology) to leverage common features and enhance performance on smaller kidney-specific datasets.
## Citation
```
@inproceedings{hatamizadeh2021swin,
  title={Swin unetr: Swin transformers for semantic segmentation of brain tumors in mri images},
  author={Hatamizadeh, Ali and Nath, Vishwesh and Tang, Yucheng and Yang, Dong and Roth, Holger R and Xu, Daguang},
  booktitle={International MICCAI Brainlesion Workshop},
  pages={272--284},
  year={2021},
  organization={Springer}
}
```
