# Classifying Images

## Azure AI Custom Vision 

Enables you to build your own computer vision models for image classification or object detection.

Creating an Azure AI Custom Vision solution involves two tasks:

* Use existing (labeled) images to train an Azure AI Custom Vision model.

* Create a client application that submits new images to your model to generate predictions.

To use the Azure AI Custom Vision service, you must provision two kinds of Azure resource:

1. A training resource (used to train your models). This can be:
    
    * An Azure AI Services resource.
    
    * An Azure AI Custom Vision (Training) resource.

2. A prediction resource, used by client applications to get predictions from your model. This can be:

    *An Azure AI Services resource.

    *An Azure AI Custom Vision (Prediction) resource.
    
You can use a single Azure AI Services resource for both training and prediction, and you can mix-and-match resource types (for example, using an Azure AI Custom Vision (Training) resource to train a model that you then publish using an Azure AI Services resource).

## Understand image classification

Image classification is a computer vision technique in which a model is trained to predict a class label for an image based on its contents. Usually, the class label relates to the main subject of the image.

For example, the following images have been classified based on the type of fruit they contain.

Images of fruit, classified as Apple, Banana, and Orange

Models can be trained for multiclass classification (in other words, there are multiple classes, but each image can belong to only one class) or multilabel classification (in other words, an image might be associated with multiple labels).

## Train an Image Classification Model

To train an image classification model with the Azure AI Custom Vision service, you can use the Azure AI Custom Vision portal, the Azure AI Custom Vision REST API or SDK, or a combination of both approaches.

In most cases, you'll typically use the Azure AI Custom Vision portal to train your model.

The Azure AI Custom Vision portal

The portal provides a graphical interface that you can use to:

    
    1. Create an image classification project for your model and associate it with a training resource.
    
    2. Upload images, assigning class label tags to them.
    
    3. Review and edit tagged images.
    
    4. Train and evaluate a classification model.
    
    5. Test a trained model.
    
    6. Publish a trained model to a prediction resource.
    
**`The REST API and SDKs enable you to perform the same tasks by writing code, which is useful if you need to automate model training and publishing as part of a DevOps process.`**

## Detect Objects (Azure AI Custom Vision)
---

Object detection is used to locate and identify objects in images. You can use Azure AI Custom Vision to train a model to detect specific classes of object in images.

Learning objectives

After completing this module, you will be able to:


    * Provision Azure resources for Azure AI Custom Vision

    * Understand object detection

    * Train an object detector

    * Consider options for labeling images

There are two components to an object detection prediction:


    * The class label of each object detected in the image. For example, you might ascertain that an image contains one apple and two oranges.

    * The location of each object within the image, indicated as coordinates of a bounding box that encloses the object.

You can use the Azure AI Custom Vision service to train an object detection model. To use the Azure AI Custom Vision service, you must provision two kinds of Azure resource:

* A training resource (used to train your models). This can be:
    * An Azure AI Services resource.
    * An Azure AI Custom Vision (Training) resource.

A prediction resource, used by client applications to get predictions from your model. This can be:
    * An Azure AI Services resource.
    * An Azure AI Custom Vision (Prediction) resource.

**`You can use a single Azure AI Services resource for both training and prediction, and you can mix-and-match resource types (for example, using an Azure AI Custom Vision (Training) resource to train a model that you then publish using an Azure AI Services resource).`**

### Train an object detector

To train an object detection model, you can use the Azure AI Custom Vision portal to upload and label images before training, evaluating, testing, and publishing the model; or you can use the REST API or SDK to write code that performs the training tasks.

The most significant difference between training an image classification model and training an object detection model is the labeling of the images with tags. While image classification requires one or more tags that apply to the whole image, object detection requires that each label consists of a tag and a region that defines the bounding box for each object in an image. The Azure AI Custom Vision portal provides a graphical interface that you can use to label your training images.

# Detect, Analyze and Recognize Faces
---

Face detection, analysis, and recognition are all common computer vision challenges for AI systems. The ability to detect when a person is present, identify a person's facial location, or recognize an individual based on their facial features is a key way in which AI systems can exhibit human-like behavior and build empathy with users.

