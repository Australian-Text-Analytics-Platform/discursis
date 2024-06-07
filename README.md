# Discursis: conversation analysis and visualisation

This repository contains notebooks to demonstrate Discursis, a conversational
analysis and visualisation tool.

If you want to install and use the Discursis tool in your own projects, see 
the [atap_widgets](https://github.com/Australian-Text-Analytics-Platform/atap_widgets)
package.

## User guide

For a short introduction to the Discursis tool, please see the [user guide](https://raw.githubusercontent.com/Australian-Text-Analytics-Platform/discursis/master/docs/Discursis%20User%20Guide.pdf).

## Notebooks

The notebooks demonstrating Discursis are in Jupyter notebooks under `notebooks/`.

Click the Binder badge to open a demo notebook directly in Binder, an online platform for hosting
Jupyter notebooks:

* Intro to Discursis: [![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://binderhub.atap-binder.cloud.edu.au/v2/gh/Australian-Text-Analytics-Platform/discursis/master/?urlpath=lab/tree/notebooks/discursis_demo.ipynb)

<b>Note:</b> CILogon authentication is required. You can use your institutional, Google or Microsoft account to login. If you have trouble authenticating, please refer to the [CILogon troubleshooting guide](cilogon-troubleshooting.pdf).

* Backup Binder instance: [![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/Australian-Text-Analytics-Platform/discursis/master/?urlpath=lab/tree/notebooks/discursis_demo.ipynb)

Current version: [v0.0.1](https://github.com/Australian-Text-Analytics-Platform/discursis/releases/tag/v0.0.1)

<!-- START RUN INFO -->


## Run these notebooks

There are a number of different ways to use these notebooks. Binder is quickest and easiest, but it doesn't save your data. I've listed the options below from easiest to most complicated (requiring more technical knowledge).

### Using Binder

[![Launch on Binder](https://mybinder.org/badge_logo.svg)](https://binderhub.atap-binder.cloud.edu.au/v2/gh/Australian-Text-Analytics-Platform/discursis/master/?urlpath=lab/tree/index.md)

Click on the button above to launch the notebooks in this repository using the [Binder](https://mybinder.org/) service (it might take a little while to load). This is a free service, but note that sessions will close if you stop using the notebooks, and no data will be saved. Make sure you download any changed notebooks or harvested data that you want to save.

See [Using Binder](https://glam-workbench.net/using-binder/) for more details.


### Using Docker

You can use Docker to run a pre-built computing environment on your own computer. It will set up everything you need to run the notebooks in this repository. This is free, but requires more technical knowledge – you'll have to install Docker on your computer, and be able to use the command line.

* Install [Docker Desktop](https://docs.docker.com/get-docker/).
* Create a new directory for this repository and open it from the command line.
* From the command line, run the following command:  
  ```
  docker run -p 8888:8888 --name discursis -v "$PWD":/home/jovyan/work quay.io/ldaca_atap/discursis repo2docker-entrypoint jupyter lab --ip 0.0.0.0 --NotebookApp.token='' --LabApp.default_url='/lab/tree/notebooks/discursis_workshop.ipynb'
  ```
* It will take a while to download and configure the Docker image. Once it's ready you'll see a message saying that Jupyter Notebook is running.
* Point your web browser to `http://127.0.0.1:8888`

See [Using Docker](https://glam-workbench.net/using-docker/) for more details.

### Setting up on your own computer

If you know your way around the command line and are comfortable installing software, you might want to set up your own computer to run these notebooks.

You need to install Git, and the [Anaconda Python distribution](https://www.anaconda.com/products/distribution).

Then the steps to set up an environment with all the required packages are:

* Clone the repository: `git clone https://github.com/Australian-Text-Analytics-Platform/discursis.git`
* Change to the `discursis` directory: `cd discursis`
* Create the environment: `conda env create -f environment.yml`
* Activate the environment: `conda activate discursis`
* Run Jupyter: `jupyter lab`

See the GLAM Workbench documentation for [more details](https://glam-workbench.net/getting-started/#using-python-on-your-own-computer).

<!-- END RUN INFO -->

This repository was created using a template from the [GLAM Workbench](https://glam-workbench.net/).
