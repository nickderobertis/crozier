

import typing

from .fragment_usage_data import FragmentUsageData
from .scenario_usage_data import ScenarioUsageData

NodeUsageData = typing.Union[FragmentUsageData, ScenarioUsageData]
