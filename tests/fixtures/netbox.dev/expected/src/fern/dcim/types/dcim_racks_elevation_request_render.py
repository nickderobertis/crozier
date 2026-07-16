

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DcimRacksElevationRequestRender(str, enum.Enum):
    JSON = "json"
    SVG = "svg"

    def visit(self, json: typing.Callable[[], T_Result], svg: typing.Callable[[], T_Result]) -> T_Result:
        if self is DcimRacksElevationRequestRender.JSON:
            return json()
        if self is DcimRacksElevationRequestRender.SVG:
            return svg()
