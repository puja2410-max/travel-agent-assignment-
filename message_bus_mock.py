import time

class MessageBus:
    def __init__(self):
        self.store = {}

    def publish(self, topic, message):
        print(f"[bus] publish {topic}: {message.get('request_id', '')}")
        self.store.setdefault(topic, []).append(message)

    def collect_responses(self, request_id, timeout=1):
        # simulate collecting responses from sub-agents
        time.sleep(0.1)
        return {
            'weather': { 'risk': 'high', 'forecast': 'heavy rain' },
            'transport': { 'recommended': 'flight', 'road_ok': False },
            'pricing': { 'est_total': 27000 }
        }
