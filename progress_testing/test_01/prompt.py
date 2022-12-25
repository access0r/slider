import os

from click import open_file
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=[input_text]
  temperature=0.9,
  max_tokens=2108,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n"],
)

def select_data_json(directory):
  json_file = open_file(os.path.join(directory, 'data.json'))
  if json_file is None:
    return None
  else:
    json_data = json.load(json_file)
    return json_data

data = select_data_json(('/path/to/dir'))
prompt = start_sequence + response['choices'][0]['text'] + restart_sequence