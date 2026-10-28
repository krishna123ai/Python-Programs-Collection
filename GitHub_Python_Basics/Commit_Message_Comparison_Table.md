# Commit Message Comparison Table

This document compares human-authored commit messages with AI-generated commit messages following the conventional commits standard (`type: short imperative summary` under 50 characters) across all three repositories.

## Comparison Table

| Repository | Actual Change | Your Commit Message | AI Commit Message | Which Is Better / Why? |
|---|---|---|---|---|
| `python-basics-krishnagupta-factorial` | Added initial factorial calculation script | `Add factorial program` | `feat: add iterative factorial script` | **AI**: More precise and adheres to conventional commit prefix (`feat:`), specifying implementation type within 50 characters. |
| `python-basics-krishnagupta-factorial` | Added AI-generated README documentation | `Update README documentation` | `docs: add initial README documentation` | **AI**: Accurately specifies the commit type (`docs:`) and that it is the initial documentation. |
| `python-basics-krishnagupta-factorial` | Added audit comparing README claims to code | `Add README claims audit` | `docs: add claims audit against code` | **AI**: Clarifies that the audit is checked against actual source code while staying concise. |
| `python-basics-krishnagupta-factorial` | Removed unsupported claims from README based on audit | `Remove unsupported README claims` | `docs: correct unsupported README claims` | **Tie**: Both are very clear; human message is direct and accurately describes removing unverified claims. |
| `python-basics-krishnagupta-fibonacci` | Added initial fibonacci sequence generator script | `Add fibonacci program` | `feat: add iterative fibonacci generator` | **AI**: Provides helpful specificity (`iterative`) and standard `feat:` prefix. |
| `python-basics-krishnagupta-fibonacci` | Added initial README documentation | `Add README for fibonacci` | `docs: add README with usage instructions` | **AI**: States what the README contains (`usage instructions`) and follows convention. |
| `python-basics-krishnagupta-fibonacci` | Added audit file verifying claims | `Add audit file` | `docs: add audit verifying fibonacci claims` | **AI**: Identifies specifically which claims are being verified rather than generic "audit file". |
| `python-basics-krishnagupta-fibonacci` | Removed unverified claims from README | `Clean up README claims` | `docs: trim unsupported claims from README` | **AI**: More accurate and uses proper prefix; human was slightly informal ("Clean up"). |
| `python-basics-krishnagupta-struct-to-dict` | Added struct-to-dict conversion script | `Add struct to dict script` | `feat: implement struct to dict converter` | **AI**: Better action verb (`implement`) and standard format. |
| `python-basics-krishnagupta-struct-to-dict` | Added initial README documentation | `Create README` | `docs: add struct-to-dict documentation` | **AI**: Human message was too vague ("Create README"), AI specifies project context. |
| `python-basics-krishnagupta-struct-to-dict` | Added audit.md analyzing claims | `Add audit.md` | `docs: audit claims in struct-to-dict README` | **AI**: Explains purpose of the file rather than just repeating filename. |
| `python-basics-krishnagupta-struct-to-dict` | Updated README to remove false claims | `Update README after audit` | `docs: align README claims with actual code` | **AI**: Clearly explains the alignment goal of the edit rather than just stating that an audit took place. |

## Key Insights
1. **Consistency**: AI-generated messages consistently apply the `type: imperative summary` convention (e.g. `feat:`, `docs:`), making Git history uniform and easy to parse.
2. **Conciseness vs Specificity**: While human messages are quick to type, they often lean towards generic descriptions (e.g., "Add audit.md"). The AI prompts consistently produced specific descriptions under 50 characters.
3. **Accuracy Check**: AI messages must always be checked to ensure they do not hallucinate features not present in the change.
