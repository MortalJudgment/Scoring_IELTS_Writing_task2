from textwrap import dedent


class ValidatePrompt():
    def Coherence_and_Cohesion(self):
        return """An essay must fully fit the positive features of the descriptor at a particular level. Bolded text (text betwenn **) indicates negative features that will limit a rating.

            Band 9: 
            The message can be followed effortlessly.
            Cohesion is used in such a way that it very rarely attracts attention.
            Any lapses in coherence or cohesion are minimal.
            Paragraphing is skilfully managed

            Band 8:
            The message can be followed with ease.
            Information and ideas are logically sequenced, and cohesion is well managed.
            Occasional lapses in coherence and cohesion may occur.
            Paragraphing is used sufficiently and appropriately.

            Band 7:
            Information and ideas are logically organised, and there is a clear progression throughout the response. (A few lapses may occur, but these are minor.)
            A range of cohesive devices including reference and substitution is used flexibly but with some inaccuracies or some over/under use.
            Paragraphing is generally used effectively to support overall coherence, and the sequencing of ideas within a paragraph is generally logical.

            Band 6:
            Information and ideas are generally arranged coherently and there is a clear overall
            progression. 
            Cohesive devices are used to some good effect but cohesion within and/or between sentences may be faulty or mechanical due to misuse, overuse or omission.
            The use of reference and substitution may lack flexibility or clarity and result in some repetition or error.
            Paragraphing may not always be logical and/or the central topic may not always be clear.

            Band 5: 
            Organisation is evident but is not wholly logical and there may be a lack of overall progression.
            Nevertheless, there is a sense of underlying coherence to the response.
            The relationship of ideas can be followed but the sentences are not fluently linked to each other.
            There may be limited/overuse of cohesive devices with some inaccuracy.
            The writing may be repetitive due to inadequate and/or inaccurate use of reference and substitution.
            **Paragraphing may be inadequate or missing**.

            Band 4:
            Information and ideas are evident but not arranged coherently and **there is no clear progression within the response**.
            **Relationships between ideas can be unclear and/or inadequately marked. There is some use of basic cohesive devices, which may be inaccurate or repetitive**.
            **There is inaccurate use or a lack of substitution or referencing**.
            **There may be no paragraphing and/or no clear main topic within paragraphs**.

            Band 3: 
            There is no apparent logical organisation. Ideas are discernible but difficult to relate to each other. There is minimal use of sequencers or cohesive devices.
            Those used do not necessarily indicate a logical relationship between ideas.
            **There is difficulty in identifying referencing**.
            **Any attempts at paragraphing are unhelpful**.

            Band 2:
            There is little relevant message, or the **entire response may be off-topic**.
            There is little evidence of control of organisational features.

            Band 1:
            **Responses of 20 words or fewer are rated at Band 1**.
            The writing fails to communicate any message and appears to be by a virtual non-writer

            Band 0: 
            Should only be used where a candidate did not attend or attempt the question in any way, used a language other than English throughout, or **where there is proof that a candidate's answer has been totally memorised**.
            """
    def Lexical_Resource(self):
        return """ An essay must fully fit the positive features of the descriptor at a particular level. Bolded text (text betwenn **) indicates negative features that will limit a rating.

            Band 9: 
            Full flexibility and precise use are widely evident.
            A wide range of vocabulary is used accurately and appropriately with very natural and sophisticated control of lexical features.
            Minor errors in spelling and word formation are extremely rare and have minimal impact on communication.

            Band 8:
            A wide resource is fluently and flexibly used to convey precise meanings.
            There is skilful use of uncommon and/or idiomatic items when appropriate, despite occasional inaccuracies in word choice and collocation.
            Occasional errors in spelling and/or word formation may occur, but have minimal impact on communication.

            Band 7:
            The resource is sufficient to allow some flexibility and precision.
            There is some ability to use less common and/or idiomatic items.
            An awareness of style and collocation is evident, though inappropriacies occur.
            There are only a few errors in spelling and/or word formation and they do not detract from overall clarity

            Band 6:
            The resource is generally adequate and appropriate for the task.
            The meaning is generally clear in spite of a rather restricted range or a lack of precision in word choice.
            If the writer is a risk-taker, there will be a wider range of vocabulary used but higher degrees of inaccuracy or inappropriacy.
            There are some errors in spelling and/or word formation, but these do not impede communication.

            Band 5: 
            The resource is limited but minimally adequate for the task.
            Simple vocabulary may be used accurately but the range does not permit much variation in expression. 
            There may be frequent lapses in the appropriacy of word choice and a lack of flexibility is apparent in frequent simplifications and/or repetitions.
            Errors in spelling and/or word formation may be noticeable and may cause some difficulty for the reader.

            Band 4:
            The resource is limited and inadequate for or **unrelated to the task**. Vocabulary is basic and may be used repetitively.
            There may be inappropriate use of lexical chunks (e.g. memorised phrases, formulaic language and/or language from the input material).
            Inappropriate word choice and/or errors in word formation and/or in spelling may impede meaning.

            Band 3: 
            The resource is inadequate (which may be due to the response being significantly underlength). Possible over-dependence on input material or memorised language.
            Control of word choice and/or spelling is very limited, and errors predominate. These errors may severely impede meaning

            Band 2:
            The resource is extremely limited with few recognisable strings, apart from memorised
            phrases.
            There is no apparent control of word formation and/or spelling.

            Band 1:
            **Responses of 20 words or fewer are rated at Band 1**.
            No resource is apparent, except for a few isolated words.

            Band 0: 
            Should only be used where a candidate did not attend or attempt the question in any way, used a language other than English throughout, or **where there is proof that a candidate's answer has been totally memorised**. 
            """
    def Grammatical_Range_and_Accuracy(self):
        return """An essay must fully fit the positive features of the descriptor at a particular level. Bolded text (text betwenn **) indicates negative features that will limit a rating.

            Band 9: 
            A wide range of structures is used with full flexibility and control.
            Punctuation and grammar are used appropriately throughout.
            Minor errors are extremely rare and have minimal impact on communication.

            Band 8:
            A wide range of structures is flexibly and accurately used.
            The majority of sentences are error-free, and punctuation is well managed.
            Occasional, non-systematic errors and inappropriacies occur, but have minimal impact on communication.

            Band 7:
            A variety of complex structures is used with some flexibility and accuracy.
            Grammar and punctuation are generally well controlled, and error-free sentences are frequent.
            A few errors in grammar may persist, but these do not impede communication.

            Band 6:
            A mix of simple and complex sentence forms is used but flexibility is limited.
            Examples of more complex structures are not marked by the same level of accuracy as in simple structures.
            Errors in grammar and punctuation occur, but rarely impede communication

            Band 5: 
            The range of structures is limited and rather repetitive.
            Although complex sentences are attempted, they tend to be faulty, and the greatest accuracy is achieved on simple sentences.
            Grammatical errors may be frequent and cause some difficulty for the reader.
            Punctuation may be faulty.

            Band 4:
            A very limited range of structures is used.
            Subordinate clauses are rare and simple sentences predominate.
            Some structures are produced accurately but grammatical errors are frequent and may impede meaning.
            Punctuation is often faulty or inadequate.

            Band 3: 
            Sentence forms are attempted, but errors in grammar and punctuation predominate (except in memorised phrases or those taken from the input material). This prevents most meaning from coming through.
            **Length may be insufficient to provide evidence of control of sentence forms**

            Band 2:
            There is little or no evidence of sentence forms (except in memorised phrases).

            Band 1:
            **Responses of 20 words or fewer are rated at Band 1**.
            No rateable language is evident.

            Band 0: 
            Should only be used where a candidate did not attend or attempt the question in any way, used a language other than English throughout, or **where there is proof that a candidate's answer has been totally memorised**. 
            """
    def Task_Response(self):
        return """An essay must fully fit the positive features of the descriptor at a particular level. Bolded text (text betwenn **) indicates negative features that will limit a rating.

            Band 9: 
            The prompt is appropriately addressed and explored in depth.
            A clear and fully developed position is presented which directly answers the question/s.
            Ideas are relevant, fully extended and well supported.
            Any lapses in content or support are extremely rare.

            Band 8:
            The prompt is appropriately and sufficiently addressed.
            A clear and well-developed position is presented in response to the question/s.
            Ideas are relevant, well extended and supported.
            There may be occasional omissions or lapses in content.

            Band 7:
            The prompt is appropriately and sufficiently addressed.
            A clear and well-developed position is presented in response to the question/s.
            Ideas are relevant, well extended and supported.
            There may be occasional omissions or lapses in content.

            Band 6:
            The main parts of the prompt are addressed (though some may be more fully covered than others). An appropriate format is used.
            A position is presented that is directly relevant to the prompt, although the conclusions drawn may be unclear, unjustified or repetitive.
            Main ideas are relevant, but some may be insufficiently developed or may lack clarity, while some supporting arguments and evidence may be less relevant or inadequate.

            Band 5: 
            The main parts of the prompt are **incompletely addressed**. The format may be inappropriate in places.
            The writer expresses a position, but the development is not always clear.
            Some main ideas are put forward, but they are limited and are not sufficiently developed and/or there may be irrelevant detail.
            There may be some repetition

            Band 4:
            The prompt is tackled in a minimal way, or the answer is tangential, possibly due to some misunderstanding of the prompt. **The format may be inappropriate**.
            A position is discernible, but the reader has to read carefully to find it.
            Main ideas are difficult to identify and such ideas that are identifiable may lack relevance, clarity and/or support.
            Large parts of the response may be repetitive.

            Band 3: 
            No part of the prompt is adequately addressed, or the prompt has been misunderstood.
            No relevant position can be identified, and/or there is little direct response to the question/s.
            There are few ideas, and these may be irrelevant or insufficiently developed.

            Band 2:
            The content is barely related to the prompt.
            No position can be identified.
            There may be glimpses of one or two ideas without development.

            Band 1:
            **Responses of 20 words or fewer are rated at Band 1**.
            **The content is wholly unrelated to the prompt**.
            Any copied rubric must be discounted

            Band 0: 
            Should only be used where a candidate did not attend or attempt the question in any way, used a language other than English throughout, or **where there is proof that a candidate's answer has been totally memorised**. 
            """


