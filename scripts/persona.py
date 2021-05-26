import requests
import os
from dotenv import load_dotenv

load_dotenv()
APIKEY = os.getenv('APIKEY')
REPORT_ID = os.getenv('REPORT_ID')

class Persona():

    def __init__(self, persona: dict)->None:
        """ Class that takes in a Dict of the persona attributes"""
        self.gender = persona['gender']
        self.age = persona['age']
        self.hypertension = 1 if 'hypertension' in persona else 0
        self.heart_disease = 1 if 'heart_disease' in persona else 0
        self.ever_married ="Yes" if 'ever_married' in persona else "No"
        self.work_type = persona['work_type']
        self.Residence_type = persona['Residence_type']
        self.avg_glucose_level = persona['avg_glucose_level']
        self.bmi = persona['bmi']
        self.smoking_status = persona['smoking_status']


    def Predict(self)->str:

        data = {
    "features":
        {
            "gender":self.gender,
            "age":self.age,
            "hypertension":self.hypertension,
            "heart_disease":self.heart_disease,
            "ever_married":self.ever_married,
            "work_type":self.work_type,
            "Residence_type":self.Residence_type,
            "avg_glucose_level":self.avg_glucose_level,
            "bmi":self.bmi,
            "smoking_status":self.smoking_status
    },
    "id": REPORT_ID
}

        headers ={"Authorization":f"ApiKey {APIKEY}"
            
        }
        r = requests.post("https://api.obviously.ai/user/persona", json=data, headers=headers)

        return r.json()