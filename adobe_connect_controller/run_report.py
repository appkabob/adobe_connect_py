from adobe_connect_controller.src.models.connect import Connect
from adobe_connect_controller.src.models.meeting import Meeting


Connect()
meeting = Meeting('Live Chat 3', '2017-03-13', '67877468')
attendees = meeting.get_attendees()
for attendee in attendees:
    print(attendee)