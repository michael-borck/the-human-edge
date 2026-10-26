# Sample Tickets for the Demo

These four tickets are written to match **real rows** in `activities/retailflow-customer-service-data.csv` (the dataset participants analyse in Exercise 3). The CSV holds metadata only, no ticket text, so the text below is invented to fit each row's category, channel, and metrics. This lets the demo reference tickets participants have genuinely seen in the data.

| Ticket | CSV row | Category | Channel | Note in the data |
|--------|---------|----------|---------|------------------|
| RF-5175 | 2024-07-10 | Billing Queries | Phone | 6.7h response, satisfaction 3.4, resolved |
| RF-5030 | 2024-07-11 | Delivery Problems | Phone | 5.1h response, satisfaction 3.1, **not resolved** |
| RF-5149 | 2024-07-07 | Returns & Refunds | Email | **20.0h response, satisfaction 1.0** (near the dataset's worst) |
| RF-5189 | 2024-07-05 | Order Tracking | Live Chat | 2.7h response, satisfaction 4.5, resolved |

## The ticket text (paste into Pi)

```
Ticket 1 (RF-5175, phone): I've been billed twice for my September order. I want the duplicate charge refunded today; I've already called once and nobody called me back.

Ticket 2 (RF-5030, phone): My delivery was due eight days ago. The courier says the parcel is lost. I work from home and this box has my work equipment in it.

Ticket 3 (RF-5149, email): I have tried twice to return my order and the portal keeps failing. This is the worst service I have ever had. I want my money back and I am posting about this online.

Ticket 4 (RF-5189, live chat): Where is my order? The tracking page hasn't updated in three days.

Triage these four tickets.
```

## Expected triage (with the skill installed)

| Ticket | Category | Severity | Suggested owner | First action |
|--------|----------|----------|-----------------|--------------|
| RF-5175 | Billing Queries | High | Finance Team | Verify the duplicate charge and process the refund |
| RF-5030 | Delivery Problems | High | Logistics Team | Open a courier trace and offer a replacement dispatch |
| RF-5149 | Returns & Refunds | High | Returns Team | Fix the portal failure manually and process the refund |
| RF-5189 | Order Tracking | Low | Support Agent | Send a tracking update with the current dispatch status |

Escalation sentence: RF-5149 first (money, unresolved, and a public-reputation threat), then RF-5030 (unresolved, customer's work blocked).

Exact wording will vary by model. If a small local model produces a slightly off table, that is fine, even useful: it feeds the verification message. The structure (table, categories, escalation) is what the skill supplies.
