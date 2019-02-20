from datetime import datetime as dt, time
from time import sleep
from os import system
import sys
import re


def set_alarm():
    pattern = r"[0-9]{1,2}:[0-9]{1,2}"
    print(f"Current time is {dt.time(dt.now())}\n")
    set_time = input("Enter time as hh:mm in 24 hour time (or E to exit): ")
    if set_time == "E":
        sys.exit()
    elif re.match(pattern, set_time):
        return [int(i) for i in set_time.split(":")]
    else:
        print("You need to enter in the format hh:mm, Eg.: 12:30")


def clear_scrn(): return system('cls')


def ring_alarm(set_alarm, clear_scrn):
    hms_array = set_alarm()
    assert hms_array[0] < 24, "Hour (hh) should be less than 24"
    assert hms_array[1] < 60, "Minutes (mm) should be less than 60"
    set_time = time(hms_array[0], hms_array[1])
    cur_time = dt.time(dt.now())
    if set_time > cur_time:
        print(f"Alarm set for {set_time}")
        while set_time.minute > cur_time.minute:
            if set_time.minute - cur_time.minute > 1:
                sleep(60)
            else:
                sleep(1)
            cur_time = dt.time(dt.now())
        try:
            for i in range(10):
                clear_scrn()
                print(chr(7), chr(7))
                print("ALRM RINGING!!!!")
                sleep(1.5)
        except KeyboardInterrupt:
            print("Interrupted by User! Bye!")
            sys.exit()

    else:
        clear_scrn()
        print("That's already over! Enter a time atleast a min later than current time\n")
        ring_alarm(set_alarm, clear_scrn)


if __name__ == '__main__':
    ring_alarm(set_alarm, clear_scrn)
