

import typing

from .dial_control_gadget import DialControlGadget
from .fan_gadget import FanGadget
from .lamp_gadget import LampGadget

PanelGadgetsItem = typing.Union[LampGadget, FanGadget, DialControlGadget]
