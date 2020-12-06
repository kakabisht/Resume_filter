## A few things about the API, i am using

1.  API Provider is [dandelion.eu](https://dandelion.eu/docs/api/datatxt/sent/v1/)
2.  The API returns a json object with the outputs, we extract three fields from the json object
    1. The language used to analyze the input text.
    2. Sentiment score: Strength of sentiment detected, from -1.0 (totally negative) to 1.0 (absolutely positive).
    3. Sentiment type": Either 'positive', 'neutral' or 'negative'
3.  For further improvement, we can shift to using [AWS Comprehend](https://aws.amazon.com/comprehend) for better natural language processing (NLP). 
