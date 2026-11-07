

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .region import Region


class BuildRegionalContainerTagsItem(UniversalBaseModel):
    container_tag: typing_extensions.Annotated[
        str, FieldMetadata(alias="containerTag"), pydantic.Field(alias="containerTag")
    ]
    region: Region

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
