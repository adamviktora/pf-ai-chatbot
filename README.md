# pf-ai-chatbot
AI chatbot for PatternFly. Based on Rasa open source framework.

## How to run
### Initial setup
- create a python virtual environment: `python3 -m venv my_venv`
- start a python virtual environment: `source my_venv/bin/activate`
- install `rasa` and other necessary libraries into this virtual environment

### Start a chatbot
- go to chatbot directory: `cd chatbot`
- train a model: `rasa train`
- in a separate terminal, start actions: `rasa run actions`
- start the model `rasa shell`

## Content

- **chatbot**
  - rasa framework project
  - `domain.yml` includes list of user **intents**, chatbot **responses**, list of **actions**, **entities**, slots, forms, session_config, ...
  - `data/nlu.yml` defines user intents and examples (sentences) for each intent
  - `data/rules.yml` defines what action should the chatbot do as a reaction on an intent = strict
  - `data/stories.yml` defines what action should the chatbot do as a reaction on an intent. Can have more steps than one intent-action.
  - `actions/actions.py` defines custom actions (how to respond on intents in a more customizable way)
  - `helpers/generate_component_intents.py` creates intents based on the various components in `actions/components.json` file
- **webscraper**
  - `main.py` downloads data about PatternFly components and saves them to `chatbot/actions/components.json`
  - requires a patternfly-org website running at `localhost:8003`

