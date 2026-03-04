# Clara Agent Pipeline

## Overview

This project builds an automation workflow that converts **demo call transcripts and onboarding transcripts** into structured configurations for a **Retell AI voice agent**.

The system extracts key information from transcripts and automatically generates:

* Account Memo JSON
* Retell Agent Draft Specification
* Versioned updates (v1 → v2)
* Changelog describing onboarding modifications

The entire pipeline runs locally and requires **zero paid APIs or services**.

---

## Project Architecture

Demo Transcript
→ Extract account data
→ Generate Account Memo JSON (v1)
→ Generate Retell Agent Draft Spec (v1)
→ Store outputs

Onboarding Transcript
→ Extract updates
→ Update account memo
→ Generate updated agent spec (v2)
→ Store outputs + changelog

---

## Folder Structure

```
clara-agent-pipeline
│
├── scripts
│   ├── run_pipeline.py
│   ├── extract_demo.py
│   ├── extract_onboarding.py
│   ├── generate_agent.py
│   └── utils.py
│
├── data
│   ├── demo
│   │   ├── ACC001_demo.txt
│   │   ├── ACC002_demo.txt
│   │   ├── ACC003_demo.txt
│   │   ├── ACC004_demo.txt
│   │   └── ACC005_demo.txt
│   │
│   └── onboarding
│       ├── ACC001_onboarding.txt
│       ├── ACC002_onboarding.txt
│       ├── ACC003_onboarding.txt
│       ├── ACC004_onboarding.txt
│       └── ACC005_onboarding.txt
│
├── outputs
│   └── accounts
│
├── templates
│   ├── account_schema.json
│   └── agent_template.json
│
├── workflows
│   └── orchestrator_workflow.md
│
└── README.md
```

---

## Setup Instructions

### 1. Install Python

Install Python **3.9 or later**.

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the pipeline

```
python -m scripts.run_pipeline
```

---

## Dataset

The pipeline processes:

* 5 demo call transcripts
* 5 onboarding transcripts

Located in:

```
data/demo/
data/onboarding/
```

Each transcript corresponds to a specific **account_id**.

Example:

```
ACC001_demo.txt
ACC001_onboarding.txt
```

---

## Outputs

For each account the pipeline generates:

```
outputs/accounts/{account_id}
```

Example:

```
outputs/accounts/ACC001/
    v1/
        account_memo.json
        agent_spec.json
    v2/
        account_memo.json
        agent_spec.json
    changelog.md
```

---

## Retell Agent Setup

1. Create a Retell account:
   https://retellai.com

2. Create a **Single Prompt Agent**

3. Copy the `system_prompt` from:

```
outputs/accounts/{account_id}/v1/agent_spec.json
```

4. Paste the prompt into the Retell prompt editor.

5. Configure voice and publish the agent.

---

## LLM Usage

This project uses **rule-based extraction and templating** instead of paid LLM APIs.

Benefits:

* Zero cost
* Deterministic results
* Fully reproducible pipeline

---

## Automation Behavior

### Pipeline A

Demo transcript → extract information → generate **agent v1**

### Pipeline B

Onboarding transcript → update memo → generate **agent v2**

The pipeline is **idempotent**, meaning running it multiple times produces consistent results without duplicate artifacts.

---

## Technologies Used

* Python
* JSON
* Rule-based NLP extraction
* Retell AI (manual configuration)

---

## Author

Parth Hardeniya
BTech CSE – VIT Vellore
