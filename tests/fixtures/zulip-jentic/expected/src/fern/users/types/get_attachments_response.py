

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.attachment import Attachment


class GetAttachmentsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    attachments: typing.Optional[typing.List[Attachment]] = pydantic.Field(default=None)
    """
    A list of `attachment` objects, each containing
    details about a file uploaded by the user.
    """

    upload_space_used: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total size of all files uploaded by users in the organization,
    in bytes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
