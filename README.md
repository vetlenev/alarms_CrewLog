# Alarm analysis integration with CrewLog
The scope of this project is to streamline the handover reporting of alarms between shifts offshore. Currently, operators collect alarm data and manually fills out a report with KPIs relevant for the workers on the next shift. The KPIs are filled out in an excel file that few people look at due to complexity and inefficiency. This project aims to automate this process using CDF and Cognite Functions, presenting the KPIs in an easily interpretable manner through a dashboard for rapid insight.
Through improved filtering and prioritization of alarms, the operators avoid an overwhelming list of alarms to be managed cross-shifts, and can instead invest time and effort to acknowledge and resolve the alarms that really matter. The alarm dashboard facilitates more valuable actions and better time usage for operations.

## Getting started
To be continued ...

## Subject for improvement
This section presents some of the challenges with the current implementation, and suggestions for improvement and resolutions.
1. Inconsistent time stamps
- Event data in CDF is two hours (one hour if winter time) behind the corresponding event data in the ABB source system. In other words, the two systems operate with different time zones. This forces us to manually add two (or one) hours to the time stamp of every event in CDF. This is not a sustainable solution on the long term, as there might be updates to the representative time zone in the Cognite Python SDK
