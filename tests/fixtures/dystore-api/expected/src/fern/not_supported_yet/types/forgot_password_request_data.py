

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .forgot_password_request_data_attributes import ForgotPasswordRequestDataAttributes


class ForgotPasswordRequestData(UniversalBaseModel):
    attributes: typing.Optional[ForgotPasswordRequestDataAttributes] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
