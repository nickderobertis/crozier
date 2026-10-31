

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lineage_digest import LineageDigest


class LineageLocator(UniversalBaseModel):
    uri: str
    media_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mediaType"), pydantic.Field(alias="mediaType")
    ] = None
    digest: typing.Optional[LineageDigest] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
