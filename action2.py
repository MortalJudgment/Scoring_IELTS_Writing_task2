from CoT_prompt import get_CoT_prompt_CC, get_CoT_prompt_LR, get_CoT_prompt_GR, get_CoT_prompt_TA


def example_prompt(criteria):
    if criteria == 'Coherence and cohesion':
        return '''**Coherence and Cohesion Evaluation Task for IELTS writing task 2**
**Coherence and Cohesion Score: 6**

    - Logical Structure: 7
    - Introduction & Conclusion Present: 6
    - Supported Main Points: 6
    - Accurate Linking Words: 9
    - Variety in Linking Words: 7

Feedback and improvement suggestions for each element:

**Logical structure:**
- Consider adding more nuanced and complex analysis to support each main point.
- Use transitional phrases to connect ideas between paragraphs more smoothly.

**Introduction & conclusion present:**
- Add more depth or insight to the introduction to grab the reader's attention.
- Consider summarizing the main points more effectively in the conclusion.

**Supported main points:**
- Provide more evidence or examples to strengthen the credibility of each argument.
- Consider addressing potential counterarguments to make the essay more persuasive.

**Accurate linking words:**
- Continue to use a variety of linking words and phrases to connect ideas effectively.
- Consider using more precise linking words to signal specific relationships between ideas.

**Variety in linking words:**
- Consider adding more synonyms for commonly used linking words (e.g., "furthermore," "in addition," "moreover").
- Use linking words to signal relationships between ideas, such as "however," "in contrast," or "nevertheless."

**Additional feedback:**
- The introduction could be stronger, consider adding more background information on the problem of congestion in cities and a clearer thesis statement.
- Use more specific examples to support the main points, especially in the body paragraphs.
- Consider adding more analysis and evaluation of the advantages and disadvantages, rather than just listing them.
- The conclusion could be more thought-provoking and reflective, rather than just summarizing the main points.
- Consider using more precise language and avoiding vague phrases, such as "in someway".
- Proofread the essay for grammar and punctuation errors.
'''

    elif criteria == 'Lexical Resource':
        return '''**Lexical Resource Evaluation Task for IELTS writing task 2**
**Lexical Resource Score: 6**

    - Varied Vocabulary: 6
    - Accurate Spelling & Word Formation: 6

Feedback and improvement suggestions for each element:

**Varied Vocabulary:**
- To improve vocabulary variety, try to use more precise and vivid word choices. For example, instead of "good care of them", consider "undivided attention" or "personalized care".
- Use synonyms to avoid repetition. For instance, instead of repeating "learn" and "teach", use "acquire", "absorb", or "educate".
- Incorporate more nuanced vocabulary to convey subtle shades of meaning. For example, instead of "successful in their career", consider "attain professional fulfillment" or "achieve long-term success".

**Accurate Spelling & Word Formation:**
- Proofread the essay carefully to eliminate minor errors in spelling and word formation.
- Improve sentence structure and grammar to enhance clarity and readability. For example, consider breaking up long sentences or using active voice instead of passive voice.
- Pay attention to word choice and usage. For instance, "contentions" is used in the introduction, but its meaning is not entirely clear in context. Consider rephrasing or providing more context to clarify its meaning.

**Additional feedback:**
- The essay could benefit from more nuanced and detailed explanations to support the arguments.
- Consider providing more examples and anecdotes to illustrate the points being made.
- The conclusion could be stronger, with a clearer summary of the main points and a more cohesive final thought.

**Improvement Suggestions:**
- Consider organizing the essay into clear paragraphs, with each paragraph focusing on a specific point or argument.
- Use transitional phrases and connective words to link ideas between sentences and paragraphs.
- Provide more context and background information to help readers understand the topic and its significance.
- Consider using more rhetorical devices, such as metaphors or analogies, to add depth and complexity to the writing.
'''

    elif criteria == 'Grammatical Range':
        return '''**Grammatical Range and Accuracy Evaluation Task for IELTS writing task 2**
**Grammatical Range and Accuracy Score: 4**

    - Mix of Complex & Simple Sentences: 7
    - Clear and Correct Grammar: 4

Feedback and improvement suggestions for each element:

**Mix of Complex & Simple Sentences:**
- To improve, the writer should aim to incorporate more complex sentence structures, such as compound-complex sentences, to increase the diversity of sentence structures.
- Vary sentence length and structure to maintain reader interest and create a more dynamic text.

**Clear and Correct Grammar:**
- The writer should proofread the essay more carefully to eliminate grammatical errors, including awkward phrasing, incorrect verb forms, and missing articles.
- Pay attention to sentence clarity and ensure that grammatical inaccuracies do not hinder understanding.
- Consider using a grammar and spell checker to identify errors before proofreading.

**Additional feedback:**
- The essay would benefit from more cohesive linking between paragraphs to improve overall flow and coherence.
- Some sentences are wordy or unclear; consider rewriting them for improved clarity.
- The conclusion could be stronger; consider summarizing the main points and reiterating the thesis statement.
- The essay could benefit from more nuanced and balanced discussion of the advantages and disadvantages of both methods.
- Consider providing more concrete examples and evidence to support the writer's opinion.

**Improvement Suggestions:**
- Read and analyze model essays to improve sentence structure and grammar.
- Practice writing complex sentences with subordinate clauses, relative clauses, or participial phrases.
- Focus on proofreading to eliminate grammatical errors and improve sentence clarity.
- Consider getting feedback from peers or teachers to identify areas for improvement.
- Revise and edit the essay to improve coherence, clarity, and overall effectiveness.
'''

    elif criteria == 'Task Achievement':
        return '''**Task Achievement Evaluation Task for IELTS writing task 2**
**Task Achievement: 7**

    - Complete Response: 7
    - Clear & Comprehensive Ideas: 7
    - Relevant & Specific Examples: 7
    - Appropriate Word Count: Yes

Feedback and improvement suggestions for each element:

**Complete Response:**
- The essay provides a good overview of both methods of teaching children, but could further explore potential counterarguments or limitations of each method to provide a more nuanced discussion.

**Clear & Comprehensive Ideas:**
- The essay presents clear and comprehensive ideas, but some ideas could be further developed or elaborated to provide more depth and nuance to the discussion.

**Relevant & Specific Examples:**
- The essay incorporates relevant examples to support the arguments presented, but could benefit from additional examples from different contexts or educational settings to further enrich the discussion.

**Appropriate Word Count:**
- The essay meets the word count requirement.

**Additional feedback:**
- The essay provides a good structure and clear ideas, but could benefit from more depth and nuance in the discussion.
- Consider adding more specific examples and counterarguments to strengthen the essay.
- Work on smoothing out the transition between paragraphs to enhance the overall flow of ideas.
- Consider elaborating on some ideas to provide more detailed insights into the effectiveness of each method.

**Improvement Suggestions:**
- Consider adding more depth to the discussion by exploring potential drawbacks of each approach.
- Consider smoothing out the transition between paragraphs to enhance the overall flow of ideas.
- Consider expanding on some examples to provide more detailed insights into the effectiveness of each method.
'''

    else:
        return ''
      

criteria = {
    'Coherence and cohesion': ['Logical structure', 'Introduction & conclusion present', 'Supported main points', 'Accurate linking words', 'Variety in linking words'], 
    'Lexical Resource': ['Varied vocabulary', 'Accurate spelling & word formation'], 
    'Grammatical Range': ['Mix of complex & simple sentences', 'Clear and correct grammar'], 
    'Task Achievement': ['Complete response', 'Clear & comprehensive ideas', 'Relevant & specific examples', 'Appropriate word count (yes or no)']
 }

def get_score_with_feedback(question, essay, chat, criteria, criteria_item):
    """
    Scoring for a given essay based on the provided question
    Parameters:
    - essay (str): An essay to consider for generating the score.
    - question (str): The question for which the score needs to be calculated.
    - model (obj): The large language model used for scoring. 
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
    example = example_prompt(criteria)

    prompt = f'''Given information {scores}.\n 
    Use information above to write scores for {criteria} and its items {criteria_item} for given {question} and {essay}. (No explanation). \n 
    Moreover, based on advantages and disadvantages given (do not write it again), give feedback and improvement suggestions (more clear if needed) to the essay for each elements. \n
    {example}
    '''
    response = chat(prompt)
    return f"{response}"
