import pywhatkit as kit
import schedule
import time

# Function to send a WhatsApp message
def send_message(phone_number, message):
    # Format phone number with country code, e.g., +1234567890
    # Send a message
    kit.sendwhatmsg_instantly(phone_number, message)

# Function to schedule messages
def schedule_messages(phone_number, message, interval):
    schedule.every(interval).seconds.do(send_message, phone_number, message)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # User inputs
    phone_number = input("Enter the phone number (include country code, e.g., +1234567890): ")
    message = input("Enter the message to send: ")
    interval = int(input("Enter the interval in seconds: "))
    
    print("Starting the bot...")
    schedule_messages(phone_number, message, interval)
