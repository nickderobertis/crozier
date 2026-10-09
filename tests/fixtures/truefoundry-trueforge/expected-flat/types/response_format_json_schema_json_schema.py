

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ResponseFormatJsonSchemaJsonSchema(UniversalBaseModel):
    """
    JSON Schema payload. Extra provider fields are allowed.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional schema description for the model.
    """

    name: str = pydantic.Field()
    """
    Schema name sent to the provider.
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="JSON Schema object for the response."),
    ] = None
    """
    JSON Schema object for the response.
    """

    strict: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When true, ask the provider to enforce the schema strictly.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
