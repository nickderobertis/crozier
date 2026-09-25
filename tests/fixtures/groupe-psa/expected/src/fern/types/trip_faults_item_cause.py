

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TripFaultsItemCause(enum.StrEnum):
    GEO_PRIVACY = "GeoPrivacy"
    FULL_PRIVACY = "FullPrivacy"
    CONNECTION = "Connection"

    def visit(
        self,
        geo_privacy: typing.Callable[[], T_Result],
        full_privacy: typing.Callable[[], T_Result],
        connection: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TripFaultsItemCause.GEO_PRIVACY:
            return geo_privacy()
        if self is TripFaultsItemCause.FULL_PRIVACY:
            return full_privacy()
        if self is TripFaultsItemCause.CONNECTION:
            return connection()
