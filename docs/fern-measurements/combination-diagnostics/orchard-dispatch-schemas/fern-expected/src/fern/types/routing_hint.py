

import typing

from .routing_hint_code import RoutingHintCode
from .routing_hint_detail import RoutingHintDetail

RoutingHint = typing.Union[RoutingHintCode, RoutingHintDetail]
