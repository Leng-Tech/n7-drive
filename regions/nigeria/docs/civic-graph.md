# Civic Graph Model

The dataset uses nodes and edges.

Nodes are civic or electoral things: country, zone, state, FCT, LGA, ward, polling unit, office, election type, election-management body, party, or election actor.

Edges are relationships between things. The same area can participate in different relationship contexts:

- `ADMINISTRATIVE`: country, zone, state, LGA, ward, polling-unit hierarchy.
- `ELECTORAL`: constituency and representation boundaries.
- `COLLATION`: result movement for a specific election type.
- `REPRESENTATION`: offices that represent a civic area.
- `OPERATIONAL`: election-management or event logistics.

Example citizen-map path:

```text
area:polling-unit:* -> area:ward:* -> area:lga:* -> area:state:* -> area:zone:* -> area:country:nigeria
```

Example collation path for presidential elections:

```text
POLLING_UNIT -> WARD -> LGA -> STATE -> COUNTRY
```

Do not infer all relationships from area nesting. Constituencies and collation routes should be added as explicit relationship records when source data is available.
