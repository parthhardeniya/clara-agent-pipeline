def extract_demo(account_id, transcript):

    text = transcript.lower()

    memo = {
        "account_id": account_id,
        "company_name": "",
        "business_hours": {
            "days": [],
            "start": "",
            "end": "",
            "timezone": ""
        },
        "office_address": "unknown",
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": {},
        "non_emergency_routing_rules": {},
        "call_transfer_rules": {
            "timeout_seconds": "",
            "retries": "",
            "fallback_message": ""
        },
        "integration_constraints": [],
        "after_hours_flow_summary": "Greeting → confirm emergency → collect caller details → transfer → fallback if transfer fails",
        "office_hours_flow_summary": "Greeting → ask purpose → collect caller details → transfer or schedule → fallback if transfer fails → close call",
        "questions_or_unknowns": [],
        "notes": "Generated from demo transcript"
    }

    if "firesafe" in text:
        memo["company_name"] = "FireSafe Systems"

    if "sprinkler" in text:
        memo["services_supported"].append("sprinkler systems")

    if "fire alarm" in text:
        memo["services_supported"].append("fire alarms")

    if "sprinkler leak" in text:
        memo["emergency_definition"].append("sprinkler leak")

    if "monday" in text:
        memo["business_hours"]["days"] = ["Mon","Tue","Wed","Thu","Fri"]

    if "8am" in text:
        memo["business_hours"]["start"] = "08:00"

    if "5pm" in text:
        memo["business_hours"]["end"] = "17:00"

    if "pst" in text:
        memo["business_hours"]["timezone"] = "PST"

    return memo