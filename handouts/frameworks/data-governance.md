---
title: "Data governance: proportionate, not prohibitive"
description: "Why 'don't upload anything to AI' is the wrong policy. The real risks are the pipeline (transmission, storage, jurisdiction), not model extraction. A four-step proportionate framework."
---

# Data governance: proportionate, not prohibitive

Many organisations have landed on blanket prohibitions: "do not upload company documents to AI." These policies treat all AI interaction as equally risky, and they conflate several distinct concerns – some legitimate, some based on fundamental misunderstandings of how large language models work.

## The legitimate concerns

The rational core of caution is about the **pipeline before training**: the transmission, processing, and storage of data, not what happens inside the model.

- **Data residency and sovereignty.** Regulations (GDPR, the Australian Privacy Act, sector-specific rules) require certain data to stay within specific jurisdictions. Pasting a document into a consumer AI tool transmits it to external infrastructure, often in another country. The act of transmission itself may be the compliance violation.
- **Contractual obligations.** NDAs, client agreements, and government contracts define which systems may process covered data. Sending it to a third-party AI service may breach those terms – even if the provider handles it perfectly.
- **Logging and retention.** AI providers may retain prompts for safety monitoring or debugging. A sensitive document sits on someone else's servers for a retention period. Enterprise agreements negotiate specific terms around this.
- **Supply chain risk.** AI providers, like any SaaS vendor, can be breached. This isn't the model leaking data; it's the company's servers being compromised. Standard infosec, managed through vendor risk assessments.

## Where the reasoning goes wrong

Problems emerge when organisations conflate those legitimate infrastructure concerns with fears about model behaviour – specifically, the belief that someone could extract uploaded documents from the model itself.

This misunderstands how LLMs work. LLMs interpolate; they do not retrieve. If data is used for training at all (enterprise tiers typically exclude it), it becomes a vanishingly small statistical signal distributed across billions of parameters. It is not stored as a retrievable file. It is dissolved into the model's general capability like a drop of ink in a swimming pool. There is no mechanism by which another user could query the model and reconstruct your document, because the model never stored it as a document.

## The double standard

Many organisations enforcing strict AI prohibitions happily allow employees to paste sensitive content into email, Slack, shared drives, and dozens of other SaaS tools – all of which carry the exact same transmission, storage, and jurisdictional risks. AI feels riskier because it's newer, not because the risk profile is different.

## A more useful framework

1. **Classify the data.** Public, internal, confidential, regulated?
2. **Match the tool to the classification.** Enterprise AI with data-processing agreements for internal/confidential work; consumer tools for public and non-sensitive brainstorming; regulated data needs a specific assessment.
3. **Manage the real risks.** Never paste credentials, API keys, or access tokens. De-identify personal information. Understand the provider's logging and retention terms.
4. **Drop the fictional risks.** Stop treating model extraction as a plausible threat. Focus governance effort where the actual exposure is: transmission, storage, jurisdiction, and contractual compliance.

The goal is professional data hygiene applied consistently across all tools – not AI exceptionalism driven by misunderstanding.

*Adapted from the AI Skills Passport's "Why Enterprise AI Data Governance Gets It Wrong."*
