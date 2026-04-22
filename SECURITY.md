# Security Policy

## Supported Versions

The following versions of `solarfactors` currently receive security updates:

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

If you discover a security vulnerability, please report it by:

1. **Email**: Send a description of the vulnerability to the maintainers via the contact information listed on the [GitHub repository](https://github.com/pvlib/solarfactors).
2. **GitHub Private Vulnerability Reporting**: Use [GitHub's private vulnerability reporting](https://github.com/pvlib/solarfactors/security/advisories/new) feature if available.

### What to include in your report

Please include as much of the following information as possible to help us understand and reproduce the issue:

- Type of vulnerability (e.g., code injection, arbitrary file read, etc.)
- Full paths of the source file(s) related to the issue
- Step-by-step instructions to reproduce the vulnerability
- Proof-of-concept or exploit code (if possible)
- Impact of the vulnerability and how it might be exploited

### What to expect

- We will acknowledge receipt of your report within **5 business days**.
- We will investigate and provide an initial assessment within **10 business days**.
- We will notify you when the vulnerability has been fixed.
- We will credit you in the release notes unless you prefer to remain anonymous.

## Security Considerations

This package is a scientific/engineering library for PV irradiance modeling. It:

- Does **not** handle user authentication or authorization
- Does **not** store or transmit sensitive user data
- Processes numerical simulation inputs provided by the user

Users should exercise caution when loading simulation data from untrusted sources, as malformed inputs could potentially cause unexpected behavior.

## Disclosure Policy

We follow [responsible disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure). Once a fix is available, we will:

1. Release a patched version
2. Publish a security advisory on GitHub
3. Update the changelog with details of the fix
