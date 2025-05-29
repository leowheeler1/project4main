# This module includes an interactive if-else chatbot that intakes the type of severity and the
# resultant action the user should take.

def chatbot(severity):

    # There are five levels:
    # Safe
    # Mild 
    # Moderate
    # Immediate Care
    # Emergency

    if severity == "Safe":
        return f"""
            You are experiencing a situation of {severity} severity. Please consider taking light
            doses of Ibuprofen, along with Gatorade / water , an icepack, and rest. Do not panic,
            everything is fine.
        """
    elif severity == "Mild":
        return f"""
            You are experiencing a situation of {severity} severity. Please consider getting in
            contact with your primary doctor with in 1-2 weeks, as this situation may cause issues.
            In the mean time, do not panic. Set an appointment at speak with your primary care 
            doctor as soon as possible.
        """
    elif severity == "Moderate":
        return f"""
            You are experiencing a situation of {severity} severity. Please consider getting in
            contact with your primary doctor with in the next week, as this situation is severe.
            Set an appointment at speak with your primary care doctor immediately.
        """
    elif severity == "Immediate Care":
        return f"""
            You are experiencing a situation of {severity} severity. You should seek urgent medical
            attention at an Urgent Care clinic, preferably in the next day or two at the most. If 
            possible, have someone else drive you there or take a rideshare service and bring
            food and water so you can stay there. Do not panic, seek help.
        """
    else:
        return f""" 
            You are experiencing a situation of {severity} severity. Do not panic. This is a major
            emergency. You need to call 911 or your local emergency services hotline to request an
            ambulance pickup or have a relative or close friend drive you to the nearest hospital.

            DO NOT WAIT. YOU NEED TO GO TO THE ER IMMEDIATELY.

            All will be well as long as you request immediate health services.
        """
