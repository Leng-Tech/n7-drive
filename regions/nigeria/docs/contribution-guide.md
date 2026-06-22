# Contribution Guide

Use stable, readable IDs and do not encode temporary source quirks into IDs.

Area ID examples:

```text
area:country:nigeria
area:zone:south-west
area:state:lagos
area:fct:abuja
area:lga:lagos:eti-osa
area:area-council:fct:abaji
area:ward:lagos:eti-osa:ward-a
area:polling-unit:lagos:eti-osa:ward-a:pu-024
```

When adding data:

1. Add the node record to the relevant file.
2. Add at least one explicit relationship to its parent or related area.
3. Add source references and quality metadata.
4. Mark unofficial or incomplete records as `NEEDS_REVIEW`.
5. Run `python3 regions/nigeria/scripts/validate.py`.

Future LGAs, wards, polling units, and constituency mappings should be sourced from official INEC or government records wherever possible. Do not add office holders, candidates, live results, user data, poll data, volunteer data, or reports to this repository.
