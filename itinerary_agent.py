from src.mediatool.message_bus_mock import MessageBus
from src.planners.optimizer import optimize_candidates

class ItineraryAgent:
    def __init__(self, bus: MessageBus = None):
        self.bus = bus or MessageBus()

    def handle_intent(self, intent):
        # publish intent on bus
        self.bus.publish('intent.requests', intent)
        responses = self.bus.collect_responses(intent['request_id'])
        candidates = self._assemble_candidates(intent, responses)
        best = optimize_candidates(candidates, weights={'cost': 0.6, 'comfort': 0.4})
        return best

    def _assemble_candidates(self, intent, responses):
        candidates = []
        # Candidate: keep month but prefer indoor activities
        candidates.append({ 'name': 'Keep July - indoor focus', 'cost': responses['pricing']['est_total'], 'comfort': 0.6 })
        # Candidate: suggest alternate month Dec
        candidates.append({ 'name': 'Move to Dec - outdoor friendly', 'cost': 32000, 'comfort': 0.9 })
        return candidates
