from textwrap import dedent
from crewai import Task
 
class Tasks():
    def scoring_IELTS(self, question, essay, agent):
        return Task(
            description=dedent(f"""\
                Given a writing Task 2 \n
                Question: {question}\n
                Essay: {essay}.\n
                Score the given IELTS essay based on its coherence and cohesion, lexical resource, grammatical range and accuracy, and task response.
                """),
            expected_output = dedent(
                """ Ouput should in format
                ## [\Bold] Coherence and Cohesion criteria [\Bold]
                ### **Coherence and Cohesion overall band score: {overall band score for Coherence and Cohesion criteria}**
                ### Sub-criterias score:
                - Logical structure: {score}. {Give short explain on strong points and weak points reasons for why you scored that score on Logical Structure.}
                - Introduction & conclusion present: {score}. {Give short explain on strong points and weak points reasons for why you scored that score on Introduction & conclusion present.}
                - Supported main points: {score}. {Give short explain on strong points and weak points reasons for why you scored that score on Supported main points.}
                - Accurate linking words: {score}. {Give short explain on strong points and weak points reasons for why you scored that score on Accurate linking words.}
                - Variety in linking words: {score}. {Give short explain on strong points and weak points reasons for why you scored that score on Variety in linking words.}
                ## [\Bold] Lexical Resource criteria [\Bold]
                ### **Lexical Resource overall band score: {overall band score for Lexical Resource criteria}**
                ### Sub-criterias score:
                - Varied vocabulary: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Varied Vocabulary.}
                - Accurate spelling & word formation: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Accurate Spelling & Word Formation.}
                ## [\Bold] Grammatical Range & Accuracy criteria [\Bold]
                ### **Grammatical Range & Accuracy overall band score: {overall band score for Grammatical Range & Accuracy criteria}**
                ### Sub-criterias score:
                - Mix of complex & simple sentences: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Mix of Complex & Simple Sentences.}
                - Clear and correct grammar: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Clear and Correct Grammar.}
                ## [\Bold] Task Response criteria [\Bold]
                ### **Task Response overall band score: {overall band score for Task Response criteria}**
                ### Sub-criterias score:
                - Complete response: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Complete Response.}
                - Clear & comprehensive ideas: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Clear & Comprehensive Ideas.}
                - Relevant & specific examples: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Relevant & Specific Examples.}
                - Appropriate word count: {Yes or No}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Appropriate Word Count.}
                
                #  [\Bold] Overall Band Score  [\Bold]: 
                """),
            async_execution=True,
            agent = agent
            )
    def scoring_CC_task(self, question, essay, agent):
        return Task(
            description=dedent(f"""\
                                Given a writing Task 2 \n
                                Question: {question}\n
                                Essay: {essay}.
                                Score the coherence and cohesion criteria of a given IELTS writing task 2 essay. And evaluate that overall band score with IELTS band descriptors.
                                """),
            expected_output = dedent(
                """ Ouput should in format
                ## [\Bold] Coherence and Cohesion criteria [\Bold]
                ### **Coherence and Cohesion overall band score: {final overall band score}**
                ### Sub-criterias score:
                - Logical structure: {score}. {Give short explain on strong points and weak points reasons for why you scored that score on Logical Structure.}
                - Introduction & conclusion present: {score}. {Give short explain on strong points and weak points reasons for why you scored that score on Introduction & conclusion present.}
                - Supported main points: {score}. {Give short explain on strong points and weak points reasons for why you scored that score on Supported main points.}
                - Accurate linking words: {score}. {Give short explain on strong points and weak points reasons for why you scored that score on Accurate linking words.}
                - Variety in linking words: {score}. {Give short explain on strong points and weak points reasons for why you scored that score on Variety in linking words.}
                """),
            async_execution=True,
            agent = agent
            )
    def scoring_LR_task(self, question, essay, agent):
        return Task(
            description=dedent(f"""\
                                Given a writing Task 2 \n
                                Question: {question}\n
                                Essay: {essay}.
                                Score the Lexical Resource criteria of a given IELTS writing task 2 essay.
                                """),
            expected_output = dedent(
                """ Ouput should in format
                ## [\Bold] Lexical Resource criteria [\Bold]
                ### **Lexical Resource overall band score: {final overall band score}**
                ### Sub-criterias score:
                - Varied vocabulary: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Varied Vocabulary.}
                - Accurate spelling & word formation: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Accurate Spelling & Word Formation.}
                """),
            async_execution=True,
            agent = agent
            )
    def scoring_GR_task(self, question, essay, agent):
        return Task(
            description=dedent(f"""\ 
                                Given a writing Task 2 \n
                                Question: {question}\n
                                Essay: {essay}.
                                Score the Grammatical Range & Accuracy criteria of a given IELTS writing task 2 essay.
                                """),
            expected_output = dedent(
                """ Ouput should in format
                ## [\Bold] Grammatical Range & Accuracy criteria [\Bold]
                ### **Grammatical Range & Accuracy overall band score: {final overall band score}**
                ### Sub-criterias score:
                - Mix of complex & simple sentences: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Mix of Complex & Simple Sentences.}
                - Clear and correct grammar: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Clear and Correct Grammar.}
                """),
            async_execution=True,
            agent = agent
            )
    def scoring_TR_task(self, question, essay, agent):
        return Task(
            description=dedent(f"""\
                                Given a writing Task 2 \n
                                Question: {question}\n
                                Essay: {essay}.
                                Score the Task Response criteria of a given IELTS writing task 2 essay.
                                """),
            expected_output = dedent(
                """ Ouput should in format
                ## [Criteria Name]: [Bold] Task Response criteria [Bold]
                ### **Task Response overall band score: {final overall band score}**
                ### Sub-criterias score:
                - Complete response: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Complete Response.}
                - Clear & comprehensive ideas: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Clear & Comprehensive Ideas.}
                - Relevant & specific examples: {score}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Relevant & Specific Examples.}
                - Appropriate word count: {Yes or No}. {Give a short explanation of strong points and weak points, and the reasons for why you scored that score on Appropriate Word Count.}
                """),
            async_execution=True,
            agent = agent
            )