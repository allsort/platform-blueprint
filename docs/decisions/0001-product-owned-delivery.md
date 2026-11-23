# Decision 0001 Product owned delivery

## Status

Accepted as a reference pattern.

## Context

Centralizing every deployment in one infrastructure repository appears simple,
but it couples unrelated release schedules and separates application changes
from their verification logic.

## Decision

Each product repository owns its build, application checks, release artifact,
and product-specific deployment workflow. The platform repository owns shared
edge, identity, telemetry, and host constraints.

## Consequences

- Product changes and their tests are reviewed together.
- Shared platform changes remain independently deployable.
- Every product must document a consistent operational contract.
- Reusable workflows are valuable, but consumers pin them to immutable
  revisions and adopt upgrades deliberately.
