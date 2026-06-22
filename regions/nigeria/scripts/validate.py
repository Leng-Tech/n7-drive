#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AREA_FILES = [
    'areas/country.json',
    'areas/geopolitical-zones.json',
    'areas/states.json',
    'areas/lgas.json',
    'areas/wards.json',
    'areas/polling-units.json',
    'areas/senatorial-districts.json',
    'areas/federal-constituencies.json',
    'areas/state-constituencies.json',
]
RELATIONSHIP_FILES = [
    'relationships/area-relationships.json',
    'relationships/electoral-boundary-relationships.json',
    'relationships/collation-relationships.json',
]
JSON_FILES = [p for p in ROOT.rglob('*.json')]

errors = []

def load_json(rel):
    path = ROOT / rel
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        errors.append(f'{rel}: invalid JSON: {exc}')
        return None

def require(condition, message):
    if not condition:
        errors.append(message)

for path in JSON_FILES:
    try:
        json.loads(path.read_text())
    except Exception as exc:
        errors.append(f'{path.relative_to(ROOT)}: invalid JSON: {exc}')

areas = []
for rel in AREA_FILES:
    data = load_json(rel)
    if data is not None:
        require(isinstance(data, list), f'{rel}: expected a JSON array')
        areas.extend(data if isinstance(data, list) else [])

area_ids = set()
for area in areas:
    aid = area.get('id')
    require(aid, f'area missing id: {area}')
    require(aid not in area_ids, f'duplicate area id: {aid}')
    area_ids.add(aid)
    require(area.get('sources'), f'{aid}: missing sources')
    require(area.get('quality'), f'{aid}: missing quality')
    if area.get('type') != 'COUNTRY':
        require(area.get('parentId'), f'{aid}: non-country area missing parentId')

relationships = []
for rel in RELATIONSHIP_FILES:
    data = load_json(rel)
    if data is not None:
        require(isinstance(data, list), f'{rel}: expected a JSON array')
        relationships.extend(data if isinstance(data, list) else [])

relationship_ids = set()
parent_relationships = set()
for rel in relationships:
    rid = rel.get('id')
    require(rid, f'relationship missing id: {rel}')
    require(rid not in relationship_ids, f'duplicate relationship id: {rid}')
    relationship_ids.add(rid)
    require(rel.get('sources'), f'{rid}: missing sources')
    require(rel.get('quality'), f'{rid}: missing quality')
    if rel.get('fromAreaId') and rel.get('toAreaId'):
        require(rel['fromAreaId'] in area_ids, f'{rid}: fromAreaId not found: {rel["fromAreaId"]}')
        require(rel['toAreaId'] in area_ids, f'{rid}: toAreaId not found: {rel["toAreaId"]}')
        if rel.get('relationshipType') == 'BELONGS_TO':
            parent_relationships.add((rel['fromAreaId'], rel['toAreaId']))

for area in areas:
    if area.get('type') == 'COUNTRY':
        continue
    if area.get('type') in {'GEO_POLITICAL_ZONE', 'STATE', 'FCT', 'LGA', 'AREA_COUNCIL'}:
        require((area['id'], area['parentId']) in parent_relationships, f'{area["id"]}: missing BELONGS_TO relationship to parentId')

for rel in ['offices/offices.json', 'elections/election-types.json', 'elections/collation-routes.json', 'parties/political-parties.json']:
    data = load_json(rel)
    if isinstance(data, list):
        seen = set()
        for record in data:
            rid = record.get('id')
            require(rid, f'{rel}: record missing id')
            require(rid not in seen, f'{rel}: duplicate id {rid}')
            seen.add(rid)
            require(record.get('sources'), f'{rid}: missing sources')
            require(record.get('quality'), f'{rid}: missing quality')

if errors:
    print('Validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print(f'Validation passed: {len(areas)} areas, {len(relationships)} relationships, {len(JSON_FILES)} JSON files.')
