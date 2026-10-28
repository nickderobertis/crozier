

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ItemsLinkType(enum.StrEnum):
    APPLICATION_GEO_JSON = "application/geo+json"

    def visit(self, application_geo_json: typing.Callable[[], T_Result]) -> T_Result:
        if self is ItemsLinkType.APPLICATION_GEO_JSON:
            return application_geo_json()
