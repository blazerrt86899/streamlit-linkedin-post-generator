import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import get_llm

llm = get_llm()

def process_posts(raw_file_path, processed_file_path="./data/processed_posts.json"):
    enriched_post = []
    with open(raw_file_path,"r", encoding="utf-8") as file:
        posts = json.load(file)
        for post in posts:
            metadata = extract_metadata(post)
            post_with_metadata = post | metadata
            enriched_post.append(post_with_metadata)
            
    unified_tags = get_unified_tags(enriched_post)
    for posts in enriched_post:
        current_tags = posts["tags"]
        new_tags = { unified_tags[tag] for tag in current_tags }
        posts['tags'] = list(new_tags)
    print(f"Enriched POSTS:-----\n {enriched_post}")
    with open(processed_file_path, "w", encoding="utf-8") as outfile:
        json.dump(enriched_post, outfile, indent=4, ensure_ascii=False)
    
def get_unified_tags(posts_with_metadata):   
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])
    unique_tags_list = ", ".join(unique_tags)
    
    print(unique_tags_list)
    
    template = '''I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unified and merged to create a shorter list.
        Example 1: "Jobseekers", "Job Hunting" can all be merged into a single tag "Job Search".
        Example 2: "Motivation", "Inspiration", "Drive" can be mapped to "Motivation".
        Example 3: "AI Agents", "Generative AI", "GenAI", "AIWorkflow" can be mapped to "Artificial Intelligence".
        Example 4: "Crew AI", "n8n", "Agentic AI", "NoCode" can be mapped to "Multi-Agent System".
        Example 5: "Marketing", "Digital Marketing", "Promotion", "Automation" can be mapped to "Automation"
    2. Each tag should follow title case convention. Example: "Motivation", "Job Search"
    3. Output should be a JSON object, No preamble.
    4. Output should have mapping of original tag and the unified tag.
        For example: {{"JobSeekers": "Job Search", "Job Hunting": "Job Search", "AI Agents": "Artificial Intelligence"}}    
    Here is the list of tags:
    {tags}
    '''
    prompt = PromptTemplate(
        template=template
    )
    chain = prompt | llm
    response = chain.invoke(input = {"tags": str(unique_tags_list)})
    
    try:
        jsonParser = JsonOutputParser()
        res = jsonParser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context is too big. Unable to parse")
    
    return res

def extract_metadata(post):
    template = '''
    You are given a LinkedIn post. You need to extract number of lines, language of the post and tags. 
    1. Return a valid json. Do not change the text. No preamble.
    2. JSON object should have exactly three keys: line_count, language and tags.
    3. tags is an array of text tags without hastags `#`. tags should be unique. Extract only two tags.
    4. Language should be English or Hinglish (Hinglish means Hindi + English).
    5. Do not make up things. If language does not have Hindi extract in it, say English.
    
    Here is the actual post on which you need to perform this task:
    {post}
    '''
    prompt = PromptTemplate.from_template(
        template=template
    )
    chain = prompt | llm
    
    response = chain.invoke(input={"post": post})
    try:
        jsonParser = JsonOutputParser()
        metadata_content = jsonParser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse.")
    
    return metadata_content

if __name__ == "__main__":
    process_posts("./data/raw_post.json", "./data/processed_posts.json")