from trustify.client.challenge import Challenge
from trustify.client import logger

############################################################
# Possible addition to challenge structure: priority parameter
# If only DVSNI and Payment are required, the user might want
# to be validated before submitting payment, allowing the user
# to gain confidence in the system.  If things do go poorly the 
# user has less invested in that particular session/transaction. 
#############################################################

class Payment_Challenge(Challenge):
    # Possible reasons: Wildcard Certificates, EV certificates
    # Malware scanning services, Organization or Identity validated certs
    def __init__(self, url, reason="Specialty Certificate"):
        self.url = url
        self.reason = reason
        self.times_performed = 0
        
    def perform(self, quiet=True):
        if quiet:
            dialog.Dialog().msgbox(get_display_string(), width=70)
        else:
            print get_display_string()
            raw_input('')

        self.times_performed += 1
        return True
    

    def get_display_string(self):
        if self.times_performed == 0:
            return "You are buying " + formatted_reasons() + " You will need to visit " + self.url + " to submit your payment\nPlease press enter once your payment has been submitted"

        # The user has tried at least once... display a different message
        else:
            return "The CA did not record your payment, please visit " + self.url + " for more information or to finish processing your transaction.\nPress Enter to continue"
        

    def formatted_reasons(self):
        return "\n\t* %s\n", self.reason

