import boto3
from botocore.client import Config
from langchain.chains import RetrievalQA
from langchain_aws import BedrockLLM
from langchain_community.retrievers import AmazonKnowledgeBasesRetriever

query = "Can I provide the incom corporation a loan of 500,000?"

retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="O9O2CCKXV4",
    retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},
)

model_kwargs_claude = {"temperature": 0, "top_k": 10, "max_tokens_to_sample": 3000}

llm = BedrockLLM(model_id="anthropic.claude-v2", model_kwargs=model_kwargs_claude)

qa = RetrievalQA.from_chain_type(
    llm=llm, retriever=retriever, return_source_documents=True
)

print(qa(query)['result'])


# bedrock_agent_runtime = boto3.client('bedrock-agent-runtime')

# def retrieveAndGenerate(input, kbId="O9O2CCKXV4"):
#     return bedrock_agent_runtime.retrieve_and_generate(
#         input={
#             'text': input
#         },
#         retrieveAndGenerateConfiguration={
#             'type': 'KNOWLEDGE_BASE',
#             'knowledgeBaseConfiguration': {
#                 'knowledgeBaseId': kbId,
#                 'modelArn': 'arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-v2'
#                 }
#             }
#         )


# print(retrieveAndGenerate("Can I loan to companies on mustafar"))