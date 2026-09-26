

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_versions_download_response_code import DocVersionsDownloadResponseCode
from .doc_versions_download_response_name import DocVersionsDownloadResponseName


class DocVersionsDownloadResponse(UniversalBaseModel):
    name: DocVersionsDownloadResponseName
    code: DocVersionsDownloadResponseCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
