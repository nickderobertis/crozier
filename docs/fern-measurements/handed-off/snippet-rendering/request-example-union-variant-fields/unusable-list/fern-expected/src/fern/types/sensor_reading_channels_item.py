

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SensorReadingChannelsItem(enum.StrEnum):
    HUMIDITY = "humidity"
    SOIL_MOISTURE = "soil_moisture"
    AIR_TEMPERATURE = "air_temperature"

    def visit(
        self,
        humidity: typing.Callable[[], T_Result],
        soil_moisture: typing.Callable[[], T_Result],
        air_temperature: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SensorReadingChannelsItem.HUMIDITY:
            return humidity()
        if self is SensorReadingChannelsItem.SOIL_MOISTURE:
            return soil_moisture()
        if self is SensorReadingChannelsItem.AIR_TEMPERATURE:
            return air_temperature()
