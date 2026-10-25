

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_envelope_status import ApiEnvelopeStatus


class ApiEnvelope(UniversalBaseModel):
    status: typing.Optional[ApiEnvelopeStatus] = None
    message: typing.Optional[str] = None
    data: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
