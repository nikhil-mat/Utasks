import caldav 
# TODO add username-password support
# maybe taking input from preferences or some safer alternative
# Maybe .netrc file???
def TaskCreator_Caldav(URL,Event):
    with caldav.DAVClient(url=URL,username="TODO",password="TODO") as client:
        tasklist = client.calendar(url=URL)
        tasks = tasklist.todos()
        tasklist.save_todo(summary=Event)
