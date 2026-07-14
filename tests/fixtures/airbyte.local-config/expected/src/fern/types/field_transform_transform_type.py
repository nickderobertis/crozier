

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FieldTransformTransformType(str, enum.Enum):
    ADD_FIELD = "add_field"
    REMOVE_FIELD = "remove_field"
    UPDATE_FIELD_SCHEMA = "update_field_schema"

    def visit(
        self,
        add_field: typing.Callable[[], T_Result],
        remove_field: typing.Callable[[], T_Result],
        update_field_schema: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FieldTransformTransformType.ADD_FIELD:
            return add_field()
        if self is FieldTransformTransformType.REMOVE_FIELD:
            return remove_field()
        if self is FieldTransformTransformType.UPDATE_FIELD_SCHEMA:
            return update_field_schema()
