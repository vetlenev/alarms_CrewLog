# Dashboard solution for alarm KPIs
The scope of this project is to streamline the handover reporting of alarms between shifts offshore. Currently, operators collect alarm data and manually fills out a report with relevant KPIs for the workers on the next shift. The KPIs are filled out manually in excel files that few people look at due to complexity and inefficiency. This project aims to automate this process using CDF and Cognite Functions, presenting the KPIs in an easily interpretable and visually pleasing manner through a dashboard for rapid insight. Through improved filtering and prioritization of alarms, the operators avoid an overwhelming list of alarms to be managed cross-shifts, and can instead invest time and effort to acknowledge and resolve the alarms that are truly important.

## Getting started
1. Clone the repository into desired folder and change directory
```
git clone https://github.com/vetlenev/alarms_CrewLog.git
cd alarms_CrewLog
```
2. Make sure to have [poetry](https://python-poetry.org/docs/) installed.
3. Set the location of the virtual environment to be inside the project repository
```
poetry config virtualenvs.in-project true
````
4. Install dependencies specified from the poetry environment
```
poetry install
```
5. Activate the poetry environment
```
.venv/Scripts/activate
```
and select `.venv` as kernel in the interactive script `src/alarmKPI.ipynb`

## Subject for improvement
This section presents some of the challenges with the current implementation, and suggestions for improvement and resolutions.
1. Inconsistent time stamps between CDF and ABB
- Data in CDF and ABB are registered for different time zones and daylight savings. Event data in CDF is two hours behind that in ABB during summer time, and one hour during winter time. This time difference must be accounted for in the Python SDK. This is not a sustainable solution on the long term, as there might be updates to the representative time zone in the Cognite Python SDK
