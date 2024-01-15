from dotenv import load_dotenv
import os

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient


def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('QA_AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('QA_AI_SERVICE_KEY')
        ai_project_name = os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(ai_endpoint, credential)


        # Submit a question and display the answer
        user_question = ''
        while user_question.lower() != 'quit':
            user_question = input("\nQuestion:\n")
            response = ai_client.get_answers(question=user_question,
                                             project_name=ai_project_name,
                                             deployment_name=ai_deployment_name)
            
            for candidate in response.answers:
                print(candidate.answer)
                print("Confidence: {}".format(candidate.confidence))
                print("Source {}:".format(candidate.source))


    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()

# This works
# curl -X POST "https://aiengineerlanguageservice.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=LearnFAQ&api-version=2021-10-01&deploymentName=production" -H "Ocp-Apim-Subscription-Key: 81344f556bf548e185eec3e2101da1fc" -H "Content-Type: application/json" -d "{\"top\": 3, \"question\": \"What is a learning path?\"}"