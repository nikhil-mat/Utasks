import json
import logging
from time import sleep
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from caldav_handle import TaskCreator_Caldav
# My imports 
import subprocess
def create_notification(message): 
    subprocess.Popen(['notify-send', message]) 
    return None 



logger = logging.getLogger(__name__)


class UtaskExtension(Extension):
    def __init__(self):
        super(UtaskExtension,self).__init__()
        self.subscribe(KeywordQueryEvent,KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent,ItemEnterEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        query = event.get_argument()
        if query is not None:
            print("\n\n\n\n",query,"\n\n\n\n")
            logger.info('preferences %s' % json.dumps(extension.preferences))
            item_name = "KOKO"
            data = {'new_name': '%s %s was clicked' % (item_name, 1)}
            items.append(ExtensionResultItem(icon='images/icon.png',
                                            name='%s %s' % (item_name, 1),
                                            description=query,
                                            on_enter=ExtensionCustomAction(query, keep_app_open=True)))
        else:
            items.append(ExtensionResultItem(
                icon = 'images/icon.png',
                name = 'Enter your task'
            ))
        return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_data()
        URL = extension.preferences['Calendar_URL']
        TaskCreator_Caldav(URL,query)
        create_notification("Task Created : " + query)
        return HideWindowAction()
        # return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
        #                                                    name="Request sent",
        #                                                    on_enter=HideWindowAction())])


if __name__ == '__main__':
    UtaskExtension().run()
