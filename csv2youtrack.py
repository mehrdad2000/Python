#https://github.com/JetBrains/youtrack-python-scripts
#https://www.jetbrains.com/help/youtrack/server/2020.1/Import-from-CSV-File.html

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
