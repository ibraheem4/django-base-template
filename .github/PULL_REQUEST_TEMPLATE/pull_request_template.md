## Overview

Provide a high-level summary of the purpose of this PR. Mention the problem it solves or the feature it introduces.

## Key Changes

Summarize the important changes made in this PR. Use bullet points for clarity.

Examples:

- Added automated release drafting using `release-drafter`
- Refactored models to include new relationships (e.g., `FeeModel`)
- Replaced `commitlint` with `commitizen` for better commit message formatting

## Code Highlights

Mention specific code changes or configurations that are worth noting. This helps reviewers focus on critical areas.

Examples:

- Updated workflows (e.g., `release-drafter.yml` or `aptible.yml`)
- Introduced new models or services
- Modified state management logic or API integrations

## Testing

Describe how the changes were tested and any relevant test results. Ensure the PR includes all necessary tests and indicate the environment where tests were performed.

Examples:

- Verified workflow automation in staging
- Tested model relationships to ensure data integrity
- Confirmed commit message formatting using commitizen

## Checklist

- [] Code follows project standards
- [] All tests passing
- [] Documentation updated (if applicable)
- [] Tested in staging environment
- [] Includes relevant screenshots, diagrams, or videos demonstrating the change

## Links

Include links to any relevant environments, documentation, or designs.
Examples:

- [Development Environment preview](app-81578.on-aptible.com)
- [Staging Environment preview](app-81579.on-aptible.com)

## Attachments

Provide any supporting images, videos, or diagrams that will help reviewers understand the changes better.

Examples:

<!-- <img width="758" alt="Example Screenshot 1" src="https://github.com/user-attachments/assets/example1.png"> -->
<!-- <img width="692" alt="Example Screenshot 2" src="https://github.com/user-attachments/assets/example2.png"> -->

## Additional Notes

Add any additional information that the reviewer might need to know. Mention pending tasks or technical debt, if any.

---

### GitHub Issue Tagging

**Format:** Use `fixes #{GITHUB_ISSUE_NUMBER}` or `closes #{GITHUB_ISSUE_NUMBER}` to automatically link and close issues on GitHub when the PR is merged.

Examples:

- `fixes #123`
- `closes #456`

Make sure to reference the relevant GitHub issues in your commit messages or PR description to keep issue tracking synchronized.

---