from textwrap import dedent

class ScoringPrompt():
    def Coherence_and_Cohesion(self):
        description = dedent("""\
            You are an expert in scoring and evaluating the coherence and cohesion of IELTS Writing Task 2 essays.
            Your task is to assess the essay's organization, logical flow, and use of linking words.
            You will examine the essay's structure, ensuring it has a clear introduction and conclusion, well-supported main points, accurate linking words, and a variety of linking words.
            Think step by step, and give reasoning before scoring for each step on Coherence and Cohesion sub-criteria.
            Factors contributing to a high score in this category and how to identify them in an essay.
            Sub criterias:
            - Logical structure
            - Introduction & conclusion present
            - Supported main points
            - Accurate linking words
            - Variety in linking words
            """)
        expected_output = dedent("""\
            Output Format:
            ## [\Bold] Coherence and Cohesion criteria [\Bold]
            ### Sub-criterias score:
            1. **Logical structure**:
                - Strong points: Identify reasons for strong logical structure.
                - Weak points: Identify reasons for weak logical structure.
                - Score: \{score\}
            2. **Introduction & conclusion present**:
                - Strong points: Identify reasons for strong introduction and conclusion.
                - Weak points: Identify reasons for weak introduction and conclusion.
                - Score: \{score\}
            3. **Supported main points**:
                - Strong points: Identify reasons for strong support of main points.
                - Weak points: Identify reasons for weak support of main points.
                - Score: \{score\}
            4. **Accurate linking words**:
                - Strong points: Identify reasons for accurate use of linking words.
                - Weak points: Identify reasons for inaccurate use of linking words.
                - Score: \{score\}
            5. **Variety in linking words**:
                - Strong points: Identify reasons for good variety in linking words.
                - Weak points: Identify reasons for poor variety in linking words.
                - Score: \{score\}

            ### **Coherence and Cohesion criteria OVERALL band score**: \{score\}
            """)
        
        return description + expected_output
    
    def Lexical_Resource(self):
        description = dedent("""\
            You are an expert in scoring and evaluating the lexical resource of IELTS Writing Task 2 essays.
            Your task is to assess the essay's use of vocabulary.
            You will examine the essay for varied vocabulary, accurate spelling, and word formation.
            Think step by step, and give reasoning before scoring for each step on Lexical Resource sub-criteria.
            Factors contributing to a high score in this category and how to identify them in an essay.
            Sub criterias:
            - Varied vocabulary
            - Accurate spelling & word formation
            """)
        expected_output = dedent("""\
            Output Format:
            ## [\Bold] Lexical Resource criteria [\Bold]
            ### Sub-criterias score:
            1. **Varied vocabulary**:
                - Strong points: Identify reasons for strong varied vocabulary.
                - Weak points: Identify reasons for weak varied vocabulary.
                - Score: \{score\}
            2. **Accurate spelling & word formation**:
                - Strong points: Identify reasons for accurate spelling & word formation.
                - Weak points: Identify reasons for inaccurate spelling & word formation.
                - Score: \{score\}

            ### **Lexical Resource criteria OVERALL band score**: \{score\}
            """)
        
        return description + expected_output
    
    def Grammatical_Range_and_Accuracy(self):
        description = dedent("""\
            You are an expert in scoring and evaluating the grammatical range and accuracy of IELTS Writing Task 2 essays.
            Your task is to assess the essay's use of grammar and sentence structures.
            You will examine the essay for a mix of complex and simple sentences, and clear and correct grammar.
            Think step by step, and give reasoning before scoring for each step on Grammatical Range and Accuracy sub-criteria.
            Factors contributing to a high score in this category and how to identify them in an essay.
            Sub criterias:
            - Mix of complex & simple sentences
            - Clear and correct grammar
            """)
        expected_output = dedent("""\
            Output Format:
            ## [\Bold] Grammatical Range and Accuracy criteria [\Bold]
            ### Sub-criterias score:
            1. **Mix of complex & simple sentences**:
                - Strong points: Identify reasons for strong mix of complex & simple sentences.
                - Weak points: Identify reasons for weak mix of complex & simple sentences.
                - Score: \{score\}
            2. **Clear and correct grammar**:
                - Strong points: Identify reasons for strong clear and correct grammar.
                - Weak points: Identify reasons for weak clear and correct grammar.
                - Score: \{score\}

            ### **Grammatical Range and Accuracy criteria OVERALL band score**: \{score\}
            """)
        
        return description + expected_output

    def Task_Response(self):
        description = dedent("""\
            You are an expert in scoring and evaluating the task response of IELTS Writing Task 2 essays.
            Your task is to assess the essay's response to the prompt.
            You will examine the essay for complete response, clear & comprehensive ideas, relevant & specific examples, and appropriate word count.
            Think step by step, and give reasoning before scoring for each step on Task Response sub-criteria.
            Factors contributing to a high score in this category and how to identify them in an essay.
            Sub criterias:
            - Complete response
            - Clear & comprehensive ideas
            - Relevant & specific examples
            - Appropriate word count
            """)
        expected_output = dedent("""\
            Output Format:
            ## [\Bold] Task Response criteria [\Bold]
            ### Sub-criterias score:
            1. **Complete response**:
                - Strong points: Identify reasons for strong complete response.
                - Weak points: Identify reasons for weak complete response.
                - Score: \{score\}
            2. **Clear & comprehensive ideas**:
                - Strong points: Identify reasons for strong clear & comprehensive ideas.
                - Weak points: Identify reasons for weak clear & comprehensive ideas.
                - Score: \{score\}
            3. **Relevant & specific examples**:
                - Strong points: Identify reasons for strong relevant & specific examples.
                - Weak points: Identify reasons for weak relevant & specific examples.
                - Score: \{score\}
            4. **Appropriate word count**:
                - Strong points: Identify reasons for strong appropriate word count.
                - Weak points: Identify reasons for weak appropriate word count.
                - Score: \{score\}

            ### **Task Response criteria OVERALL band score**: \{score\}
            """)
        
        return description + expected_output

