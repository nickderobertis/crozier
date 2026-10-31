

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Artifact(UniversalBaseModel):
    content_length: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="contentLength"), pydantic.Field(alias="contentLength")
    ] = None
    content_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ] = None
    height: typing.Optional[float] = None
    label: typing.Optional[str] = None
    url: typing.Optional[str] = None
    width: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
