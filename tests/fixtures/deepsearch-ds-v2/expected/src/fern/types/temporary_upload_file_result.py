

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .temporary_url import TemporaryUrl
from .temporary_url_fields import TemporaryUrlFields


class TemporaryUploadFileResult(UniversalBaseModel):
    id: str
    upload: TemporaryUrlFields
    download: TemporaryUrl
    metadata: TemporaryUrl
    upload_private: TemporaryUrlFields
    download_private: TemporaryUrl
    metadata_private: TemporaryUrl

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
