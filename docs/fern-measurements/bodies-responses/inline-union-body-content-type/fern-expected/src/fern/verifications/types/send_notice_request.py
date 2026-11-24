

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SendNoticeRequest_Email(UniversalBaseModel):
    """
    Either address to notify.
    """

    type: typing.Literal["email"] = "email"
    email: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SendNoticeRequest_Sms(UniversalBaseModel):
    """
    Either address to notify.
    """

    type: typing.Literal["sms"] = "sms"
    phone: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SendNoticeRequest = typing_extensions.Annotated[
    typing.Union[SendNoticeRequest_Email, SendNoticeRequest_Sms], pydantic.Field(discriminator="type")
]
