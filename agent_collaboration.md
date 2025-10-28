    # Agent Collaboration Model

- Agents communicate via a message bus (events) and support REST for sync queries.
- Example topics:
  - intent.requests
  - agent.weather.requests / agent.weather.responses
  - agent.transport.responses
  - agent.pricing.responses
  - agent.booking.commands
  - events.replanning

- Use consistent JSON message schema and versioning.

- Transaction pattern: Saga for bookings (compensating actions on partial failure).
