from langchain.prompts import PromptTemplate
from langchain_community.llms.ollama import Ollama


def summarize_page(page_content):
    llm = Ollama(model="mistral")
    prompt = """
    You will be given a single page of a book. This section will be enclosed in triple backticks (```)
    Your goal is to give a summary of this section so that a reader will have a full understanding of it.
    Your response should be up to three paragraphs and fully encompass what was said in the passage.

    ```{text}```
    FULL SUMMARY:
    """
    summarize_prompt = PromptTemplate(template=prompt, input_variables=["text"])
    chain = summarize_prompt | llm
    return chain.invoke({"text": page_content})
