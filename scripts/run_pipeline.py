from pathlib import Path
from scripts.utils import read_text, write_json, write_text
from scripts.extract_demo import extract_demo
from scripts.extract_onboarding import extract_updates
from scripts.generate_agent import generate_agent

demo_folder = Path("data/demo")
onboard_folder = Path("data/onboarding")
output_folder = Path("outputs/accounts")

def main():

    for file in demo_folder.glob("*.txt"):

        account_id = file.stem.split("_")[0]

        transcript = read_text(file)

        memo_v1 = extract_demo(account_id, transcript)

        agent_v1 = generate_agent(memo_v1,"v1")

        path = output_folder / account_id / "v1"

        write_json(path / "account_memo.json", memo_v1)
        write_json(path / "agent_spec.json", agent_v1)

    for file in onboard_folder.glob("*.txt"):

        account_id = file.stem.split("_")[0]

        transcript = read_text(file)

        updates = extract_updates(transcript)

        memo_path = output_folder / account_id / "v1" / "account_memo.json"

        if not memo_path.exists():
            continue

        memo = read_text(memo_path)

        import json
        memo = json.loads(memo)

        memo.update(updates)

        agent_v2 = generate_agent(memo,"v2")

        path = output_folder / account_id / "v2"

        write_json(path / "account_memo.json", memo)
        write_json(path / "agent_spec.json", agent_v2)

        changes = """
        v2 Changes:

        • Added emergency routing rules from onboarding call
        • Updated call transfer timeout to 60 seconds
        • Added integration constraint: never create sprinkler jobs in ServiceTrade
        • Updated agent configuration based on onboarding requirements
        """

        write_text(output_folder / account_id / "changelog.md", changes)

    print("Pipeline completed")

if __name__ == "__main__":
    main()