    # Data & Control Flow (high level)

    - User issues intent via UI -> Itinerary Agent.
- Itinerary Agent publishes intent to message bus.
- Sub-agents (Weather, Transport, Pricing, Preference) subscribe and respond with structured responses.
- Itinerary Agent collects responses, constructs candidate itineraries and runs the planner/optimizer.
- Final itinerary returned to UI with explanation traces and booking links (if user confirms).
