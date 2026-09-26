

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocPagesInsert200ResponseMetaCacheDeltaPagesItemCache(UniversalBaseModel):
    content_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="contentVersion"), pydantic.Field(alias="contentVersion")
    ]
    annotation_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="annotationVersion"), pydantic.Field(alias="annotationVersion")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
