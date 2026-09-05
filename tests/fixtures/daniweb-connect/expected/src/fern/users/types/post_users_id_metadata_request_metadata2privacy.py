

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostUsersIdMetadataRequestMetadata2Privacy(enum.StrEnum):
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
        if self is PostUsersIdMetadataRequestMetadata2Privacy.PUBLIC:
            return public()
        if self is PostUsersIdMetadataRequestMetadata2Privacy.PRIVATE:
            return private()
        if self is PostUsersIdMetadataRequestMetadata2Privacy.BUBBLED:
            return bubbled()
        if self is PostUsersIdMetadataRequestMetadata2Privacy.USER:
            return user()
