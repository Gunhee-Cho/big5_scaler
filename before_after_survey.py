from openai import OpenAI
import os
from persona_prompt import BIG5_PERSONA_PROMPT
from bf_survey_prompt import BIG5_SURVEY_PROMPT 
from util import write_memory, read_memory, gpt_generation, bert_similarity

os.environ['OPENAI_API_KEY'] = "OPENAI-KEY"
client = OpenAI()

# with open("openess_prompt.txt", 'r') as file:
#     openess_prompt = file.read()

# with open("conscientiousness_prompt.txt", 'r') as file:
#     conscientiousness_prompt = file.read()

# with open("openess_conscientiousness_prompt.txt", 'r') as file:
#     conscientiousness_prompt = file.read()

# with open("all_prompt.txt", 'r') as file:
#     all_prompt = file.read()

prompt = BIG5_PERSONA_PROMPT + '\n\n' + BIG5_SURVEY_PROMPT

answer = gpt_generation(prompt)

write_memory(answer)

memory = read_memory()
questions = [
    'Do you enjoy spending time with friends?',
    "Do you find yourself trying to understand and respect others' opinions?",
    "Do you make an effort to plan and follow schedules?",
    "Are you able to remain calm when under stress?",
    "Do you actively seek out new ideas or experiences?"
    ]

score = 0
for question in questions:
    before_survey_prompt = BIG5_PERSONA_PROMPT + '\n\n' + question
    after_survey_prompt = '#persona#' + '\n' + BIG5_PERSONA_PROMPT +'\n\n' + '#memory#' + '\n' + memory + '\n\n' + "You are an agent with this memory, and you should respond based on it." + '\n\n' + question

    before_survey_answer = gpt_generation(before_survey_prompt)
    after_survey_answer = gpt_generation(after_survey_prompt)

    print("before_survey_answer\n", before_survey_answer, "\n")
    print("after_survey_answer\n", after_survey_answer, "\n")

    bert_sim = bert_similarity(before_survey_answer, after_survey_answer)

    print(bert_sim)

    score += bert_sim

print(score/5)




