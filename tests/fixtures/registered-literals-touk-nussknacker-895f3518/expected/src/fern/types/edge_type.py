

import typing

from .custom_node_output import CustomNodeOutput
from .filter_false import FilterFalse
from .filter_true import FilterTrue
from .fragment_output import FragmentOutput
from .next_switch import NextSwitch
from .switch_default import SwitchDefault

EdgeType = typing.Union[CustomNodeOutput, FilterFalse, FilterTrue, FragmentOutput, NextSwitch, SwitchDefault]
