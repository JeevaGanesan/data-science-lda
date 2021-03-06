Clustering
----------

Visualize clustering using Kmeans and LDA
=========================================

This section describes clustering using Kmeans and LDA model for the vectors.


.. code-block:: console

    LDA_MODEL_REPO_PATH=./data-science-lda/data_science/lda/test_2020-04-26_20:33:54/test_2020-04-26_20:33:54_lda_model PYTHONPATH=. pipenv run python3 cli.py -m

``NUMBER_CLUSTERS`` is optional in this case and set to the same number of topics obtained through the LDA model.

This command will create plots using `Uniform Manifold Approximation and Projection for Dimension Reduction (UMAP) <https://pypi.org/project/umap-learn/>`__
showing clusters created with vectors from the LDA model.