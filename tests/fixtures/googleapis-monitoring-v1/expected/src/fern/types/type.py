

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field import Field
from .option import Option
from .source_context import SourceContext
from .type_syntax import TypeSyntax


class Type(UniversalBaseModel):
    """
    A protocol buffer message type.
    """

    edition: typing.Optional[str] = pydantic.Field(default=None)
    """
    The source edition string, only valid when syntax is SYNTAX_EDITIONS.
    """

    fields: typing.Optional[typing.List[Field]] = pydantic.Field(default=None)
    """
    The list of fields.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The fully qualified message name.
    """

    oneofs: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of types appearing in oneof definitions in this type.
    """

    options: typing.Optional[typing.List[Option]] = pydantic.Field(default=None)
    """
    The protocol buffer options.
    """

    source_context: typing_extensions.Annotated[
        typing.Optional[SourceContext],
        FieldMetadata(alias="sourceContext"),
        pydantic.Field(alias="sourceContext", description="The source context."),
    ] = None
    """
    The source context.
    """

    syntax: typing.Optional[TypeSyntax] = pydantic.Field(default=None)
    """
    The source syntax.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
