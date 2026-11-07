

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LobbyVisibility(enum.StrEnum):
    """
    Types of lobbies a player can create.

    `private`: the player who created the room must share the roomId with their friends

    `public`: visible in the public lobby list, anyone can join

    `local`: for testing with a server running locally
    """

    PRIVATE = "private"
    PUBLIC = "public"
    LOCAL = "local"

    def visit(
        self,
        private: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
        local: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LobbyVisibility.PRIVATE:
            return private()
        if self is LobbyVisibility.PUBLIC:
            return public()
        if self is LobbyVisibility.LOCAL:
            return local()
