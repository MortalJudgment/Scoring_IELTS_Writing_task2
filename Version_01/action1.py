from .CoT_prompt import get_CoT_prompt_CC, get_CoT_prompt_LR, get_CoT_prompt_GR, get_CoT_prompt_TA

def get_score(question, essay, chat, criteria, criteria_item):
    """
    Scoring for a given essay based on the provided question
    Parameters:
    - essay (str): An essay to consider for generating the score.
    - question (str): The question for which the score needs to be calculated.
    - chat (obj): The large language model used for scoring. 
    Returns:
    - float: The score for the given question.
    """
    get_prompt_function = {
      'Coherence and cohesion': get_CoT_prompt_CC,
      'Lexical Resource': get_CoT_prompt_LR,
      'Grammatical Range': get_CoT_prompt_GR,
      'Task Achievement': get_CoT_prompt_TA,
    }[criteria]

  # Generate prompt based on criteria
    get_prompt = get_prompt_function(question, essay)

    scores = chat(get_prompt)

    prompt = f'''Given information {scores}.\n 
    Use information above to write scores for {criteria} and its items {criteria_item} for given {question} and {essay}. (No explanation, give score only, present smart to user easy to read). \n
    For example,
    Coherence and Cohesion: 6
        - Logical structure: 6
        - Introduction & conclusion present: 7
        - Supported main points 6
        - Accurate linking words 7
        - Variety in linking words 7
    '''
    response = chat(prompt)
    return f"{response}"
