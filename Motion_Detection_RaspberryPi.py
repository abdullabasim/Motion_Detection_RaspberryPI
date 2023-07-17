import RPi.GPIO as GPIO
import time
from google.cloud import storage
from firebase import firebase
import os
import datetime
import uuid
import os
from twilio.rest import Client

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

def upload_pictures(image_name):
    # Create a Google Cloud Storage client
    client = storage.Client('YOUR_STORAGE_CLIENT')

    # Get the desired bucket
    bucket = client.get_bucket('YOUR_CLIENT_BUCKET')

    # Create a blob object for the image file
    blob = bucket.blob(image_name)

    # Upload the image file to the bucket
    blob.upload_from_filename("/home/pi/motion_detection_images/" + image_name + ".jpg")
    
    # Create a Firebase application instance
    firebases = firebase.FirebaseApplication('YOUR_FIREBASE_URL', None)

    # Post the image name to the Firebase database
    firebases.post('/data', image_name)
    
    # Remove the uploaded image file from the local directory
    os.remove("/home/pi/motion_detection_images/" + image_name + ".jpg")
    
    print("Done!!")

try:
    time.sleep(2)  # Stabilize the sensor

    while True:
        if GPIO.input(14):
            print("Motion Detected...")

            # Generate unique image names using UUID
            image_name1 = str(uuid.uuid4())
            image_name2 = str(uuid.uuid4())

            # Capture the first image
            os.system("raspistill --width 800 --height 600 --quality 100 -o " + image_name1 + ".jpg")
            upload_pictures(image_name1)

            # Capture the second image
            os.system("raspistill --width 800 --height 600 --quality 100 -o " + image_name2 + ".jpg")
            upload_pictures(image_name2)

            # Send SMS using Twilio
            account_sid = "YOUR_TWILIO_ACCOUNT_SID"
            auth_token = "YOUR_TWILIO_AUTH_TOKEN"
            client = Client(account_sid, auth_token)

            client.messages.create(
                body="Motion Detection Done!",
                from_="YOUR_TWILIO_PHONE_NUMBER",
                to="RECEIVER_PHONE_NUMBER"
            )

            print("SMS sent successfully!!")
            time.sleep(5)  # Avoid multiple detections
            time.sleep(0.1)  # Loop delay, should be less than detection delay

except ValueError as e:
    GPIO.cleanup()
    print(e)
