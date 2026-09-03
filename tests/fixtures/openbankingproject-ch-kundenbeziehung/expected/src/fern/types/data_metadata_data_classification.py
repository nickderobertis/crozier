

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataMetadataDataClassification(enum.StrEnum):
    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"
    RESTRICTED = "restricted"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        internal: typing.Callable[[], T_Result],
        confidential: typing.Callable[[], T_Result],
        restricted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataMetadataDataClassification.PUBLIC:
            return public()
        if self is DataMetadataDataClassification.INTERNAL:
            return internal()
        if self is DataMetadataDataClassification.CONFIDENTIAL:
            return confidential()
        if self is DataMetadataDataClassification.RESTRICTED:
            return restricted()
