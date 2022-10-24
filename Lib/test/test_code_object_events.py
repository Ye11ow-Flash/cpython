import unittest
from PyCodeObjectPtr.from_pyobject_ptr import PyCodeObject

from _testcapi import (
    PYCODEOBJECT_EVENT_CREATED,
    PYCODEOBJECT_EVENT_DESTROYED,
    # restore_code_object_event_callback,
    set_code_object_event_callback,
    get_code_object_created_counts,
    get_code_object_destroyed_counts,
)

class CodeObjectEventsTest(unittest.TestCase):
    def test_code_object_events_dispatched(self):
        set_code_object_event_callback()
        created = get_code_object_created_counts()
        destroyed = get_code_object_destroyed_counts()

        if created > 0:
            print("Code Object Created Couter: ", created)
        if destroyed > 0:
            print("Code Object Destroyed Couter: ", destroyed)
        # events = []
        # def handle_code_object_event(*args):
        #     events.append(args)
        # set_code_object_event_callback(handle_code_object_event)

        # # try:
        # PyCodeObject *mycodeobject
        # self.assertIn((PYCODEOBJECT_EVENT_CREATED, mycodeobject, None), events)
        # mycodeobject_id = id(mycodeobject)

        # # Clear events reference to func
        # events = []
        # del mycodeobject
        # self.assertIn((PYCODEOBJECT_EVENT_DESTROYED, mycodeobject_id, None), events)
        # finally:
            # restore_code_object_event_callback()