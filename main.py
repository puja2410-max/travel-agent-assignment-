"""Demo CLI to run a sample intent through the mock message bus and planner"""
from src.mediatool.message_bus_mock import MessageBus
from src.agents.itinerary_agent import ItineraryAgent

def demo():
    bus = MessageBus()
    agent = ItineraryAgent(bus)
    intent = {
        'request_id': 'req-001',
        'user_id': 'user_001',
        'destination': 'Goa',
        'days': 3,
        'month': 'July',
        'budget_inr': 25000,
        'preferences': { 'transport': 'road' }
    }
    plan = agent.handle_intent(intent)
    print('\n=== Suggested Plans ===')
    for p in plan:
        print(p)

if __name__ == '__main__':
    demo()
