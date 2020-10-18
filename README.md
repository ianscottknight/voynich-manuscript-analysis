# Voynich Manuscript Analysis

An analysis of the Voynich manuscript using modern data analysis methods.

## Project Organization
------------

    │
    ├── README.md           
    ├── CHANGELOG.md        <- See keepachangelog.com
    ├── pyproject.toml      <- See PEP 518
    ├── poetry.lock         <- See Poetry documentation
    ├── tests               <- Scripts for testing
    ├── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │   └── fix_notebook_imports.py
    ├── references          <- Data dictionaries, manuals, and all other explanatory materials.
    ├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting
    └── voynich_manuscript_analysis
        ├── util.py         <- Shared functions and helpful file paths
        ├── make_dataset.py <- Scripts to download or generate data
        ├── pipeline.py     <- Data processing pipeline to be used in train.py and predict.py
        ├── train.py        <- Train model
        ├── predict.py      <- Make predictions using a trained model
        ├── visualize.py    <- Script to create exploratory and results-oriented visualizations
        ├── data
        │   ├── external    <- Data from third party sources.
        │   ├── interim     <- Intermediate data that has been transformed.
        │   ├── processed   <- The final, canonical data sets for modeling.
        │   └── raw         <- The original, immutable data dump.
        └── models          <- Trained and serialized models and model predictions
     


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
