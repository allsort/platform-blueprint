# Decision 0002 Verify before and after cutover

## Status

Accepted as a reference pattern.

## Context

A successful container start does not prove that the candidate is configured
correctly, and candidate success does not prove that edge routing serves the
intended release.

## Decision

Validate the candidate before cutover, switch traffic atomically, then verify
the externally served release. Restore the previous release automatically or
through a bounded operator action when live verification fails.

## Consequences

- Deployment takes slightly longer.
- Failures are discovered before or immediately after user traffic changes.
- The previous release and its configuration must remain available until live
  verification completes.
