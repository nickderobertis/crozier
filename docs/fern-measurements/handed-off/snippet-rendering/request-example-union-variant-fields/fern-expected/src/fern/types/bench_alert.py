

import typing

from .bench_alert_levels import BenchAlertLevels
from .bench_alert_one import BenchAlertOne

BenchAlert = typing.Union[BenchAlertLevels, BenchAlertOne]
