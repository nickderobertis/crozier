

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2upload_part_url import V2UploadPartUrl


class V2PartUrlsData(UniversalBaseModel):
    """
    Signed transfer URLs for the requested multipart upload parts.
    """

    parts: typing.List[V2UploadPartUrl] = pydantic.Field()
    """
    Signed URLs for requested parts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
