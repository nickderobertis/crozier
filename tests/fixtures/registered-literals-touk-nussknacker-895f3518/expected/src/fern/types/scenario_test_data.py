

import typing

from .with_live_data import WithLiveData
from .with_parameters import WithParameters

ScenarioTestData = typing.Union[WithLiveData, WithParameters]
