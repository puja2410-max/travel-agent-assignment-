from src.planners.replanner import replan_on_delay

def test_replan_on_delay():
    opts = replan_on_delay({}, 6)
    assert len(opts) >= 1
