## A few things about the API, i am using

1.  API Provider is [api.assemblyai.com](https://docs.assemblyai.com/overview/getting-started)
2.  The API returns a json object with the outputs, we extract three fields from the json object
    1. Audio_duration
    2. Text
    3. Confidence
3.  For further improvement, we can shift to using [AWS Transcribe](https://aws.amazon.com/transcribe/) for better voice and video analysis.               