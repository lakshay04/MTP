import time


class Log:
    ENABLE = False

    def __init__(self):
        pass

    @staticmethod
    def exc(tag, message):
        Log.print_log(
            "==>PRIORITY  " + " " + "[" + " " + str(time.clock()) + " " + "]" + " " + tag + " " + ":" + " " + message, True)

    @staticmethod
    def d(tag, message):
        Log.print_log("==>DEBUG  "+" "+"["+" "+str(time.clock())+" "+"]"+" "+tag+" "+":"+" "+message)

    @staticmethod
    def i(tag, message):
        Log.print_log("==>INFO   "+" "+"["+" "+str(time.clock())+" "+"]"+" "+tag+" "+":"+" "+message)

    @staticmethod
    def w(tag, message):
        Log.print_log("==>WARNING" + " " + "[" + " " + str(time.clock()) + " " + "]" + " " + tag + " " + ":" + " " + message)

    @staticmethod
    def e(tag, message):
        Log.print_log("==>ERROR  " + " " + "[" + " " + str(time.clock()) + " " + "]" + " " + tag + " " + ":" + " " + message)

    @staticmethod
    def print_log(message, priority=False):
        if not priority:
            if Log.ENABLE:
                print message
        else:
            print message

