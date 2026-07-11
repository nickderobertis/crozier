

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TypesWeatherReport(str, enum.Enum):
    SUNNY = "SUNNY"
    CLOUDY = "CLOUDY"
    RAINING = "RAINING"
    SNOWING = "SNOWING"

    def visit(
        self,
        sunny: typing.Callable[[], T_Result],
        cloudy: typing.Callable[[], T_Result],
        raining: typing.Callable[[], T_Result],
        snowing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TypesWeatherReport.SUNNY:
            return sunny()
        if self is TypesWeatherReport.CLOUDY:
            return cloudy()
        if self is TypesWeatherReport.RAINING:
            return raining()
        if self is TypesWeatherReport.SNOWING:
            return snowing()
