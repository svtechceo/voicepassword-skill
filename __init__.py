from mycroft import MycroftSkill, intent_file_handler


class Voicepassword(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('voicepassword.intent')
    def handle_voicepassword(self, message):
        self.speak_dialog('voicepassword')


def create_skill():
    return Voicepassword()

