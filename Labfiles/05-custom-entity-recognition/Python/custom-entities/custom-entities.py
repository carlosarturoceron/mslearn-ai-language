from dotenv import load_dotenv
import os

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('NER_AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('NER_AI_SERVICE_KEY')
        project_name = os.getenv('NER_PROJECT')
        deployment_name = os.getenv('NER_DEPLOYMENT')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(ai_endpoint, credential)


        # Read each text file in the reviews folder
        batchedDocuments = []
        articles_folder = 'ads'
        files = os.listdir(articles_folder)
        for file_name in files:
            # Read the file contents
            text = open(os.path.join(articles_folder, file_name), encoding='utf8').read()
            batchedDocuments.append(text)
            
            # Extract entities
            operation = ai_client.begin_recognize_custom_entities(
                batchedDocuments,
                project_name=project_name,
                deployment_name=deployment_name
            )

            document_results = operation.result()

            for doc, custom_entities_result in zip(files, document_results):
                print(doc)
                if custom_entities_result.kind == "CustomEntityRecognition":
                    for entity in custom_entities_result.entities:
                        print(
                            "\tEntity '{}' has category '{}' with confidence score of '{}'".format(
                                entity.text, entity.category, entity.confidence_score
                            )
                        )
                elif custom_entities_result.is_error is True:
                    print("\tError with code '{}' and message '{}'".format(
                        custom_entities_result.error.code, custom_entities_result.error.message
                        )
                    )

        
        


    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()