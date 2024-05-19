import priming as priming
import api as api

ERROR_MESSAGE = 'Internal error. Please try again.'

def run_simile(input, temperature):
    input = input.lower().strip()
    simile_prompt = priming.construct_prompt(
        priming.SIMILE_PROMPT_COMPONENTS,
        [input]
    )
    response = api.predict(simile_prompt, temperature)
    if "error" in response:
        return ERROR_MESSAGE
    return response
    

def run_explode(input, temperature):
    input = input.lower().strip()
    explode_prompt = priming.construct_prompt(
        priming.EXPLODE_PROMPT_COMPONENTS,
        [f'"{input}"{priming.PREFIX_DELIMITER}']
    )
    response = api.predict(explode_prompt, temperature)
    if "error" in response:
        return ERROR_MESSAGE
    return response
    

def run_unexpect(input, temperature):
    input = input.lower().strip()
    unexpect_prompt = priming.construct_prompt(
        priming.UNEXPECT_PROMPT_COMPONENTS,
        [input]
    )
    response = api.predict(unexpect_prompt, temperature)
    if "error" in response:
        return ERROR_MESSAGE
    return response
    

def run_chain(input, temperature):
    input = input.lower().strip()
    chain_prompt = priming.construct_prompt(
        priming.CHAIN_PROMPT_COMPONENTS,
        [f'"{input}"{priming.PREFIX_DELIMITER}']
    )
    response = api.predict(chain_prompt, temperature)
    if "error" in response:
        return ERROR_MESSAGE
    return response
    

def run_pov(input, temperature):
    input = input.lower().strip()
    pov_prompt = priming.construct_prompt(
        priming.POV_PROMPT_COMPONENTS,
        [f'"{input}"{priming.PREFIX_DELIMITER}']
    )
    response = api.predict(pov_prompt, temperature)
    if "error" in response:
        return ERROR_MESSAGE
    return response
    

def run_acronym(input, temperature):
    input = input.lower().strip()
    acronym_prompt = priming.construct_prompt(
        priming.ACRONYM_PROMPT_COMPONENTS,
        [f'"{input}"{priming.PREFIX_DELIMITER}']
    )
    response = api.predict(acronym_prompt, temperature)
    if "error" in response:
        return ERROR_MESSAGE
    return response
    

def run_scene(input, temperature):
    input = input.lower().strip()
    scenes_prompt = priming.construct_prompt(
        priming.SCENE_PROMPT_COMPONENTS,
        [input]
    )
    response = api.predict(scenes_prompt, temperature)
    if "error" in response:
        return ERROR_MESSAGE
    return response

def run_unfold(input, temperature):
    input = input.lower().strip()
    unfold_prompt = priming.construct_prompt(
        priming.UNFOLD_PROMPT_COMPONENTS,
        [input]
    )
    response = api.predict(unfold_prompt, temperature)
    if "error" in response:
        return ERROR_MESSAGE
    return response
    
    
# working
# 1) simile
# 2) explode
# 3) unexpected
# 4) chain
# 5) pov
# 7) scene
# 8) unfold

# not working
# 6) acronym

# out of scope
# Alliteration
# Fuse

ans = run_scene('sports car', 0.1)
print(ans)