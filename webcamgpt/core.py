import os
import numpy as np
import requests
from webcamgpt.utils import compose_payload

API_KEY = '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'

class OpanAIConnector:

    def __init__(self, api_key: str = API_KEY):
        if api_key is None:
            raise ValueError("API_KEY is not set")
        self.api_key = api_key

    def simple_prompt(self, image: np.ndarray, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = compose_payload(image=image, prompt=prompt)

        max_retries = 10
        for attempt in range(max_retries):
            try:
                response = requests.post("https://api.openai.com/v1/chat/completions",
                                         headers=headers, json=payload).json()

                return response['choices'][0]['message']['content']

            except KeyError:
                if attempt == max_retries - 1:
                    return "retry your qeustion retard"
