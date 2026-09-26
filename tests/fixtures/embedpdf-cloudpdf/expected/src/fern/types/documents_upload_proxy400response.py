

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .documents_upload_proxy400response_error import DocumentsUploadProxy400ResponseError


class DocumentsUploadProxy400Response(UniversalBaseModel):
    error: DocumentsUploadProxy400ResponseError

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
