from few_shot import FewShotsPost
from llm_helper import get_llm

llm = get_llm()
few_shot = FewShotsPost()

def get_length_str(length):
    if length == "Short":
        return "1 to 9 lines"
    if length == "Medium":
        return "10 to 15 lines"
    if length == "Long":
        return "15 to 20 lines"
    
def get_prompt(tag, length, language, creator):
    length_str = get_length_str(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.
    1. Topic: {tag}
    2. Length: {length_str}
    3. Language: {language}
    If language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
    examplePosts = few_shot.get_filtered_posts(length=length, 
                                               language=language, 
                                               tag=tag, 
                                               creator=creator)
    if len(examplePosts) > 0:
        prompt += f"4. Use the writing style of {creator} as per the following examples: "
        for i, post in enumerate(examplePosts):
            post_text = post['text']
            post_creator = post['creator']
            prompt += f"\n\n Example {i+1}: \n\n {post_text} \n\n Creator: {post_creator}"
            if i == 1:
                break
    return prompt

def generate_post(tag, length, language, creator):
    prompt = get_prompt(tag=tag, length=length, language=language, creator=creator)
    response = llm.invoke(prompt)
    return response.content