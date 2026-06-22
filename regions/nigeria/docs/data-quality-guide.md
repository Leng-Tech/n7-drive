# Data Quality Guide

Quality metadata records review state and verification depth.

Statuses:

- `DRAFT`: early contribution, not ready for product import.
- `SOURCE_MATCHED`: matched to a named source.
- `VERIFIED`: reviewed and accepted for product use.
- `NEEDS_REVIEW`: usable as a placeholder or seed, but not final.
- `CONFLICTED`: sources disagree or data requires adjudication.
- `DEPRECATED`: retained for history but should not be used as current data.

Use `issues` for concrete next actions, such as verifying an LGA against an official source or replacing a type-level example with a constituency-specific mapping.