class RefinedOutput():
    def Coherence_and_Cohesion(self):
        return dedent("""\
            Output Format:
            ## [\Bold] Coherence and Cohesion criteria [\Bold]
            ### Sub-criterias score:
            1. **Logical structure**: \{score\}
                - Strong points: Identify reasons for strong logical structure.
                - Weak points: Identify reasons for weak logical structure.
                - *Improvement*: 
            2. **Introduction & conclusion present**: \{score\}
                - Strong points: Identify reasons for strong introduction and conclusion.
                - Weak points: Identify reasons for weak introduction and conclusion.
                - *Improvement*: 
            3. **Supported main points**: \{score\}
                - Strong points: Identify reasons for strong support of main points.
                - Weak points: Identify reasons for weak support of main points.
                - *Improvement*: 
            4. **Accurate linking words**: \{score\}
                - Strong points: Identify reasons for accurate use of linking words.
                - Weak points: Identify reasons for inaccurate use of linking words.
            5. **Variety in linking words**: \{score\}
                - Strong points: Identify reasons for good variety in linking words.
                - Weak points: Identify reasons for poor variety in linking words.
                - *Improvement*: 

            ### **Coherence and Cohesion criteria OVERALL band score**: \{score\}
            ### Feedback:

            """)
    def Lexical_Resource(self):
        return dedent("""\
            Output Format:
            ## [\Bold] Lexical Resource criteria [\Bold]
            ### Sub-criterias score:
            1. **Varied vocabulary**: \{score\}
                - Strong points: Identify reasons for strong varied vocabulary.
                - Weak points: Identify reasons for weak varied vocabulary.
                - *Improvement*: 
            2. **Accurate spelling & word formation**: \{score\}
                - Strong points: Identify reasons for accurate spelling & word formation.
                - Weak points: Identify reasons for inaccurate spelling & word formation.
                - *Improvement*: 

            ### **Lexical Resource criteria OVERALL band score**: \{score\}
            ### Feedback:
            
            """)

    def Grammatical_Range_and_Accuracy(self):
        return dedent("""\
            Output Format:
            ## [\Bold] Grammatical Range and Accuracy criteria [\Bold]
            ### Sub-criterias score:
            1. **Mix of complex & simple sentences**: \{score\}
                - Strong points: Identify reasons for strong mix of complex & simple sentences.
                - Weak points: Identify reasons for weak mix of complex & simple sentences.
                - *Improvement*: 
            2. **Clear and correct grammar**: \{score\}
                - Strong points: Identify reasons for strong clear and correct grammar.
                - Weak points: Identify reasons for weak clear and correct grammar.
                - *Improvement*: 

            ### **Grammatical Range and Accuracy criteria OVERALL band score**: \{score\}
            ### Feedback:
            
            """)

    def Task_Response(self):
        return dedent("""\
            Output Format:
            ## [\Bold] Task Response criteria [\Bold]
            ### Sub-criterias score:
            1. **Complete response**: \{score\}
                - Strong points: Identify reasons for strong complete response.
                - Weak points: Identify reasons for weak complete response.
                - *Improvement*: 
            2. **Clear & comprehensive ideas**: \{score\}
                - Strong points: Identify reasons for strong clear & comprehensive ideas.
                - Weak points: Identify reasons for weak clear & comprehensive ideas.
                - *Improvement*: 
            3. **Relevant & specific examples**: \{score\}
                - Strong points: Identify reasons for strong relevant & specific examples.
                - Weak points: Identify reasons for weak relevant & specific examples.
                - *Improvement*: 
            4. **Appropriate word count**: \{score\}
                - Strong points: Identify reasons for strong appropriate word count.
                - Weak points: Identify reasons for weak appropriate word count.
                - *Improvement*: 

            ### **Task Response criteria OVERALL band score**: \{score\}
            ### Feedback:
            
            """)

