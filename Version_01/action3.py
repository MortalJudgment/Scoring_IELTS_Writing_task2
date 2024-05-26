
def suggest_outline(chat, question, number):
    prompt = f'''question = {question}
        Above is an IELTS writing task 2 question, give me a detail outline (give example also) to get at least {number} score overall step by step.
        Note that you provide an answer to support users, so that they can write their own, not to provide a complete answer.
        '''
    return chat(prompt)
    