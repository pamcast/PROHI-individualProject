# We Care Dashboard Example

**Author**: [Pamela Castillo]
<!-- As main author, do not write anything in the line below.
The collaborator will edit the line below in GitHub -->
**Collaborator**: Songyue Xie

_Note that this file is written in **MarkDown** language. A reference is available here: <https://www.markdownguide.org/basic-syntax/>_

Dashboard screenshots

![Your dashboard](./assets/dashboard1.png)
![Your dashboard](./assets/dashboard2.png)
![Your dashboard](./assets/dashboard3.png)
![Your dashboard](./assets/dashboard4.png)

## Introduction

This template project will contain a simple interactive web dashboard with Streamlit. I used my database from the data science course, the purpose of the dashboard is to identify patients that will have a heart disease, the dashboard contains a home page where the user can input information and submit to get the result if the patient will have a heart disease, it will also display charts from the descriptive analysis of the data and the about page displays information about the supervised and unsupervised modeling that was done with the data. 

## System description
The system should be user-friendly and easy to navigate, it will also comply with data privacy laws and will allow the user to input information about the patient. 

### Installation of libraries

Run the commands below in a terminal to configure the project and install the package dependencies for the first time.

If you are using Mac, you may need to install Xcode. Check the official Streamlit documentation [here](https://docs.streamlit.io/get-started/installation/command-line#prerequisites).

1. Create the environment with `python -m venv env`
2. Activate the virtual environment for Python
   - [Linux/Mac] `source env/bin/activate` 
   - [Windows command prompt] `.\env\Scripts\activate.bat` 
   - [in Windows PowerShell] `.\env\Scripts\Activate.ps1`
3. Make sure that your terminal is in the environment (`env`) not in the global Python installation. The terminal should start with the word `env`
4. Install required packages `pip install -r ./requirements.txt`
5. Check that the installation works running `streamlit hello`
6. Stop the terminal by pressing **Ctrl+C**

### Execute custom Dashboard

First, make sure that you are running Python from the environment. Check the steps 2 and 3 above. Then, to run the custom dashboard execute the following command:

```
> streamlit run Dashboard.py
# If the command above fails, use:
> python -m streamlit run Dashboard.py
```

### Dependencies

Tested on Python 3.12.7 with the following packages:
  - Jupyter v1.1.1
  - Streamlit v1.46.1
  - Seaborn v0.13.2
  - Plotly v6.2.0
  - Scikit-Learn v1.7.0
  - shap v0.48.0

## Contributors

_Add the project's authors, contact information, and links to websites or portfolios._

