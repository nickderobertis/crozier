

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseManifestConfig(UniversalBaseModel):
    description: typing.Optional[str] = None
    name: str
    required_config: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="requiredConfig"), pydantic.Field(alias="requiredConfig")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
