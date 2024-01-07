import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def schedule_command(command, delay):
    scheduler.enter(delay, 1, command.execute)


def run():
    try:
        scheduler.run()
    except KeyboardInterrupt:
        pass
