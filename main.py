import pywhatkit as kit
import schedule
import time
import logging
import datetime


logging.basicConfig(filename="reminder.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

def send_drink_water_reminder():
    now = datetime.datetime.now()

    # Only log when time is between 11:00 and 20:00
    if now.hour < 11 or now.hour >= 20:
        logging.info("Reminder Voided: Outside of allowed time window")
        print("Reminder Voided")
        return

    try:
        kit.sendwhatmsg_to_group_instantly(
                                        "BxVI70EcSww6qRWLAB06kr", 
                                        "Remember to Drink Water My BB :3\n\n*Sent by ReminderBot* ", 
                                        15, True, 5
                                    )
        logging.info("Reminder Sent")
        print("Reminder Sent")

    except Exception as e:
        logging.info(f"Error: {e}")
        print(f"Error: {e}")


schedule.every(1).hour.do(send_drink_water_reminder)

if __name__ == "__main__":
    logging.info("Process Started")
    print("Process Started")
    send_drink_water_reminder()
    
    while True:
        schedule.run_pending()
        time.sleep(1)
