# Security model

## Supply-chain controls

Reusable automation reduces drift, but it also creates a high-impact trust
point. Consumers therefore reference shared workflows and actions by full
commit SHA. Version labels may appear in comments for readability, but mutable
tags are not execution boundaries.

Scanner installers should verify both publisher identity and downloaded bytes:

1. Pin the installer action or bootstrap mechanism.
2. Verify the scanner release signature or Sigstore bundle.
3. Constrain the expected workflow identity and OIDC issuer.
4. Verify the archive checksum before installation.
5. Install without requiring elevated host privileges.
6. Record machine-readable findings as retained artifacts.

Different repositories can advance scanner versions independently while using
one reviewed installation and reporting pattern.

## Secrets

- Store production values in the deployment system, not the repository.
- Document required secret names and owners without including example values
  that look real.
- Render runtime configuration only in the protected deployment context.
- Avoid sharing a credential merely because two products use the same vendor.
- Fail closed when required configuration is missing.
- Scan both changes and repository history before changing a repository to
  public visibility.

## Runtime posture

Where the application permits it:

- run as a non-root user;
- use a read-only root filesystem;
- mount writable temporary storage explicitly;
- drop Linux capabilities;
- enable `no-new-privileges`;
- apply resource limits;
- separate public, administrative, and data networks;
- expose only the edge service directly.

See [`examples/compose/secure-service.yml`](../examples/compose/secure-service.yml)
for a generic starting point.

## Vulnerability decisions

A scan result is an input to a decision, not a substitute for one. The default
gate blocks known high- and critical-severity findings. An exception should
record the affected artifact, exposure, fix availability, compensating
controls, owner, and expiry date.

Ignoring all unfixed vulnerabilities by default hides risk. If an unfixed-only
policy is temporarily required, retain the complete report even when the gate
considers only fixable findings.
