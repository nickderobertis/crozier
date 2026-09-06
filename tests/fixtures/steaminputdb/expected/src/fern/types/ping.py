

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Ping(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="$schema"),
        pydantic.Field(alias="$schema", description="A URL to the JSON Schema for this object."),
    ] = None
    """
    A URL to the JSON Schema for this object.
    """

    service: str
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
