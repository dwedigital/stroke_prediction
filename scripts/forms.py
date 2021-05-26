from wtforms import Form, SelectField, validators, IntegerField, BooleanField

class StrokeForm(Form):
    gender = SelectField('Gender', [validators.InputRequired()], choices=['Male', 'Female'])
    age = IntegerField('Age', [validators.NumberRange(min=13,max=90), validators.InputRequired()])
    hypertension = BooleanField('Hypertension', false_values=[False])
    heart_disease = BooleanField('Heart Disease',false_values=[False])
    ever_married = BooleanField('Ever Married',false_values=[False])
    work_type = SelectField('Work Type', choices=[('Govt_job','Government Role'),('Private','Private Sector'),("Self-employed","Self-employed")])
    Residence_type = SelectField('Residence Type', choices=["Urban","Rural"])
    avg_glucose_level = IntegerField('Glucose Level')
    bmi = IntegerField('BMI')
    smoking_status=SelectField('Smoking Status', choices=[('formerly smoked',"Used to Smoke"),("smokes","Smokes"),("never smoked","Never Smoked")])