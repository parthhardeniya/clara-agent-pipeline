def generate_agent(memo, version):

    agent = {

        "agent_name": f"{memo['company_name']} Dispatch Agent",

        "voice_style": "professional, calm, helpful",

        "system_prompt": f"""
You are Clara AI answering calls for {memo['company_name']}.

You assist callers with sprinkler systems and fire alarm services.

Business hours are {memo['business_hours']['days']} 
from {memo['business_hours']['start']} to {memo['business_hours']['end']} 
timezone {memo['business_hours']['timezone']}.

Emergency situations include:
{memo['emergency_definition']}.

Always collect caller name, phone number and address before transferring.

Remain polite, concise and professional.
""",

        "key_variables": {
            "account_id": memo["account_id"],
            "company_name": memo["company_name"],
            "timezone": memo["business_hours"]["timezone"],
            "business_hours": memo["business_hours"],
            "office_address": memo["office_address"],
            "services_supported": memo["services_supported"],
            "emergency_definition": memo["emergency_definition"]
        },

        "tool_placeholders": [
            "transfer_call",
            "schedule_service_call"
        ],

        "call_transfer_protocol": {
            "timeout_seconds": memo["call_transfer_rules"]["timeout_seconds"] or 60,
            "retries": memo["call_transfer_rules"]["retries"] or 1,
            "message": "Please hold while I transfer your call."
        },

        "fallback_protocol": "If transfer fails apologize and collect caller name, phone number and address so the team can call back.",

        "version": version
    }

    return agent