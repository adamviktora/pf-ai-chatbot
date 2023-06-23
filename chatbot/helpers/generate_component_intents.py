import json


def starts_with_vowel(string):
    vowels = ('a', 'e', 'i', 'o')
    return string.lower().startswith(vowels)


def generate_examples_from_json(json_file):
    with open(json_file, 'r') as file:
        components_data = json.load(file)

    examples_string = ""

    for lowercase_component_name in components_data.keys():
        component_name = components_data[lowercase_component_name]["name"]

        for name in (lowercase_component_name, component_name):
            examples_string += \
                f"    - [{name}](component)\n" \
                f"    - What is {'an' if starts_with_vowel(name) else 'a'} [{name}](component)?\n" \
                f"    - Tell me about the [{name}](component).\n" \
                f"    - Give me details on the [{name}](component) component.\n" \
                f"    - Explain the [{name}](component) to me.\n" \
                f"    - Explain the [{name}](component) component to me.\n"

    return examples_string


def save_examples_to_nlu(examples):
    with open("../data/nlu.yml", "r") as yml_file:
        for line in yml_file:
            if line.strip() == "- intent: get_component_info":
                return

    with open("../data/nlu.yml", "a") as yml_file:
        yml_header = "\n- intent: get_component_info\n" \
                     "  examples: |\n"
        yml_file.write(yml_header)
        yml_file.write(examples)


json_file_path = '../actions/components.json'
generated_examples = generate_examples_from_json(json_file_path)
save_examples_to_nlu(generated_examples)
