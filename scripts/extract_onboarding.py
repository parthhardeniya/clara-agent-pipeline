import re

def extract_updates(transcript):

    updates = {}
    text = transcript.lower()

    timeout = re.findall(r'(\d+) seconds', text)

    if timeout:
        updates["call_transfer_rules"] = {
            "timeout_seconds": int(timeout[0])
        }

    if "never create sprinkler jobs" in text:
        updates["integration_constraints"] = [
            "never create sprinkler jobs in ServiceTrade"
        ]

    return updates