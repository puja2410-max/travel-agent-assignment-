    # Use Cases

## Simple Use Case (Weather-based adjustment)
1. User: 3 days in Goa in July, budget ₹25,000.
2. Itinerary Agent queries Weather Agent -> High rainfall risk.
3. Itinerary Agent suggests indoor activities and/or alternate months (Dec–Feb) with cost/time tradeoffs.

## Advanced Use Case (Dynamic re-planning - Flight delayed)
1. Booking Agent receives flight-delay webhook (6 hours).
2. Booking Agent emits `events.replanning`.
3. Itinerary Agent invokes replanner -> consults Transport & Pricing agents.
4. Replanner outputs options; Booking Agent auto-books or prompts user based on preference.
