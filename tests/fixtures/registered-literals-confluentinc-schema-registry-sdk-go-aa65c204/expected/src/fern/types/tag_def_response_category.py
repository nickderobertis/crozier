

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TagDefResponseCategory(enum.StrEnum):
    PRIMITIVE = "PRIMITIVE"
    OBJECT_ID_TYPE = "OBJECT_ID_TYPE"
    ENUM = "ENUM"
    STRUCT = "STRUCT"
    CLASSIFICATION = "CLASSIFICATION"
    ENTITY = "ENTITY"
    ARRAY = "ARRAY"
    MAP = "MAP"
    RELATIONSHIP = "RELATIONSHIP"
    BUSINESS_METADATA = "BUSINESS_METADATA"

    def visit(
        self,
        primitive: typing.Callable[[], T_Result],
        object_id_type: typing.Callable[[], T_Result],
        enum: typing.Callable[[], T_Result],
        struct: typing.Callable[[], T_Result],
        classification: typing.Callable[[], T_Result],
        entity: typing.Callable[[], T_Result],
        array: typing.Callable[[], T_Result],
        map_: typing.Callable[[], T_Result],
        relationship: typing.Callable[[], T_Result],
        business_metadata: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TagDefResponseCategory.PRIMITIVE:
            return primitive()
        if self is TagDefResponseCategory.OBJECT_ID_TYPE:
            return object_id_type()
        if self is TagDefResponseCategory.ENUM:
            return enum()
        if self is TagDefResponseCategory.STRUCT:
            return struct()
        if self is TagDefResponseCategory.CLASSIFICATION:
            return classification()
        if self is TagDefResponseCategory.ENTITY:
            return entity()
        if self is TagDefResponseCategory.ARRAY:
            return array()
        if self is TagDefResponseCategory.MAP:
            return map_()
        if self is TagDefResponseCategory.RELATIONSHIP:
            return relationship()
        if self is TagDefResponseCategory.BUSINESS_METADATA:
            return business_metadata()
