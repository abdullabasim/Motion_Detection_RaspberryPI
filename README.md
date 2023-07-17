# Motion Detection with Raspberry Pi

This project demonstrates motion detection using Raspberry Pi. It captures images upon detecting motion and performs various actions, including uploading the images to Google Cloud Storage, posting the image names to Firebase, and sending an SMS notification using Twilio.

## Prerequisites

- Raspberry Pi with RPi.GPIO library installed
- Google Cloud Storage account with a configured bucket
- Firebase account with a configured Realtime Database
- Twilio account with an allocated phone number

## Installation

1. Connect the Raspberry Pi and set up the necessary GPIO pin (14 in this case) as an input for motion detection.

2. Install the required Python libraries:
   ```
   pip install google-cloud-storage firebase-admin twilio RPi.GPIO
   ```

3. Clone or download the project files to your Raspberry Pi.

4. Open the Python script file `Motion_Detection_RaspberryPi.py` and update the following placeholders with your own credentials and settings:
   - `YOUR_STORAGE_CLIENT`: Your Google Cloud Storage client ID.
   - `YOUR_CLIENT_BUCKET`: The name of your Google Cloud Storage bucket.
   - `YOUR_FIREBASE_URL`: The URL of your Firebase Realtime Database.
   - `YOUR_TWILIO_ACCOUNT_SID`: Your Twilio account SID.
   - `YOUR_TWILIO_AUTH_TOKEN`: Your Twilio account authentication token.
   - `YOUR_TWILIO_PHONE_NUMBER`: Your Twilio phone number.
   - `RECEIVER_PHONE_NUMBER`: The phone number to receive SMS notifications.

## Usage

1. Run the Python script:
   ```
   python Motion_Detection_RaspberryPi.py
   ```

2. The script will start monitoring for motion detection using the connected GPIO pin.

3. Upon detecting motion, the script captures two images using Raspberry Pi Camera, uploads them to Google Cloud Storage, posts their names to Firebase, and sends an SMS notification via Twilio.

4. Check the console for status updates and notifications.

## Customization

- You can adjust the GPIO pin number for motion detection by modifying `GPIO.setup(14, GPIO.IN)` in the script.
- Feel free to modify the image capture settings using the `raspistill` command according to your preferences.
