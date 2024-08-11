#pip install pywhatkit
import pywhatkit as kit

# Replace with your WhatsApp number in the format '+countrycodephonenumber'
phone_number = '+1234567890'
# Replace with your message
message = 'Hello, this is a test message from my bot!'
# Time in 24-hour format (hour, minute)
time_hour = 14
time_minute = 30

kit.sendwhatmsg(phone_number, message, time_hour, time_minute)
