

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_delete200response_meta_cache_delta_pages_item import (
    DocAnnotationsDelete200ResponseMetaCacheDeltaPagesItem,
)


class DocAnnotationsDelete200ResponseMetaCacheDelta(UniversalBaseModel):
    previous_doc_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="previousDocVersion"), pydantic.Field(alias="previousDocVersion")
    ]
    doc_version: typing_extensions.Annotated[int, FieldMetadata(alias="docVersion"), pydantic.Field(alias="docVersion")]
    annotations_version: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="annotationsVersion"), pydantic.Field(alias="annotationsVersion")
    ] = None
    layer_version: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="layerVersion"), pydantic.Field(alias="layerVersion")
    ] = None
    working: typing.Optional[bool] = None
    pages: typing.List[DocAnnotationsDelete200ResponseMetaCacheDeltaPagesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
