### Problem Statement
This study aims to understand the number people's visits to outpatient healthcare facilities affected by weather (For example higher rainfall, is there increase number of people visit healthcare facilities). By looking at data on outpatient visits alongside rainfall records, we want to see if there's a connection between rainy days and more people seeking healthcare. This research can help us figure out how to plan healthcare services better, especially during rainy seasons, and make sure everyone gets the care they need. There should be a direct co-relationship between the rainy days and frequency of outpatient healthcare facilities visits.

### Datasets

Relevant weather datasets from [data.gov.sg](data.gov.sg):

* [Relative Humidity](https://data.gov.sg/dataset/relative-humidity-monthly-mean)
* [Monthly Maximum Daily Rainfall](https://data.gov.sg/dataset/rainfall-monthly-maximum-daily-total)
* [Hourly wet buld temperature](https://data.gov.sg/dataset/wet-bulb-temperature-hourly)
* [Monthly mean sunshine hours](https://data.gov.sg/dataset/sunshine-duration-monthly-mean-daily-duration)
* [Surface Air Temperature](https://data.gov.sg/dataset/surface-air-temperature-mean-daily-minimum)

Hospital Addmission and Outpatient Attendances datasets from [singstat.gov.sg](singstat.gov.sg):

* [Hospital Admissions, Public Sector Outpatient Attendances And Day Surgeries](https://tablebuilder.singstat.gov.sg/table/TS/M870341): Healthcare facilities attendances in Singapore from 1897 to 2024

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|month|int|df|Month|
|maximum_rainfall_in_a_day|int|df|Maximum rainfall in a day|
|total_rainfall|float|df|Total rainfall|
|mean_rh|float|df|Mean of Humidity|
|mean_sunshine_hrs|float|df|Mean of Sunshine per hour|
|mean_temp|float|df|Mean of Tempdrature|
|wet_bulb_temperature|float|df|Wet Bulb Temperature|
|date|datetime|df|Date in format: YYYY-MM-DD|
|year|int|df|Year|
|specialist_outpatient_clinics|int|df|Headcount of Attendance to Clinics|
|accident & emergency departments|int|df|Headcount of Attendance to A&E|
|polyclinics|int|df|Headcount of Attendance to Polyclinics|

### Conclusions and Recommendations

1. The correlation between number of rainy day and attendance of healthcare facilities are positive.
2. The correlation between air surface temperature and attendance of healthcare facilities are positive.
3. November and December have the highest number of rainy days.
4. May has the highest surface air temperature.
5. The months of May, November and December require more healthcare manpower and operating hour of the healthcare facilities
