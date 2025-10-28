from src.agents.itinerary_agent import ItineraryAgent
from src.mediatool.message_bus_mock import MessageBus

def test_handle_intent_runs():
    bus = MessageBus()
    agent = ItineraryAgent(bus)
    intent = {'request_id': 't-1', 'user_id': 'u1', 'destination': 'Goa', 'days': 3, 'month': 'July', 'budget_inr': 25000}
    plans = agent.handle_intent(intent)
    assert isinstance(plans, list)
