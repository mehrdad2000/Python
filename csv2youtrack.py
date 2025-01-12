#https://github.com/JetBrains/youtrack-python-scripts
#https://www.jetbrains.com/help/youtrack/server/2020.1/Import-from-CSV-File.html

step1
pip2 install youtrack-scripts

step2
csv2youtrack -g -m mapping.json mycsv.csv

step3
csv2youtrack -m mapping.json -t '$TOKEN'  mycsv.csv http://192.168.1.1:4001


#mycsv.csv
project_id	project_name	numberInProject	summary	created	reporterName	description	resolved	State	Assignee	Due Date	Regarding	Subsystem	Type	Priority	Fix versions	Estimate Person Per Day	Related Issue	Reference
PT	project-test	6208	task1	2025-01-01	a_user	"info"		Verified & Closed			ALL	NEW	Bug	1	116		PUB_APP-2192	user1


#mapping.json
{
    "csv_field_delimiter": ",",
    "csv_value_delimiter": ",",
    "date_format_string": "%Y-%m-%d",
    "field_names": {
        "project_id": "project_id",
        "project_name": "project_name",
        "numberInProject": "numberInProject",
        "summary": "summary",
        "created": "created",
        "reporterName": "reporterName",
        "description": "description",
        "resolved": "resolved",
        "State": "State",
        "Assignee": "Assignee",
        "Due Date": "Due Date",
        "Regarding": "regarding",
        "Subsystem": "subsystem",
        "Type": "type",
        "Priority": "priority",
        "Fix versions": "Fix versions",
        "Estimate Person Per Day": "Estimate Person Per Day",
        "Related Issue": "Related Issue",
        "Reference": "Reference"
    },
    "field_types": {
        "State": "state[1]",
        "Assignee": "user[1]",
        "Due Date": "date"
    },
    "use_markdown": "no"
}
