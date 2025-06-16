from openai import OpenAI
import os
from package.generation_util import model_generation, model_generation_v2, make_prompt, make_prompt_v2
from package.util import file_read
import argparse
from package.util import extract_python_list_from_gpt_response, make_args, save_result
from package.score_util import calculate_score

args = make_args()

prompt, instruction, survey = make_prompt_v2(args)

print(prompt)

answer = model_generation_v2(prompt, instruction, survey, args)

big5_score = calculate_score(answer,args)

save_result(big5_score, args)
