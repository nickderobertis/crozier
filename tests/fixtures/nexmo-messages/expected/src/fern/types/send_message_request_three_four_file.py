

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SendMessageRequestThreeFourFile(UniversalBaseModel):
    url: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The URL of the file attachment.
    
    Supports a wide range of attachments including `.zip`, `.csv` and `.pdf`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
