

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CoreUnifiedSearchResultEntry(UniversalBaseModel):
    thumbnail_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="thumbnailUrl"), pydantic.Field(alias="thumbnailUrl")
    ]
    title: str
    subline: str
    resource_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="resourceUrl"), pydantic.Field(alias="resourceUrl")
    ]
    icon: str
    rounded: bool
    attributes: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