In this module, you'll learn how to detect, analyze, and recognize faces using Azure AI Services.

After completing this module, you’ll be able to:


    * Identify options for face detection analysis.

    * Describe considerations for face analysis.

    * Detect faces with the Azure AI Vision service.

    * Describe the capabilities of the Face service.

    * Learn about facial recognition.

## There are two Azure AI services that you can use to build solutions that detect faces or people in images.

The Azure AI Vision and Face services offer facial analysis capabilities

The Azure AI Vision service

    * The Azure AI Vision service enables you to detect people in an image, as well as returning a bounding box for its location.

The Face service
The Face service offers more comprehensive facial analysis capabilities than the Azure AI Vision service, including:
 
    * Face detection (with bounding box).
 
    * Comprehensive facial feature analysis (including head pose, presence of spectacles, blur, facial landmarks, occlusion and others).
 
    * Face comparison and verification.
 
    * Facial recognition.

While all applications of artificial intelligence require considerations for responsible and ethical use, system that rely on facial data can be particularly problematic.

When building a solution that uses facial data, considerations include (but are not limited to):

    * Data privacy and security. Facial data is personally identifiable, and should be considered sensitive and private. You should ensure that you have implemented adequate protection for facial data used for model training and inferencing.

    * Transparency. Ensure that users are informed about how their facial data will be used, and who will have access to it.

    * Fairness and inclusiveness. Ensure that you face-based system cannot be used in a manner that is prejudicial to individuals based on their appearance, or to unfairly target individuals.

## The Face Service

The Face service provides functionality that you can use for:


    * Face detection - for each detected face, the results include an ID that identifies the face and the bounding box coordinates indicating its location in the image.

    * Face attribute analysis - you can return a wide range of facial attributes, including:

    * Head pose (pitch, roll, and yaw orientation in 3D space)

    * Glasses (NoGlasses, ReadingGlasses, Sunglasses, or Swimming Goggles)

    * Blur (low, medium, or high)

    * Exposure (underExposure, goodExposure, or overExposure)

    * Noise (visual noise in the image)

    * Occlusion (objects obscuring the face)

    * Accessories (glasses, headwear, mask)

    * QualityForRecognition (low, medium, or high)

    * Facial landmark location - coordinates for key landmarks in relation to facial features (for example, eye corners, pupils, tip of nose, and so on)

    * Face comparison - you can compare faces across multiple images for similarity (to find individuals with similar facial features) and verification (to determine that a face in one image is the same person as a face in another image)

    * Facial recognition - you can train a model with a collection of faces belonging to specific individuals, and use the model to identify those people in new images.

    * Facial liveness - liveness can be used to determine if the input video is a real stream or a fake to prevent bad intentioned individuals from spoofing the recognition system.

**`You can provision Face as a single-service resource, or you can use the Face API in a multi-service Azure AI Services resource.`**

## Compare and match detected faces

When a face is detected by the Face service, an ID is assigned to it and retained in the service resource for 24 hours. The ID is a GUID, with no indication of the individual's identity other than their facial features.

While the detected face ID is cached, subsequent images can be used to compare the new faces to the cached identity and determine if they are similar (in other words, they share similar facial features) or to verify that the same person appears in two images.

This ability to compare faces anonymously can be useful in systems where it's important to confirm that the same person is present on two occasions, without the need to know the actual identity of the person. For example, by taking images of people as they enter and leave a secured space to verify that everyone who entered leaves.

## Implement facial recognition

For scenarios where you need to positively identify individuals, you can train a facial recognition model using face images.

As mentioned in the previous unit, recognition models will require getting approved through a Limited Access policy.

