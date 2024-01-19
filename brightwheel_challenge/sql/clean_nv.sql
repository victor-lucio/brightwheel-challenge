SELECT 
    CAST("Name" AS VARCHAR) as name,
    CAST("Credential Type" AS VARCHAR) as credential_type,
    CAST("Credential Number" AS VARCHAR) as credential_number,
    CAST("Status" AS VARCHAR) as status,
    CAST("Expiration Date" AS DATE) as expiration_date,
    CAST("Disciplinary Action" AS VARCHAR) as disciplinary_action,
    CAST("Address" AS VARCHAR) as address,
    CAST("State" AS VARCHAR) as state,
    CAST("County" AS VARCHAR) as county,
    CAST("Phone#" AS VARCHAR) as phone,
    CAST("First Issue Date" AS DATE) as first_issue_date,
    CAST("Primary Contact Name" AS VARCHAR) as primary_contact_name,
    CAST("Primary Contact Role" AS VARCHAR) as primary_contact_role
FROM 
    raw_nv;