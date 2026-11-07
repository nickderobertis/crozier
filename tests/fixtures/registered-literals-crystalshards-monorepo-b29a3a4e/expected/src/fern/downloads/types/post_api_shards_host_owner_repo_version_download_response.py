

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostApiShardsHostOwnerRepoVersionDownloadResponse(UniversalBaseModel):
    message: typing.Optional[str] = None
    download_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Presigned URL for downloading the package
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
