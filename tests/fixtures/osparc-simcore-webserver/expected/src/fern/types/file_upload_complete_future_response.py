

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .e_tag import ETag
from .file_upload_complete_state import FileUploadCompleteState


class FileUploadCompleteFutureResponse(UniversalBaseModel):
    state: FileUploadCompleteState
    e_tag: typing.Optional[ETag] = None
    last_modified: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Last modification timestamp reported by S3, set together with e_tag
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
