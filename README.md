# Instagram-themed Phishing Simulation (Ethical / Training)

> ⚠️ **Important:** This repository is for **authorized, ethical security awareness and testing only**.  
> Do **not** use any materials here to target real users or systems without written authorization. Unauthorized phishing is illegal.

## Purpose
Run a controlled simulation that mimics an Instagram credential-harvest style attack for the purpose of:
- Measuring employee/user susceptibility to social engineering;
- Delivering immediate training and remediation to those who interact with the simulation;
- Improving technical controls (email filtering, MFA, URL inspection) and reducing organizational risk.

## High-level Goals
- Assess click and credential submission rates.
- Provide non-punitive, constructive training to users.
- Deliver an executive summary and technical findings to stakeholders.
- Demonstrate improvements over repeated campaigns.

## Rules of Engagement (ROE) — (MUST be signed before testing)
- **Authorization**: Written, signed authorization from an executive or security owner is required. Store it in the `auth/` folder.
- **Scope**: Define which user groups, departments, or test accounts are in scope. Exclude external customers, minors, contractors, and VIPs unless explicitly authorized.
- **Timeline**: Predefine start and end datetimes.
- **Data**: Use simulated/test credentials where possible. If real credentials are collected accidentally, notify the authorized contact immediately and follow the purge procedure.
- **Escalation**: List contacts for Incident Response, Legal, HR, and the campaign owner.
- **Privacy**: Results are confidential; access limited to authorized staff.

## Safe Lab Environment (recommended)
- Run campaigns inside an isolated network segment or private lab VLAN.
- Use private DNS or test domains (e.g., `lab.local`, `example.test`) — do not register deceptive public domains.
- Do NOT publish or port-forward simulation servers to the public internet.
- Use test email domains and simulated user accounts.
- Log to encrypted storage with strict ACLs. Keep logs only as long as needed.

## Tools (Ethical / Recommended)
- **GoPhish** — open source phishing simulation platform (use only in lab or authorized environment).
- Commercial security awareness platforms (for automated training workflows).
- Internal mail server or sandboxed SMTP relay for test deliveries.
- VM snapshots and restore points for safe rollback.

> Note: Avoid custom, publicly hosted credential capture. Instead, use landing pages that immediately show a training message or accept only simulated credentials.

## Safe Simulation Design (principles)
1. **Educational landing page**: If a user submits credentials, show a clear, immediate training page (e.g., “This was a simulated test — you are now enrolled in a 10-minute awareness module”).
2. **Minimal data collection**: Collect only the metrics needed (clicks, submits, time to click). Avoid storing real passwords.
3. **Pilot first**: Run a small pilot with consenting accounts to validate wording, links, and monitoring.
4. **Non-punitive**: Results should be used for training and improvement, not punishment.

## Data Handling & Retention
- Minimize collection. Prefer boolean metrics (clicked/submitted) and timestamps.
- If credentials are collected, immediately move them to secure storage, notify the campaign owner, and delete after analysis. Keep an audit log of deletion.
- Retention period: default 30–90 days (set by policy), then securely purge.
- Access restricted to the security team. All handling must follow company privacy policy.

## Reporting & Deliverables
- **Executive summary**: high level risk, click/submit rates, top recommendations.
- **Technical appendix**: methodology, infrastructure used, pilot results, raw metrics.
- **User remediation plan**: individualized training for those who submitted credentials (if agreed), organization-wide lessons.
- **Follow-up plan**: schedule re-tests and track KPI trends.

## Pre-launch Checklist
- [ ] Signed ROE in `auth/`
- [ ] Pilot run completed and validated
- [ ] Test accounts configured
- [ ] Mail server / SMTP relay isolated
- [ ] Landing page set to educational content on submit
- [ ] Monitoring and logging verified
- [ ] Escalation contacts confirmed

## Example Templates (placeholders — fill before running)
- `templates/ROE-template.md` — Rules of Engagement
- `templates/pilot-checklist.md` — Pilot steps
- `templates/escalation-contact.md` — Contacts and phone numbers
- `templates/user-training-email.md` — Post-test training message

### Example (short) ROE wording (fill and sign):
> We authorize the Security Team to conduct an Instagram-themed phishing simulation for employees of [Org]. Scope: [departments/test accounts]. Dates: [start — end]. Campaign owner: [name, email, phone]. Signed: [executive, name, date].

## Ethical Considerations
- Never expose or transmit real passwords offsite.
- Never coerce password resets or lock accounts publicly.
- Avoid content that could cause panic, financial action, or reputational harm.
- Coordinate with HR for any required communications.

## Post-Test Remediation
- Send immediate training/materials to users who clicked or submitted (non-punitive).
- Enforce technical mitigations where patterns emerged (block senders, add URL scanners, enforce MFA).
- Share executive findings and recommended budget/controls for improvement.

## Frequently Asked Questions (FAQ)
**Q:** Can we use real user accounts?  
**A:** Only with explicit consent in the signed ROE. Prefer simulated/test accounts.

**Q:** Do we send emails from real domains?  
**A:** Prefer internal/test domains and isolated SMTP relays. Do not impersonate third parties without legal review.

**Q:** How long should data be kept?  
**A:** Keep only for analysis and remediation; purge per your privacy policy (commonly 30–90 days).

## Further Reading & Resources
- GoPhish documentation (use in lab only)
- Security awareness training providers (for follow-up modules)
- Local legal counsel or compliance for privacy and consent guidance

## Contact & Repository Owner
- Security Team — `security@example.com`  
- Campaign Owner: `[Name]` — `[email]`

---

> If you want, I can also:
> - Provide a **fillable ROE template** file you can drop into `templates/ROE-template.md`.  
> - Produce a **pre-launch checklist** markdown file.  
> - Draft a short **non-punitive user training email** to send after the simulation.

