SELECT 
    CAST("Operation #" AS INTEGER) as operation,
    CAST("Agency Number" AS INTEGER) as agency_number,
    CAST("Operation/Caregiver Name" AS VARCHAR) as operation_caregiver_name,
    CAST("Address" AS VARCHAR) as address,
    CAST("City" AS VARCHAR) as city,
    CAST("State" AS VARCHAR) as state,
    CAST("Zip" AS INTEGER) as zip,
    CAST("County" AS VARCHAR) as county,
    CAST("Phone" AS VARCHAR) as phone,
    CAST("Type" AS VARCHAR) as type,
    CAST("Status" AS VARCHAR) as status,
    CAST("Issue Date" AS DATE) as issue_date,
    CAST("Capacity" AS INTEGER) as capacity,
    CAST("Email Address" AS VARCHAR) as email_address,
    CAST("Facility ID" AS INTEGER) as facility_id,
    CAST("Monitoring Frequency" AS VARCHAR) as monitoring_frequency,
    CAST("Infant" AS BOOLEAN) as infant,
    CAST("Toddler" AS BOOLEAN) as toddler,
    CAST("Preschool" AS BOOLEAN) as preschool,
    CAST("School" AS BOOLEAN) as school
FROM 
    raw_tx;