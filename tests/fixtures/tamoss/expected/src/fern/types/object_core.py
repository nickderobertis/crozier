

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .object_core_get_urls_item import ObjectCoreGetUrlsItem


class ObjectCore(UniversalBaseModel):
    """
    Provides the location and metadata of the media files corresponding to a Media Object.
    """

    get_urls: typing.Optional[typing.List[ObjectCoreGetUrlsItem]] = pydantic.Field(default=None)
    """
    A list of URLs to which a GET request can be made to directly retrieve the contents of the Media Object. This is required by the `http_object_store` Storage Backend type, which is the only one currently described. Clients may choose any URL in the list and treat the content returned as identical, however servers may sort the list such that the preferred URL is first. Storage Backend metadata for controlled URLs should be populated by the TAMS instance based on the Storage Backend the Meda Object instance resides in.
    """

    key_frame_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of key frames in the Media Object. This should be set greater than zero when the Media Object contains key frames that serve as a stream access point
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
