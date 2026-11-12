# AI Academy Final Exercise — Student Guide, Part 2: AI agent and presentation

Nov 2, 2026 · @Matteo Bonas

## How Part 2 works

Part 2 continues the project you built in Part 1: same dataset, same repository, same cluster. It may run days after Part 1, so start with *Before Part 2* to get your environment back up. For the dataset catalogue, tool installation and troubleshooting of the base setup, see the Part 1 guide: Part 1 — Analysis and deployment.

| Task | What you deliver | Timebox |
| --- | --- | --- |
| Task 3: AI agent | Agent with tools and a trained model, shipped as a CLI and as a container, short report | 2:00–3:00 h |
| Task 4: Presentation prep | Slides or demo plan, README and design notes | 1:00–1:30 h |
| Class presentations | Your talk or live demo to peers and instructors | 10 minutes |

Nothing is graded. Your level profile from Part 1 is extended with the Part 2 skill areas, each rated Emerging, Proficient, Advanced or "not yet shown".

Task 3 ends with a short Markdown report in your own words, using the templates in the starter repository.

## Part 2 tasks

A task counts as completed when its **minimum objectives** are met; **advanced objectives** are extra credit on your profile. Unfinished work is normal: stop and tag when the timebox ends.

**Task 3: AI agent.** Build a simple agent that talks about your dataset, using the LLM endpoint and API key you are given.

- Answer simple questions about the dataset.
- Use the tools you give it to answer questions about the dataset and your Part 1 analysis.
- Use advanced tools, such as a prediction or classification model, to make predictions. Training a model on your dataset is required here; the catalogue is chosen so that training fits in under 30 minutes on a laptop CPU.
- Ship the agent as a CLI tool.
- Ship the agent as a containerised service with Docker or Kubernetes.

**Task 4: Presentation prep.** Prepare and submit your presentation material and documentation (README, design notes such as ADRs). The content is described in *The presentation* below.

**Minimum objectives:** an AI agent designed, built and deployed, with tools to interact with users and data; a clear presentation of your idea and the architectural challenges you met; critical thinking about implementation and deployment.

**Advanced objectives:** original ways for the agent to interact with data and users; sound ML practice for training, testing and serving; creative problem solving in implementation and deployment.

### What reviewers look at

| Task | Skill areas on your profile |
| --- | --- |
| Task 3 | Evaluation protocol and baseline, modelling choices, agent tools and grounding (answers traceable to data or model output), deployment |
| Task 4 | Clarity, justification of choices, ability to discusse your own code |

## The presentation

Each student gets about 10 minutes, as slides or a live technical demo, run from your own laptop with your cluster up. Cover three things:

1. Your data exploration and analysis design, and what you found.
2. Your idea and the architectural decisions you made, including the trade-offs and what you would change for production.
3. Your results and a demo of the agent.

After your talk, the instructor asks you to explain one component and to make one small change to it, live. AI help was allowed during the exercise, so this is where you show that you understand and can justify what you built. If you cannot do it yet, that skill is recorded as "not yet shown" with a suggestion on how to build it.