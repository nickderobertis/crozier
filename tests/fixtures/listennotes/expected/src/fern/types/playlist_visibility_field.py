

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlaylistVisibilityField(enum.StrEnum):
    """
    Visibility of this playlist.
    """

    PUBLIC = "public"
    UNLISTED = "unlisted"
    PRIVATE = "private"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        unlisted: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlaylistVisibilityField.PUBLIC:
            return public()
        if self is PlaylistVisibilityField.UNLISTED:
            return unlisted()
        if self is PlaylistVisibilityField.PRIVATE:
            return private()