To train a facial recognition model with the Face service:
    
    * Create a Person Group that defines the set of individuals you want to identify (for example, employees).
    
    * Add a Person to the Person Group for each individual you want to identify.
    
    * Add detected faces from multiple images to each person, preferably in various poses. The IDs of these faces will no longer expire after 24 hours (so they're now referred to as persisted faces).
    
    * Train the model.

The trained model is stored in your Face (or Azure AI Services) resource, and can be used by client applications to:

    
    * Identify individuals in images.
    
    * Verify the identity of a detected face.
    
    * Analyze new images to find faces that are similar to a known, persisted face.

Now that you've completed this module, you can:

    
    * Identify options for face detection analysis.
    
    * Describe considerations for face analysis.
    
    * Detect people with the Azure AI Vision service.
    
    * Describe the capabilities of the Face service.
    
    * Understand facial recognition.

# Read text in images and documents with Azure AI Vision Service

Suppose you are given thousands of images and asked to transfer the text on the images to a computer database. The scanned images have text organized in different formats and contain multiple languages. What are some ways you could complete the project in a reasonable time frame and make sure the data is entered with a high degree of accuracy?

Companies around the world are tackling similar scenarios every day. Without AI services, it would be challenging to complete the project, especially if it were to change in scale.

Using AI services, we can treat this project as an Azure AI Vision scenario and apply Optical Character Recognition (OCR). OCR allows you to extract text from images, such as photos of street signs and products, as well as from documents — such as handwritten or unstructured documents.

To build an automated AI solution, you need to train machine learning models to cover many use cases. Azure AI Vision service gives access to advanced algorithms for processing images and returns data to secure storage.

In this module, you'll learn how to:

    * Identify how the Azure AI Vision service enables you to read text from images
    * Use the Azure AI Vision service with SDKs and the REST API
    * Develop an application that can read printed and handwritten text

Azure AI provides two different features that read text from documents and images, one in the Azure AI Vision Service, the other in Azure AI Document Intelligence. There is overlap in what each service provides, however each is optimized for results depending on what the input is.

Image Analysis Optical character recognition (OCR):
    
    * Use this feature for general, unstructured documents with smaller amount of text, or images that contain text.
    
    * Results are returned immediately (synchronous) from a single API call.
    
    * Has functionality for analyzing images past extracting text, including object detection, describing or categorizing an image, generating smart-cropped thumbnails and more.
    
    * Examples include: street signs, handwritten notes, and store signs.

Document Intelligence:
    
    * Use this service to read small to large volumes of text from images and PDF documents.
    
    * This service uses context and structure of the document to improve accuracy.
    
    * The initial function call returns an asynchronous operation ID, which must be used in a subsequent call to retrieve the results.
    
    * Examples include: receipts, articles, and invoices.
    
You can access both technologies via the REST API or a client library. In this module, we'll focus on the OCR feature in Image Analysis. If you'd like to learn more about Document Intelligence, reading this module will provide a good introduction.

# Azure AI Video Indexer
---

Azure Video Indexer is a service to extract insights from video, including face identification, text recognition, object labels, scene segmentations, and more.

It's increasingly common for organizations and individuals to generate content in video format. For example, you might use a cellphone to capture a live event, or you might record a teleconference that combines webcam footage and presentation of slides or documents. As a result, a great deal of information is encapsulated in video files, and you may need to extract this information for analysis or to support indexing for searchability.

In this module, you will learn how to use the Azure Video Indexer service to analyze videos.

After completing this module, you’ll be able to:

    * Describe Azure Video Indexer capabilities.
    
    * Extract custom insights.
    
    * Use Azure Video Indexer widgets and APIs.

## Capabilities

The Azure Video Indexer service is designed to help you extract information from videos. It provides functionality that you can use for:
    
    * Facial recognition - detecting the presence of individual people in the image. This requires Limited Access approval.
    
    * Optical character recognition - reading text in the video.
    
    * Speech transcription - creating a text transcript of spoken dialog in the video.
    
    * Topics - identification of key topics discussed in the video.
    
    * Sentiment - analysis of how positive or negative segments within the video are.
    
    * Labels - label tags that identify key objects or themes throughout the video.
    
    * Content moderation - detection of adult or violent themes in the video.
    
    * Scene segmentation - a breakdown of the video into its constituent scenes.

**`The Video Analyzer service provides a portal website that you can use to upload, view, and analyze videos interactively.`**

## Usage

While you can perform all video analysis tasks in the Azure Video Indexer portal, you may want to incorporate the service into custom applications. There are two ways you can accomplish this.

1. Azure Video Indexer widgets

The widgets used in the Azure Video Indexer portal to play, analyze, and edit videos can be embedded in your own custom HTML interfaces. You can use this technique to share insights from specific videos with others without giving them full access to your account in the Azure Video Indexer portal.

Video Analyzer widgets in a custom web page

2. Azure Video Indexer API

Azure Video Indexer provides a REST API that you can use to obtain information about your account, including an access token.

HTTP
`https://api.videoindexer.ai/Auth/<location>/Accounts/<accountId>/AccessToken`

You can then use your token to consume the REST API and automate video indexing tasks, creating projects, retrieving insights, and creating or deleting custom models.

For example, a GET call to 
`https://api.videoindexer.ai/<location>/Accounts/<accountId>/Customization/CustomLogos/Logos/<logoId>?<accessToken> `
REST endpoint returns the specified logo. In another example, you can send a GET request to 
`https://api.videoindexer.ai/<location>/Accounts/<accountId>/Videos?<accessToken>`, which returns details of videos in your account, similar to the following JSON example:

JSON:

```python
{
    "accountId": "SampleAccountId",
    "id": "30e66ec1b1",
    "partition": null,
    "externalId": null,
    "metadata": null,
    "name": "test3",
    "description": null,
    "created": "2018-04-25T16=50=00.967+00=00",
    "lastModified": "2018-04-25T16=58=13.409+00=00",
    "lastIndexed": "2018-04-25T16=50=12.991+00=00",
    "privacyMode": "Private",
    "userName": "SampleUserName",
    "isOwned": true,
    "isBase": true,
    "state": "Processing",
    "processingProgress": "",
    "durationInSeconds": 13,
    "thumbnailVideoId": "30e66ec1b1",
    "thumbnailId": "55848b7b-8be7-4285-893e-cdc366e09133",
    "social": {
        "likedByUser": false,
        "likes": 0,
        "views": 0
    },
    "searchMatches": [],
    "indexingPreset": "Default",
    "streamingPreset": "Default",
    "sourceLanguage": "en-US"
}
```

Deploy with ARM template

Azure Resource Manager (ARM) templates are available to create the Azure AI Video Indexer resource in your subscription, based on the parameters specified in the template file.

For a full list of available APIs, see the Video Indexer Developer Portal.

## Results

Timeline pane now includes:
    
    * Transcript of audio narration.
    
    * Text visible in the video.
    
    * Indications of speakers who appear in the video. Some well-known people are automatically recognized by name, others are indicated by number (for example Speaker #1).

# Analyze Text with Azure AI Language (https://learn.microsoft.com/en-us/azure/ai-services/language-service/overview)

https://language.azure.com/
https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/01-analyze-text.html
---

Every day, the world generates a vast quantity of data; much of it text-based in the form of emails, social media posts, online reviews, business documents, and more. Artificial intelligence techniques that apply statistical and semantic models enable you to create applications that extract meaning and insights from this text-based data.

The Azure AI Language provides an API for common text analysis techniques that you can easily integrate into your own application code.

In this module, you will learn how to use Azure AI Language to:


    * Detect language from text.

    * Analyze text sentiment.

    * Extract key phrases, entities, and linked entities.

## Azure AI Language Resource

Azure AI Language is designed to help you extract information from text. It provides functionality that you can use for:

* maximum size that can be analyzed is 5,120 characters


    * Language detection - determining the language in which text is written.

    * Key phrase extraction - identifying important words and phrases in the text that indicate the main points.
 
    * Sentiment analysis - quantifying how positive or negative the text is.
 
    * Named entity recognition - detecting references to entities, including people, locations, time periods, organizations, and more.
    Person, Location, DateTime, Organization, Address, Email, URL.
 
    * Entity linking - identifying specific entities by providing reference links to Wikipedia articles.

    * Summarization - Summarization is available for both documents and conversations, and will summarize the text into key sentences that are predicted to encapsulate the input's meaning.

    * Personally identifiable information (PII) detection - PII detection allows you to identify, categorize, and redact information that could be considered sensitive, such as email addresses, home addresses, IP addresses, names, and protected health information. For example, if the text "email@contoso.com" was included in the query, the entire email address can be identified and redacted.

    * Learned features - Learned features require you to label data, train, and deploy your model to make it available to use in your application. These features allow you to customize what information is predicted or extracted.

    * Conversational language understanding (CLU) - CLU is one of the core custom features offered by Azure AI Language. CLU helps users to build custom natural language understanding models to predict overall intent and extract important information from incoming utterances. CLU does require data to be tagged by the user to teach it how to predict intents and entities accurately.
    
    * Custom named entity recognition -Custom entity recognition takes custom labeled data and extracts specified entities from unstructured text. For example, if you have various contract documents that you want to extract involved parties from, you can train a model to recognize how to predict them.
    
    * Custom text classification- Custom text classification enables users to classify text or documents as custom defined groups. For example, you can train a model to look at news articles and identify the category they should fall into, such as News or Entertainment.

    * Question answering - Question answering is a mostly pre-configured feature that provides answers to questions provided as input. The data to answer these questions comes from documents like FAQs or manuals.

    For example, say you want to make a virtual chat assistant on your company website to answer common questions. You could use a company FAQ as the input document to create the question and answer pairs. Once deployed, your chat assistant can pass input questions to the service, and get the answers as a result.


Entity Linkinh Example.

API CALL

```
{
  "kind": "EntityLinking",
  "parameters": {
    "modelVersion": "latest"
  },
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "language": "en",
        "text": "I saw Venus shining in the sky"
      }
    ]
  }
}
```

Response

```
{
  "kind": "EntityLinkingResults",
  "results": {
    "documents": [
      {
        "id": "1",
        "entities": [
          {
            "bingId": "89253af3-5b63-e620-9227-f839138139f6",
            "name": "Venus",
            "matches": [
              {
                "text": "Venus",
                "offset": 6,
                "length": 5,
                "confidenceScore": 0.01
              }
            ],
            "language": "en",
            "id": "Venus",
            "url": "https://en.wikipedia.org/wiki/Venus",
            "dataSource": "Wikipedia"
          }
        ],
        "warnings": []
      }
    ],
    "errors": [],
    "modelVersion": "2021-06-01"
  }
}
```

## Question Answering (https://language.azure.com/)

https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/02-qna.html

The question answering capability of the Azure AI Language service makes it easy to build applications in which users ask questions using natural language and receive appropriate answers.

After completing this module, you will be able to:


    * Understand question answering and how it compares to language understanding

    * Create, test, publish and consume a knowledge base

    * Implement multi-turn conversation and active learning

    * Create a question answering bot to interact with using natural language

A common pattern for "intelligent" applications is to enable users to ask questions using natural language, and receive appropriate answers. In effect, this kind of solution brings conversational intelligence to a traditional frequently asked questions (FAQ) publication. In this module, you will learn how to use Azure AI Language to create a knowledge base of question and answer pairs that can support an application or bot.

After completing this module, you’ll be able to:


    * Understand question answering and how it compares to language understanding.

    * Create, test, publish and consume a knowledge base.

    * Implement multi-turn conversation and active learning.

    * Create a question answering bot to interact with using natural language.

## How it works?

Azure AI Language includes a question answering capability, which enables you to define a knowledge base of question and answer pairs that can be queried using natural language input. The knowledge base can be published to a REST endpoint and consumed by client applications, commonly bots.

The knowledge base can be created from existing sources, including:

    
    * Web sites containing frequently asked question (FAQ) documentation.
    
    * Files containing structured text, such as brochures or user guides.
    
    * Built-in chit chat question and answer pairs that encapsulate common conversational exchanges.

Question answering vs Conversational AI?

|                       | Question answering                                            | Language understanding                                        |
|-----------------------|--------------------------------------------------------------|----------------------------------------------------------------|
| **Usage pattern**     | User submits a question, expecting an answer                | User submits an utterance, expecting an appropriate response or action  |
| **Query processing**  | Service uses natural language understanding to match the question to an answer in the knowledge base | Service uses natural language understanding to interpret the utterance, match it to an intent, and identify entities  |
| **Response**          | Response is a static answer to a known question             | Response indicates the most likely intent and referenced entities |
| **Client logic**      | Client application typically presents the answer to the user | Client application is responsible for performing appropriate action based on the detected intent |

* The two services are in fact complementary. You can build comprehensive natural language solutions that combine language understanding models and question answering knowledge bases.

Create a Knowledge Base

In Language Studio, select your Azure AI Language resource and create a Custom question answering project.

Add one or more data sources to populate the knowledge base:

    
    * URLs for web pages containing FAQs.
    
    * Files containing structured text from which questions and answers can be derived.
    
    * Predefined chit-chat datasets that include common conversational questions and responses in a specified style.
    
    * Edit question and answer pairs in the portal.

Implement multi-turn conversation

    * Although you can often create an effective knowledge base that consists of individual question and answer pairs, sometimes you might need to ask follow-up questions to elicit more information from a user before presenting a definitive answer. This kind of interaction is referred to as a multi-turn conversation.

You can enable multi-turn responses when importing questions and answers from an existing web page or document based on its structure, or you can explicitly define follow-up prompts and responses for existing question and answer pairs.

For example, suppose an initial question for a travel booking knowledge base is "How can I cancel a reservation?". A reservation might refer to a hotel or a flight, so a follow-up prompt is required to clarify this detail. The answer might consist of text such as "Cancellation policies depend on the type of reservation" and include follow-up prompts with links to answers about canceling flights and canceling hotels.

When you define a follow-up prompt for multi-turn conversation, you can link to an existing answer in the knowledge base or define a new answer specifically for the follow-up. You can also restrict the linked answer so that it is only ever displayed in the context of the multi-turn conversation initiated by the original question.

You can create a knowledge base from scratch, but it’s common to start by importing questions and answers from an existing FAQ page or document. 

In this case, you’ll import data from an existing FAQ web page for Microsoft learn, and you’ll also import some pre-defined “chit chat” questions and answers to support common conversational exchanges.

### Build a Natural Language Understanding Model
[exercise]https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/03-language-understanding.html

[prebuilt entities](https://learn.microsoft.com/en-us/azure/ai-services/language-service/conversational-language-understanding/prebuilt-component-reference)

The Azure AI Language conversational language understanding service (CLU) enables you to train a model that apps can use to extract meaning from natural language.

Learning objectives

    * Provision Azure resources for Azure AI Language resource
    
    * Define intents, utterances, and entities
    
    * Use patterns to differentiate similar utterances
    
    * Use pre-built entity components
    
    * Train, test, publish, and review an Azure AI Language model

#### Desing Pattern

In this design pattern:

    * An app accepts natural language input from a user.
    
    * A language model is used to determine semantic meaning (the user's intent).
    
    * The app performs an appropriate action.

Utterances are the phrases that a user might enter when interacting with an application that uses your language model. 
An intent represents a task or action the user wants to perform, or more simply the meaning of an utterance. You create a model by defining intents and associating them with one or more utterances.
Entities are used to add specific context to intents. For example, you might define a TurnOnDevice intent that can be applied to multiple devices, and use entities to define the different devices.

Learned entities are the most flexible kind of entity, and should be used in most cases. You define a learned component with a suitable name, and then associate words or phrases with it in training utterances. When you train your model, it learns to match the appropriate elements in the utterances with the entity.
List entities are useful when you need an entity with a specific set of possible values - for example, days of the week. You can include synonyms in a list entity definition, so you could define a DayOfWeek entity that includes the values "Sunday", "Monday", "Tuesday", and so on; each with synonyms like "Sun", "Mon", "Tue", and so on.
Prebuilt entities are useful for common types such as numbers, datetimes, and names. For example, when prebuilt components are added, you will automatically detect values such as "6" or organizations such as "Microsoft". You can see this article for a list of supported prebuilt entities.

Guidelines in mind:

Capture multiple different examples, or alternative ways of saying the same thing
    
    * Vary the length of the utterances from short, to medium, to long
    
    * Vary the location of the noun or subject of the utterance. Place it at the beginning, the end, or somewhere in between

Use correct grammar and incorrect grammar in different utterances to offer good training data examples

The precision, consistency and completeness of your labeled data are key factors to determining model performance.
    
    * Label precisely: Label each entity to its right type always. Only include what you want extracted, avoid unnecessary data in your labels.
    
    * Label consistently: The same entity should have the same label across all the utterances.
    
    * Label completely: Label all the instances of the entity in all your utterances.

For example, consider the following list of intents and associated utterances:

GetTime:
    
    * "What time is it?"
    
    * "What is the time?"
    
    * "Tell me the time"

GetWeather:
    
    * "What is the weather forecast?"
    
    * "Do I need an umbrella?"
    
    * "Will it snow?"
    
    * TurnOnDevice
    
    * "Turn the light on."
    
    * "Switch on the light."
    
    * "Turn on the fan"

None:
    
    * "Hello"
    
    * "Goodbye"

Examples:

| Utterance                             | Intent         | Entities                           |
|----------------------------------------|----------------|------------------------------------|
| What is the time?                      | GetTime        |                                    |
| What time is it in London?             | GetTime        | Location (London)                  |
| What's the weather forecast for Paris?  | GetWeather     | Location (Paris)                   |
| Will I need an umbrella tonight?       | GetWeather     | Time (tonight)                     |
| What's the forecast for Seattle tomorrow?| GetWeather   | Location (Seattle), Time (tomorrow)|
| Turn the light on.                     | TurnOnDevice   | Device (light)                     |
| Switch on the fan.                      | TurnOnDevice   | Device (fan)                       |

In some cases, a model might contain multiple intents for which utterances are likely to be similar. You can use the pattern of utterances to disambiguate the intents while minimizing the number of sample utterances.

For example, consider the following utterances:

    * "Turn on the kitchen light"
    
    * "Is the kitchen light on?"
    
    * "Turn off the kitchen light"

These utterances are syntactically similar, with only a few differences in words or punctuation. However, they represent three different intents (which could be named TurnOnDevice, GetDeviceStatus, and TurnOffDevice). Additionally, the intents could apply to a wide range of entity values. In addition to "kitchen light", the intent could apply to "living room light", television", or any other device that the model might need to support.

To correctly train your model, provide a handful of examples of each intent that specify the different formats of utterances.

TurnOnDevice:
    
    * "Turn on the {DeviceName}"
    
    * "Switch on the {DeviceName}"
    
    * "Turn the {DeviceName} on"

GetDeviceStatus:

    * "Is the {DeviceName} on[?]"

TurnOffDevice:

    * "Turn the {DeviceName} off"

    * "Switch off the {DeviceName}"

    * "Turn off the {DeviceName}"

When you teach your model with each different type of utterance, the Azure AI Language service can learn how to categorize intents correctly based off format and punctuation.

Note: The logic in the application is deliberately simple, and has a number of limitations. For example, when getting the time, only a restricted set of cities is supported and daylight savings time is ignored. The goal is to see an example of a typical pattern for using Language Service in which your application must:

Connect to a prediction endpoint.
Submit an utterance to get a prediction.
Implement logic to respond appropriately to the predicted intent and entities.

## Create a custom text classification solution (https://learn.microsoft.com/en-us/training/modules/custom-text-classification/2-understand-types-of-classification-projects)

The Azure AI Language service enables processing of natural language to use in your own app. Learn how to build a custom text classification project.

Learning objectives:

After completing this module, you'll be able to:
    
    * Understand types of classification projects
    
    * Build a custom text classification project
    
    * Tag data, train, and deploy a model
    
    * Submit classification tasks from your own app

Natural language processing (NLP) is one of the most common AI problems, where software must interpret text or speech in the natural form that humans use. Part of NLP is the ability to classify text, and Azure provides ways to classify text including sentiment, language, and custom categories defined by the user.

In this module, you'll learn how to use the Azure AI Language service to classify text into custom groups.

After completing this module, you'll be able to:

    
    * Understand types of classification projects:
        
        * Single label classification - you can assign only one class to each file. Following the above example, a video game summary could only be classified as "Adventure" or "Strategy".
        
        * Multiple label classification - you can assign multiple classes to each file. This type of project would allow you to classify a video game summary as "Adventure" or "Adventure and Strategy".
    
    * Build a custom text classification project.
    
    * Tag data, train, and deploy a model.
    
    * Submit classification tasks from your own app.

Labeling data
In single label projects, each file is assigned one class during the labeling process; class assignment in Azure AI Language only allows you to select one class.

When labeling multiple label projects, you can assign as many classes that you want per file. The impact of the added complexity means your data has to remain clear and provide a good distribution of possible inputs for your model to learn from.

Conceptual diagram that shows mapping of documents to labels for single label and multiple label classifications.

Labeling data correctly, especially for multiple label projects, is directly correlated with how well your model performs. The higher the quality, clarity, and variation of your data set is, the more accurate your model will be.

Evaluating and improving your model

Measuring predictive performance of your model goes beyond how many predictions were correct. Correct classifications are when the actual label is x and the model predicts a label x. In the real world, documents result in different kinds of errors when a classification isn't correct:

False positive - model predicts x, but the file isn't labeled x.
False negative - model doesn't predict label x, but the file in fact is labeled x.
These metrics are translated into three measures provided by Azure AI Language:

Recall - Of all the actual labels, how many were identified; the ratio of true positives to all that was labeled.
Precision - How many of the predicted labels are correct; the ratio of true positives to all identified positives.
F1 Score - A function of recall and precision, intended to provide a single score to maximize for a balance of each component

With a single label project, you can identify which classes aren't classified as well as others and find more quality data to use in training your model. For multiple label projects, figuring out quality data becomes more complex due to the matrix of possible permutations of combined labels.

For example, let's your model is correctly classifying "Action" games and some "Action and Strategy" games, but failing at "Strategy" games. To improve your model, you'll want to find more high quality and varied summaries for both "Action and Strategy" games, as well at "Strategy" games to teach your model how to differentiate the two. This challenge increases exponentially with more possible classes your model is classifying into.

Was getting a 503 CORS not enabled issue and solved it by adding language studio base url to the blob storage

Headers:

```
Accept,Authorization,Beare,Referer,Sec-Ch-Ua,Sec-Ch-Ua-Mobile,Sec-Ch-Ua-Platform,Skip-Throttling,User-Agent,User-Session-Id,X-Ms-Blob-Type,X-Ms-Version 
```

## Custom Named Entity Recognition (CUSTOM NER)

Creating an entity extraction model typically follows a similar path to most Azure AI Language service features:

    * Define entities: Understanding the data and entities you want to identify, and try to make them as clear as possible. For example, defining exactly which parts of a bank statement you want to extract.

    * Tag data: Label, or tag, your existing data, specifying what text in your dataset corresponds to which entity. This step is important to do accurately and completely, as any wrong or missed labels will reduce the effectiveness of the trained model. A good variation of possible input documents is useful. For example, label bank name, customer name, customer address, specific loan or account terms, loan or account amount, and account number.

    * Train model: Train your model once your entities are labeled. Training teaches your model how to recognize the entities you label.

    * View model: After your model is trained, view the results of the model. This page includes a score of 0 to 1 that is based on the precision and recall of the data tested. You can see which entities worked well (such as customer name) and which entities need improvement (such as account number).

    * Improve model: Improve your model by seeing which entities failed to be identified, and which entities were incorrectly extracted. Find out what data needs to be added to your model's training to improve performance. This page shows you how entities failed, and which entities (such as account number) need to be differentiated from other similar entities (such as loan amount).

    * Deploy model: Once your model performs as desired, deploy your model to make it available via the API. In our example, you can send to requests to the model when it's deployed to extract bank statement entities.

    * Extract entities: Use your model for extracting entities. The lab covers how to use the API, and you can view the API reference for more details.

## Translate Text

There are many commonly used languages throughout the world, and the ability to exchange information between speakers of different languages is often a critical requirement for global solutions.

The Azure AI Translator provides an API for translating text between 90 supported languages.

After completing this module, you'll be able to:

Provision an Azure AI Translator resource
Understand language detection, translation, and transliteration
Specify translation options
Define and run custom translations
















