# Contributing to the Open AOS Factory

Thank you for your interest in improving the **Open AOS Factory**. Contributions follow the same governance model the factory enforces for its own users: **every change flows through the design specification first.**

If you are new to contributing on GitHub, see [Contributing to a project](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project).

---

## The design spec is the source of truth

The canonical source of truth for the factory is `design-spec/aos-factory-design-specification.md`. It records every design decision made during the factory's development: the governance model, the permission levels, the folder schema, the builder section structure, agent responsibilities and boundaries, workflow definitions, escalation rules, and the framework-vs-instance layout. **If the spec and a builder file ever disagree, the spec wins.**

Because everything is generated from this one canonical spec, the design, the docs, and the implementation can't quietly drift apart. Keeping that discipline is what makes outside contribution practical — and it's why **only pull requests for the design spec will be considered.**

---

## How to propose a change

1. Open `design-spec/aos-factory-design-specification.md` and identify the section(s) your change affects.
2. Draft the proposed revision and discuss it in a **Planning mode** session (`pmode` at the start of your Claude session). Claude will not create or modify any files in this mode.
3. Once the revision is agreed, type `Proceed` to authorize the spec update. No regeneration of factory files happens without that explicit authorization.
4. Regenerate the affected builder file(s), then rebuild and repackage `claude-plugin/`. Test your changes with:

   - `Rebuild the factory`
   - `Create a new AOS`

5. Submit your design spec via a pull request. **Only pull requests for the design spec will be considered.**

---

## Adding a new agent builder

Adding a new agent builder follows the same sequence above, plus one additional step: add the new agent to the available-agent roster in the spec (Section 2.3 or equivalent), define its full section schema, then generate the builder file and `SKILL.md` together.

---

## What not to do

Do not edit builder files in `builders/` or skill files in `claude-plugin/aos-factory/skills/` directly without first updating the spec. The spec is the design record; a builder that diverges from it is a bug.

---

## Questions

For questions, or to discuss larger architectural changes before drafting spec language, open an issue.
