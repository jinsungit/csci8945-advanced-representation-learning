Welcome to CSCI 8945: Advanced Representation Learning!
========================================================

**Course website**: *Advanced Representation Learning*

**Course edition**: Fall 2025

**Repository**: `GitHub Repository <https://github.com/yourusername/csci8945-advanced-representation-learning>`_

**Author**: Course Instructor

.. note::
   This course covers advanced topics in representation learning, including classical methods like PCA, 
   modern deep learning approaches, and cutting-edge techniques in self-supervised learning.

For this course, we have created a series of Jupyter notebooks that are designed to help you understand 
the "theory" from the lectures by seeing corresponding implementations. We will visit various topics 
such as Principal Component Analysis (PCA), autoencoders, variational autoencoders, contrastive learning, 
and more (for a full list, see below).

The notebooks are presented during lecture sessions and are designed to be both educational and practical. 
You can decide whether you want to look at the filled notebook, try it yourself, or code along during 
the sessions. The notebooks are directly relevant to assignments and exams.

Schedule (Fall 2025)
====================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - **Date**
     - **Topic**
   * - Week 1
     - Tutorial 1: Principal Component Analysis (PCA)
   * - Week 2
     - Tutorial 2: Kernel PCA and Non-linear Dimensionality Reduction
   * - Week 3
     - Tutorial 3: Autoencoders and Variational Autoencoders
   * - Week 4
     - Tutorial 4: Self-Supervised Learning and Contrastive Methods
   * - Week 5
     - Tutorial 5: Graph Representation Learning
   * - Week 6
     - Tutorial 6: Transformer Representations
   * - Week 7
     - Tutorial 7: Meta-Learning and Few-Shot Learning
   * - Week 8
     - Tutorial 8: Advanced Topics and Research Frontiers

How to run the notebooks
========================

On this website, you will find the notebooks exported into an HTML format so that you can read them 
from whatever device you prefer. However, we suggest that you also give them a try and run them yourself. 
There are three main ways of running the notebooks we recommend:

* **Locally on CPU**: All notebooks are stored in the GitHub repository. The notebooks are designed 
  so that you can execute them on common laptops without the necessity of a GPU. We provide pretrained 
  models that are automatically downloaded when running the notebooks. The required disk space for the 
  pretrained models and datasets is less than 2GB. To ensure that you have all the right Python packages 
  installed, we provide a conda environment file.

* **Google Colab**: If you prefer to run the notebooks on a different platform than your own computer, 
  or want to experiment with GPU support, we recommend using Google Colab. Each notebook on this 
  documentation website has a badge with a link to open it on Google Colab. Remember to enable GPU 
  support before running the notebook (``Runtime -> Change runtime type``).

* **University Computing Resources**: If you want to train your own (larger) neural networks based on 
  the notebooks, you can make use of university computing resources. However, this is only suggested 
  if you really want to train a new model.

Content Overview
================

**Tutorial Notebooks**

.. toctree::
   :maxdepth: 2
   :caption: Tutorial Notebooks

   notebooks/tutorial1_pca
   
**Course Information**

.. toctree::
   :maxdepth: 2
   :caption: Course Information

   course_info/syllabus
   course_info/assignments
   course_info/resources

Tutorial Notebooks
==================

Tutorial 1: Principal Component Analysis (PCA)
-----------------------------------------------

* Introduction to dimensionality reduction
* Mathematical foundations of PCA
* Implementation from scratch
* Comparison with sklearn implementation
* Applications to real datasets
* Visualization and interpretation

.. note::
   More tutorials will be added as the course progresses. Each tutorial builds upon previous concepts 
   and introduces new representation learning techniques.

Prerequisites
=============

* Linear algebra (vectors, matrices, eigenvalues/eigenvectors)
* Basic probability and statistics
* Python programming
* NumPy and matplotlib
* Basic machine learning concepts

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
