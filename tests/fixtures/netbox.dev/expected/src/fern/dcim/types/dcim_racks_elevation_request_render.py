

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DcimRacksElevationRequestRender(enum.StrEnum):
    JSON = "json"
    SVG = "svg"

    def visit(self, json: typing.Callable[[], T_Result], svg: typing.Callable[[], T_Result]) -> T_Result:
        if self is DcimRacksElevationRequestRender.JSON:
            return json()
        if self is DcimRacksElevationRequestRender.SVG:
            return svg()
