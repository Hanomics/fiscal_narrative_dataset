#!/usr/bin/env python3
"""
Smoke check for the paper replication dataset.

Loads `dataset.dta` at the repository root (the authoritative paper replication
file, stored in Git LFS) and prints a short summary: columns, dtypes, row
count, and any duplicate (iso3, year) rows if those columns are present. This
is intentionally a best-effort check rather than strict schema enforcement --
the schema under `data/schema/` was designed for the prior CSV layout and has
not been reconciled with the Stata file yet.

Exits non-zero only if the file is missing or unreadable.

TODO: reconcile `data/schema/dataset_schema.json` with the actual columns and
dtypes of `dataset.dta` (the Stata replication dataset), then tighten this
validator again to enforce the reconciled schema (required columns, dtypes,
and no duplicate country-year rows).

Usage:

    python validate_dataset.py
"""
import os
import sys

import pandas as pd

LFS_POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1"


def is_lfs_pointer(path: str) -> bool:
    with open(path, "rb") as f:
        head = f.read(len(LFS_POINTER_PREFIX))
    return head == LFS_POINTER_PREFIX


def main() -> int:
    repo_root = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    data_path = os.path.join(repo_root, "dataset.dta")

    if not os.path.exists(data_path):
        print(f"Dataset not found at {data_path}", file=sys.stderr)
        return 1

    if is_lfs_pointer(data_path):
        print(
            f"{data_path} is a Git LFS pointer (real contents not fetched); "
            "skipping summary."
        )
        return 0

    try:
        df = pd.read_stata(data_path)
    except Exception as exc:
        print(f"Failed to read {data_path} with pandas.read_stata: {exc}", file=sys.stderr)
        return 1

    print(f"Loaded {data_path}")
    print(f"  rows: {len(df)}")
    print(f"  columns: {list(df.columns)}")
    print("  dtypes:")
    for col, dtype in df.dtypes.items():
        print(f"    {col}: {dtype}")

    if {"iso3", "year"}.issubset(df.columns):
        dup_mask = df.duplicated(subset=["iso3", "year"], keep=False)
        n_dups = int(dup_mask.sum())
        if n_dups:
            print(f"  WARNING: {n_dups} duplicate (iso3, year) rows found")
        else:
            print("  no duplicate (iso3, year) rows")

    return 0


if __name__ == "__main__":
    sys.exit(main())
