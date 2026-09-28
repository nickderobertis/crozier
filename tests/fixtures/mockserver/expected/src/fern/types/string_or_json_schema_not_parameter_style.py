

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StringOrJsonSchemaNotParameterStyle(enum.StrEnum):
    SIMPLE = "SIMPLE"
    SIMPLE_EXPLODED = "SIMPLE_EXPLODED"
    LABEL = "LABEL"
    LABEL_EXPLODED = "LABEL_EXPLODED"
    MATRIX = "MATRIX"
    MATRIX_EXPLODED = "MATRIX_EXPLODED"
    FORM_EXPLODED = "FORM_EXPLODED"
    FORM = "FORM"
    SPACE_DELIMITED_EXPLODED = "SPACE_DELIMITED_EXPLODED"
    SPACE_DELIMITED = "SPACE_DELIMITED"
    PIPE_DELIMITED_EXPLODED = "PIPE_DELIMITED_EXPLODED"
    PIPE_DELIMITED = "PIPE_DELIMITED"
    DEEP_OBJECT = "DEEP_OBJECT"

    def visit(
        self,
        simple: typing.Callable[[], T_Result],
        simple_exploded: typing.Callable[[], T_Result],
        label: typing.Callable[[], T_Result],
        label_exploded: typing.Callable[[], T_Result],
        matrix: typing.Callable[[], T_Result],
        matrix_exploded: typing.Callable[[], T_Result],
        form_exploded: typing.Callable[[], T_Result],
        form: typing.Callable[[], T_Result],
        space_delimited_exploded: typing.Callable[[], T_Result],
        space_delimited: typing.Callable[[], T_Result],
        pipe_delimited_exploded: typing.Callable[[], T_Result],
        pipe_delimited: typing.Callable[[], T_Result],
        deep_object: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StringOrJsonSchemaNotParameterStyle.SIMPLE:
            return simple()
        if self is StringOrJsonSchemaNotParameterStyle.SIMPLE_EXPLODED:
            return simple_exploded()
        if self is StringOrJsonSchemaNotParameterStyle.LABEL:
            return label()
        if self is StringOrJsonSchemaNotParameterStyle.LABEL_EXPLODED:
            return label_exploded()
        if self is StringOrJsonSchemaNotParameterStyle.MATRIX:
            return matrix()
        if self is StringOrJsonSchemaNotParameterStyle.MATRIX_EXPLODED:
            return matrix_exploded()
        if self is StringOrJsonSchemaNotParameterStyle.FORM_EXPLODED:
            return form_exploded()
        if self is StringOrJsonSchemaNotParameterStyle.FORM:
            return form()
        if self is StringOrJsonSchemaNotParameterStyle.SPACE_DELIMITED_EXPLODED:
            return space_delimited_exploded()
        if self is StringOrJsonSchemaNotParameterStyle.SPACE_DELIMITED:
            return space_delimited()
        if self is StringOrJsonSchemaNotParameterStyle.PIPE_DELIMITED_EXPLODED:
            return pipe_delimited_exploded()
        if self is StringOrJsonSchemaNotParameterStyle.PIPE_DELIMITED:
            return pipe_delimited()
        if self is StringOrJsonSchemaNotParameterStyle.DEEP_OBJECT:
            return deep_object()
