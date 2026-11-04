

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JsonSchemaResponseFormatParam(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of what the response format is for, used by the model to
    determine how to respond in the format.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the response format. Must be a-z, A-Z, 0-9, or contain
    underscores and dashes, with a maximum length of 64.
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="schema"),
        pydantic.Field(
            alias="schema", description="The schema for the response format, described as a JSON Schema object."
        ),
    ] = None
    """
    The schema for the response format, described as a JSON Schema object.
    """

    strict: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable strict schema adherence when generating the output.
    If set to true, the model will always follow the exact schema defined
    in the `schema` field. Only a subset of JSON Schema is supported when
    `strict` is `true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
