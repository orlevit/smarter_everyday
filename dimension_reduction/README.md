# 3D and 2D Dimensionality Reduction Visualization

This project demonstrates various techniques for dimensionality reduction and clustering using both synthetic and real-world datasets. 
The code covers 3D visualization of clustering results and a comparison of different dimensionality reduction methods in 2D space.

## Overview

*  **3D Visualization**:
   - Generates and visualizes 3D plots of the Swiss Roll and S Curve datasets.
   - Performs agglomerative clustering and K-Nearest Neighbors (KNN) classification on a sample dataset.
   - Displays clustering results using different color maps.

<figure>
  <img src="images/3d_combined_plots.png" width="900" height="400">
</figure>

* **2D Dimensionality Reduction Comparison**:
   - Applies various dimensionality reduction techniques (PCA, MDS, t-SNE, and UMAP) on multiple datasets.
   - Compares results in 2D plots to visualize how each technique transforms high-dimensional data.

<figure>
  <img src="images/2d_plots.png" width="900" height="500">
</figure>


## Datasets

**Considering these datasets:**

* **Mammoth**: A 3D scanned model of a woolly mammoth skeleton, included in the Smithsonian Institution's collection of digital 3D models. The dataset comprises 1 million data points, of which 5,000 have been randomly selected for analysis.

* **Swiss Roll**: A 3D dataset in which points are organized in a spiral, helical shape resembling a rolled-up surface. It is created using parametric equations that define a spiral: \(x = t \cdot \cos(t)\), \(y = h\), \(z = t\). Where \(t\) represents the distance along the spiral and \(h\) is a vertical component. Additional Gaussian noise is added to introduce variability. A total of 1000 data points were sampled.

* **Digits**: A dataset containing 1,797 samples of handwritten digits (0-9), represented as 8x8 pixel grayscale images. Each image is converted into a 64-dimensional vector, corresponding to the pixel intensities. This dataset is part of the UCI Machine Learning Repository.

* **S Curve**: A 2-dimensional (2D) surface embedded in a 3-dimensional (3D) space. The points in the dataset are arranged in an "S" shape, with the curve bending back and forth along two of the three axes, resulting in a non-linear form. This dataset is created by mapping a 2D grid onto a 3D space using the following mathematical function: \(x = t\), \(y = \sin(t)\), \(z = h\). A total of 1000 data points were sampled.

## Insights

1. **Mammoth, Swiss Roll, and S Curve**: PCA and MDS preserve the global structure of the data. However, **t-SNE and UMAP** might introduce artifacts, resulting in misleading clusters or artificial islands.

2. **Digits**: PCA and MDS produce cluttered visualizations. This is because they focus on **global structure preservation**, which may not sufficiently capture the local variations and distinct features of each digit. Consequently, the resulting plots can be less informative, with overlapping digit representations.

3. **PCA & MDS** - Best suited for preserving the global structure of the data, providing a broad overview. They may not capture local details as effectively, which can result in less detailed visualizations, especially for datasets with complex local structures.

4. **t-SNE and UMAP**: Excellent at preserving **local structures** and revealing small clusters or patterns within the data. They might introduce artifacts, and their performance is sensitive to hyperparameter settings. Proper tuning of these parameters is crucial to achieving accurate and interpretable results.
