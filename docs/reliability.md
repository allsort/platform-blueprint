# Reliability and operations

## Health contracts

A health check should answer a narrow operational question. Separate process
liveness from readiness to receive traffic. Do not report healthy merely
because the web process started if the service cannot reach a required data
store or complete its startup work.

Health checks should be:

- inexpensive enough to run frequently;
- safe under partial dependency failure;
- explicit about which dependencies they cover;
- protected from leaking configuration or customer data;
- observable from the same network path used by the relevant caller.

## Monitoring and alerts

Monitor user-visible availability, certificate and DNS health, container or
process health, resource pressure, and product-specific failure signals. Alerts
need an owner and an action. A dashboard without a response path is not an
operational control.

## Backup and restore

Backups are incomplete until restoration has been exercised.

For each product data store, document:

- owner and storage location;
- encryption and access boundary;
- backup cadence and retention;
- expected recovery point and recovery time;
- restoration procedure;
- last successful restore exercise;
- dependencies that must be restored in order.

Do not infer that a successful backup command produced a usable recovery point.
Automated validation and periodic restore drills answer different questions and
both are valuable.

## Incident response

Runbooks should optimize for decisions under pressure:

1. Confirm user impact and current release.
2. Stop concurrent changes.
3. Preserve logs and evidence.
4. Choose between mitigation, rollback, and forward repair.
5. Verify recovery from outside the service boundary.
6. Record follow-up work with an owner.

Post-incident reviews should distinguish the triggering change from conditions
that allowed the impact to spread or remain undetected.
