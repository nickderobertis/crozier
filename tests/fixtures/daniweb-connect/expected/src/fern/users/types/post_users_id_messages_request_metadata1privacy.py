

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostUsersIdMessagesRequestMetadata1Privacy(enum.StrEnum):
    PUBLIC = "Public"
    PRIVATE = "Private"
    BUBBLED = "Bubbled"
    USER = "User"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
        bubbled: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostUsersIdMessagesRequestMetadata1Privacy.PUBLIC:
            return public()
        if self is PostUsersIdMessagesRequestMetadata1Privacy.PRIVATE:
            return private()
        if self is PostUsersIdMessagesRequestMetadata1Privacy.BUBBLED:
            return bubbled()
        if self is PostUsersIdMessagesRequestMetadata1Privacy.USER:
            return user()
