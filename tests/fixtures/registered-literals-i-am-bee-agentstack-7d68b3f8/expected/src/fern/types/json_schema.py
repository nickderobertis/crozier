

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JsonSchema(UniversalBaseModel):
    """
    Structured Outputs configuration options, including a JSON Schema.
    """

    name: str
    description: typing.Optional[str] = None
    schema_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ] = None
    strict: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
