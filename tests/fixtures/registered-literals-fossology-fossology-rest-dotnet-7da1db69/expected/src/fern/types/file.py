

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_message import FileMessage
from .findings import Findings
from .hash import Hash


class File(UniversalBaseModel):
    """
    Meta information about file in FOSSology
    """

    hash: Hash
    findings: typing.Optional[Findings] = None
    uploads: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Upload ID if the file was uploaded as a package
    """

    message: typing.Optional[FileMessage] = pydantic.Field(default=None)
    """
    Message in case provided hash not found or error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
