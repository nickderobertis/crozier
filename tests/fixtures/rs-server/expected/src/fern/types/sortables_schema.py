

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SortablesSchema(UniversalBaseModel):
    """
    Pydantic model for the Sortables JSON Schema response.
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="$schema"), pydantic.Field(alias="$schema")
    ] = None
    id: typing_extensions.Annotated[str, FieldMetadata(alias="$id"), pydantic.Field(alias="$id")]
    type: typing.Optional[str] = None
    title: typing.Optional[str] = None
    properties: typing.Optional[typing.Dict[str, typing.Any]] = None
    additional_properties: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="additionalProperties"), pydantic.Field(alias="additionalProperties")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
