
from langchain.agents import tool

@tool
def compute_writing_score(task_response: float, coherence_cohesion: float, grammar_range: float, lexical_resource: float) -> float:
    """
    Computes the Writing Task 2 score based on scores in four categories,
    with all categories weighted equally and rounding up at 0.5.

    Args:
        task_response (float): Score for Task Response (0-9)
        coherence_cohesion (float): Score for Coherence and Cohesion (0-9)
        grammar_range (float): Score for Grammar and Range (0-9)
        lexical_resource (float): Score for Lexical Resource (0-9)

    Returns:
        float: Overall Writing Task 2 score (0-9)
    """
    # Input validation
    if not all(0 <= score <= 9 for score in [task_response, coherence_cohesion, grammar_range, lexical_resource]):
        raise ValueError("Scores must be between 0 and 9")

    # Calculate the average score
    average_score = (task_response + coherence_cohesion + grammar_range + lexical_resource) / 4
    
    # Compute the integer part and the decimal part
    int_part = int(average_score)
    decimal_part = average_score - int_part
    
    # Rounding procedure
    if decimal_part < 0.25: # Round down to the preceding integer
        rounded_score = int_part
    elif decimal_part < 0.75: # Round to 0.5
        rounded_score = int_part + 0.5
    else: # Round up to the next integer
        rounded_score = int_part + 1
    
    return rounded_score
