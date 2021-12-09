# Analyzing Climate Change using Earth Surface Temperature Visualization

## Introduction to the Project

With each passing day, the threat of climate change has become an important matter to be concerned about. The emission of greenhouse gases like carbon dioxide and methane and drastic weather changes lead to global warming. Over recent years, there has been a massive increase in Earth’s surface temperature, rising heat waves, melting glaciers, and decreasing land size. Not only humans but also plants and animal kingdoms are being affected rigorously.

In this project, we will visualize how climate change affects the surface temperature of Earth and how it will likely look in the future.

## Clone the Project

You need Python on your machine in order to run the project. Get it from the [Python website](http://python.org) for your system. We recommend using **_Python 3.8.8_**.

Clone the project to your local machine:

```
git clone https://github.com/luciferreeves/Analyzing-Climate-Change-using-Earth-Surface-Temperature-Visualization.git
```

## Setting Up Dependencies ([Skip this step](#automate-above-processes))

To install dependencies run:

```
pip install -r requirements.txt
```

## Getting Files ([Skip this step](#automate-above-processes))

The project contains files which are larger than 100MB and therefore they require to be downloaded separately. Go to [latest releases page](https://github.com/luciferreeves/Analyzing-Climate-Change-using-Earth-Surface-Temperature-Visualization/releases/latest) and download these 3 files:

- arima.compressed
- database.db
- GlobalLandTemperaturesByCity.csv

Put all three in the root of the project directory. Read the [Project Structure](#project-structure) to visualize the directory structure.

## Automate Above Processes

You can also run [initial_setup.py](initial_setup.py) and these files will be downloaded automatically. If you are missing any dependencies, then those would be installed automatically as well.

To do so, run the following command:

```
python initial_setup.py
```

## Start Flask Server

Run the Project using the following command:

```
python app.py
```

## Dataset and Data Description

We will use the Berkeley Earth Surface Temperature Study dataset, which contains 1.6 billion temperature records. It is very well packaged and has interesting subsets (like countries, cities, and more). They have published the source data for the transformations. They have included methods that have weather observations from a short timespan to be included. In this dataset, there are several files. Global Land and Ocean-and-Land Temperatures record from 1750 – 2015.

Other files include – Global Average Land Temperature record for Country, Global Average Land Temperature record for State, Global Land Temperatures record for Major City, Global Land Temperatures record for City.

## Proposed Analysis

The raw data collected from Berkley Earth has been processed and cleaned by many developers and made into a proper dataset; researchers can work upon it and bring more insights. We will be demonstrating time series analysis over this dataset.

We will also build a machine learning model that predicts how the Earth's surface temperature is likely going to be in the future. Finally, we will package everything and put it in a dashboard, where users can see heat maps and visualize the changes for themselves.

## Project Structure

```
.
├── GlobalLandTemperaturesByCity.csv
├── LICENSE
├── README.md
├── __dbscripts__
│   ├── database_creation_script.py
│   └── dbcreation.ipynb
├── app.py
├── arima.compressed
├── arima.pkl
├── cities.json
├── database.db
├── functions
│   ├── array_functions.py
│   └── sql_functions.py
├── initial_setup.py
├── libs
│   ├── __pycache__
│   │   └── decompressor.cpython-38.pyc
│   ├── decompressor.py
│   └── zipper.py
├── model_builder.py
├── predictor.py
├── requirements.txt
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       ├── map.js
│       └── search.js
└── templates
    └── index.html
```

## Refrences:

http://berkeleyearth.org/data/

https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data

