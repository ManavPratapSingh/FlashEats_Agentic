# Product Context

FlashEats Operations monitors live deliveries during busy service periods.

The current application is an internal tool, not a customer-facing product.

## Current operational objective

Help an Operations Manager focus on **active orders that may require intervention now**.

Operations currently treats an order as actionable risk according to the rule implemented in the existing service layer. Product language sometimes uses words such as *late*, *delayed*, and *at risk* loosely, so engineers should verify the implemented business rule before creating new logic.

## Important constraints

- Completed and cancelled orders should not enter the active intervention queue.
- Unknown delay should not be silently converted into a numeric risk value.
- Existing API contracts should remain stable unless a requirement explicitly changes them.
- The first MVP should not introduce driver reassignment, refunds, maps, or predictive-model changes.
