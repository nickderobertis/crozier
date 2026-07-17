

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_reference import ApiReference


class SubclassLevelResource(UniversalBaseModel):
    class_: typing_extensions.Annotated[
        typing.Optional[ApiReference], FieldMetadata(alias="class"), pydantic.Field(alias="class")
    ] = None
    features: typing.Optional[typing.List[ApiReference]] = None
    index: typing.Optional[str] = None
    level: typing.Optional[float] = None
    subclass: typing.Optional[ApiReference] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
