import boto3

s3 = boto3.resource('s3')
BUCKET = "company-data-multi-agent-debate"

client = boto3.client('bedrock-agent')
dataSourceId = "KCMQSPR11Y"
knowledgeBaseId = "DUBJRQ0WDR"

print(s3.Bucket(BUCKET).upload_file("./company_data.csv", "company_data/company_data.csv"))
print(s3.Bucket(BUCKET).upload_file("./policy/business_policy.pdf", "company_data/policy/business_policy.pdf"))
print(s3.Bucket(BUCKET).upload_file("./policy/planet_policy.pdf", "company_data/policy/planet_policy.pdf"))

# response = client.start_ingestion_job(
#     dataSourceId=dataSourceId,
#     knowledgeBaseId=knowledgeBaseId
# )

# print(response)