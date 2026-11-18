import requests
url = ("https://sn-watson-emotion.labs.skills.network"
       "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")
headers = {"grpc-metadata-mm-model-id":
           "emotion_aggregated-workflow_lang_en_stock"}
r = requests.post(url, json={"raw_document": {"text": ""}},
                  headers=headers, timeout=10)
print(r.status_code)
print(r.text)