

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SeriesMetadataUpdateDtoReadingDirection(enum.StrEnum):
    LEFT_TO_RIGHT = "LEFT_TO_RIGHT"
    RIGHT_TO_LEFT = "RIGHT_TO_LEFT"
    VERTICAL = "VERTICAL"
    WEBTOON = "WEBTOON"

    def visit(
        self,
        left_to_right: typing.Callable[[], T_Result],
        right_to_left: typing.Callable[[], T_Result],
        vertical: typing.Callable[[], T_Result],
        webtoon: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SeriesMetadataUpdateDtoReadingDirection.LEFT_TO_RIGHT:
            return left_to_right()
        if self is SeriesMetadataUpdateDtoReadingDirection.RIGHT_TO_LEFT:
            return right_to_left()
        if self is SeriesMetadataUpdateDtoReadingDirection.VERTICAL:
            return vertical()
        if self is SeriesMetadataUpdateDtoReadingDirection.WEBTOON:
            return webtoon()
