

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RecheckVerificationRequest_Email(UniversalBaseModel):
    type: typing.Literal["email"] = "email"
    email: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RecheckVerificationRequest_Sms(UniversalBaseModel):
    type: typing.Literal["sms"] = "sms"
    phone: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RecheckVerificationRequest = typing_extensions.Annotated[
    typing.Union[RecheckVerificationRequest_Email, RecheckVerificationRequest_Sms], pydantic.Field(discriminator="type")
]
