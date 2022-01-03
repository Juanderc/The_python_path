import logging

#logging have the same function of a print
#that show you an info, but logging
#go more ahead and show you a type 
#of info/message

#It could show you

#DEBUG(10) Useful for diagnosing issues in the code.
#INFO(20) It can act as an acknowledgment that there are no bugs in the code
#WARNING(30) Indicative of a problem that could occur in the future.
#ERROR(40) A serious bug in the code, could be a syntax error, out of memory error, exceptions.
#CRITICAL(50) An error due to which the program might stop functioning or might exit abruptly.

#basicConfig is a method that help to create a basic configuration
#for the logging system to work.

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("INFO LOGGING MESSAGE")