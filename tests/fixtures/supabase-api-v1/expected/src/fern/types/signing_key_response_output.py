

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .signing_key_response_output_algorithm import SigningKeyResponseOutputAlgorithm
from .signing_key_response_output_status import SigningKeyResponseOutputStatus


class SigningKeyResponseOutput(UniversalBaseModel):
    id: str
    algorithm: SigningKeyResponseOutputAlgorithm
    status: SigningKeyResponseOutputStatus
    public_jwk: typing.Optional[typing.Any] = None
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
