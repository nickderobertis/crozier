

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostMessagesIdMetadataRequestMetadata1Privacy(enum.StrEnum):
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
        if self is PostMessagesIdMetadataRequestMetadata1Privacy.PUBLIC:
            return public()
        if self is PostMessagesIdMetadataRequestMetadata1Privacy.PRIVATE:
            return private()
        if self is PostMessagesIdMetadataRequestMetadata1Privacy.BUBBLED:
            return bubbled()
        if self is PostMessagesIdMetadataRequestMetadata1Privacy.USER:
            return user()
