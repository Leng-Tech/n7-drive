# Nigeria Civic Knowledge Graph

This directory stores the canonical Nigeria civic and electoral reference data for Voter's Choice. It models civic geography, offices, elections, election-management bodies, political parties, and relationships as a graph-compatible set of JSON and YAML files.

The graph is not a strict tree. Administrative geography, electoral representation, and result collation can overlap, so relationships are stored explicitly instead of being inferred from folder layout alone.

Current coverage:

- Country: Nigeria
- Geopolitical zones: 6
- States and FCT: 37 records
- LGAs and FCT Area Councils: 774 records migrated from the previous repository seed data
- Core offices, election types, management bodies, collation routes, election actors, and INEC-sourced political parties

Later phases should add source-matched wards, polling units, senatorial districts, federal constituencies, state constituencies, and boundary mappings.

Run validation with:

```sh
python3 regions/nigeria/scripts/validate.py
```
