

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .flow_storage_media_objects_item import FlowStorageMediaObjectsItem


class FlowStorage(UniversalBaseModel):
    """
    Gives information on storage for Media Objects. This schema is for the `http_object_store` Storage Backend type which provides URLs for storing Media Objects in object store buckets, and is the only Storage Backend type currently implemented.  URLs SHOULD support the inclusion of checksums in headers as supported by advertised Storage Backend product. See AppNote 0048 for more details.
    """

    media_objects: typing.Optional[typing.List[FlowStorageMediaObjectsItem]] = pydantic.Field(default=None)
    """
    List of information for identifying and uploading Media Objects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
