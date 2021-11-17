# Analyzing Climate Change using Earth Surface Temperature Visualization

## Introduction to the Project

With each passing day, the threat of climate change has become an important matter to be concerned about. The emission of greenhouse gases like carbon dioxide and methane and drastic weather changes lead to global warming. Over recent years, there has been a massive increase in Earth’s surface temperature, rising heat waves, melting glaciers, and decreasing land size. Not only humans but also plants and animal kingdoms are being affected rigorously.

In this project, we will visualize how climate change affects the surface temperature of Earth and how it will likely look in the future.

## Set up Git LFS

The project contains files which are larger than 100MB and therefore they require GIT LFS to be set up on your machine. Here are the instructions to setup Git LFS:

### macOS:

Download HomeBrew if you don't already have it. Go to [brew.sh](https://brew.sh) or run the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Once done, run the following command:

```bash
brew install git-lfs
```

Then, install Git LFS, by running the following command (notice there is no dash(-) between `git` and `lfs`):

```bash
git lfs install
```

Restart your terminal.

### Windows:

Download the latest version of Git LFS from [the Git LFS website](https://git-lfs.github.com).

Then, install Git LFS, by running the following command (notice there is no dash(-) between `git` and `lfs`):

```bash
git lfs install
```

Restart your terminal.

### Linux (Debian or RHEL based):

packagecloud hosts git-lfs packages for popular Linux distributions with Apt/deb and Yum/rpm based package-managers. To get started, you need to add the packagecloud repository.

**These scripts must be run sudo root***** to

#### For APT/DEB repos:
```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
```

#### For Yum/RPM repos:

```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | sudo bash
```

If you are running LinuxMint 17.1 Rebecca, which is downstream of Ubuntu Trusty and Debian Jessie, you can run:

```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | os=debian dist=jessie sudo -E sudo bash
```

Finally Install Git LFS:

#### For APT/Debian based distributions:

```
sudo apt-get install git-lfs
```

#### For Yum/RPM based distributions:

```
sudo yum install git-lfs
```

Then, install Git LFS, by running the following command (notice there is no dash(-) between `git` and `lfs`):

```bash
git lfs install
```

Restart your terminal.

### Arch Linux:

Git LFS is available in the Arch repository. You can install by running this as root (sudo):

```
pacman -S git-lfs
```

Then, install Git LFS, by running the following command (notice there is no dash(-) between `git` and `lfs`):

```bash
git lfs install
```

Restart your terminal.

## Running the Project

You need Python on your machine in order to run the project. Get it from the [Python website](http://python.org) for your system. We recommend using **_Python 3.8.8_**.

Clone the project to your local machine:

```
git clone https://github.com/luciferreeves/Analyzing-Climate-Change-using-Earth-Surface-Temperature-Visualization.git
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Project:

```
python app.py
```

## Project Structure

```
.
├── GlobalLandTemperaturesByCity.csv [The orginal CSV data file]
├── README.md [This File]
├── app.py [Main Script]
├── database.db [Normalized database]
├── database_creation_script.py [Script to create the database]
├── dbcreation.ipynb [Notebook to create the database]
├── requirements.txt [The requirements file]
├── static [Contains Static Files]
│   ├── css [Contains CSS Files]
│   │   └── style.css [Internal Styles]
│   └── js [Contains JavaScript Files]
│       └── map.js [Map Rendering Algorithm]
└── templates [Contains HTML Files]
    └── index.html [Main HTML Dashboard]
```


## Dataset and Data Description

We will use the Berkeley Earth Surface Temperature Study dataset, which contains 1.6 billion temperature records. It is very well packaged and has interesting subsets (like countries, cities, and more). They have published the source data for the transformations. They have included methods that have weather observations from a short timespan to be included. In this dataset, there are several files. Global Land and Ocean-and-Land Temperatures record from 1750 – 2015.

Other files include – Global Average Land Temperature record for Country, Global Average Land Temperature record for State, Global Land Temperatures record for Major City, Global Land Temperatures record for City.

## Proposed Analysis

The raw data collected from Berkley Earth has been processed and cleaned by many developers and made into a proper dataset; researchers can work upon it and bring more insights. We will be demonstrating time series analysis over this dataset.

We will also build a machine learning model that predicts how the Earth's surface temperature is likely going to be in the future. Finally, we will package everything and put it in a dashboard, where users can see heat maps and visualize the changes for themselves.

## Refrences:

http://berkeleyearth.org/data/

https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data

