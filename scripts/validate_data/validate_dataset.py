#!/usr/bin/env python3
"""
Simple validation script for the Fiscal Consolidation SSA dataset.

This script checks that the dataset conforms to the schema defined in
`data/schema/dataset_schema.json` and that there are no duplicate
country‑year entries.

Usage:

    python validate_dataset.py
"""
import json
import os
import pandas as pd
import sys

def load_schema(schema_path: str) -> dict:
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate(df: pd.DataFrame, schema: dict) -> list:
    errors = []
    # Check required columns
    for col in schema['required']:
        if col not in df.columns:
            errors.append(f"Missing required column: {col}")
    # Check data types
    for col, props in schema['properties'].items():
        if col not in df.columns:
            continue
        expected_type = props['type']
        # Basic type checks
        if expected_type == 'integer' and not pd.api.types.is_integer_dtype(df[col]):
            errors.append(f"Column {col} is not integer type")
        if expected_type == 'string' and not pd.api.types.is_object_dtype(df[col]):
            errors.append(f"Column {col} is not string type")
    # Check duplicates
    dup_mask = df.duplicated(subset=['iso3', 'year'], keep=False)
    if dup_mask.any():
        dups = df.loc[dup_mask, ['iso3', 'year']].drop_duplicates()
        for _, row in dups.iterrows():
            errors.append(f"Duplicate entry for {row['iso3']} in {row['year']}")
    return errors

def main():
    # Locate the current dataset (data/current/narrative_shocks.csv)
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_path = os.path.join(repo_root, 'data', 'current', 'narrative_shocks.csv')
    schema_path = os.path.join(repo_root, 'data', 'schema', 'dataset_schema.json')
    if not os.path.exists(data_path):
        print(f"Dataset not found at {data_path}", file=sys.stderr)
        sys.exit(1)
    df = pd.read_csv(data_path)
    schema = load_schema(schema_path)
    errors = validate(df, schema)
    if errors:
        print("Validation errors:")
        for err in errors:
            print(f" - {err}")
        sys.exit(1)
    print("Dataset validation passed.")

if __name__ == '__main__':
    main()
