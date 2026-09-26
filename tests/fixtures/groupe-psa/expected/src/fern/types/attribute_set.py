

import typing

from .attribute import Attribute

AttributeSet = typing.List[Attribute]
"""
Additional attributes-set as key/value pairs wich will be added to the request when sending the event. It can be used as http header enhancement (such as headers can be used as an authentication parameter when posting the event) or simply added to the notification event body (as set of key/values) or finally as additional query parameters.
"""
