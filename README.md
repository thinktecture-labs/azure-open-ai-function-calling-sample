# OpenAI Function Calling with Azure OpenAI

This repository contains a sample application demonstrating how to user OpenAI Function Calling with `gpt-35-turbo` or `gpt-4` models deployed in Azure OpenAI.

For more information, consult the corresponding article at [https://labs.thinktecture.com/openai-function-calling-with-azure-openai/](https://labs.thinktecture.com/openai-function-calling-with-azure-openai/).

## Necessary environment variables

The sample loads necessary configuration data from `.env` file. To run this sample, create a `.env` file in the root folder before running the application.

```bash
OPENAI_API_TYPE=azure
OPENAI_API_KEY=<YOUR_API_KEY>
OPENAI_API_BASE=https://<YOURINSTANCE>.openai.azure.com
OPENAI_API_VERSION=2023-07-01-preview
MODEL_NAME=<YOUR_MODEL_NAME>
AZURE_OPENAI_DEPLOYMENT_NAME=<YOUR_DEPLOYMENT_NAME>
```

## Running the application

Once you've installed necessary [dependencies](./requirements.txt) and created your custom configuration using a `.env` file, you can run the sample using `python3 main.py`.
