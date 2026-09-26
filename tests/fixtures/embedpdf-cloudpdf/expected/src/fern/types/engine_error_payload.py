

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .engine_error_payload_code import EngineErrorPayloadCode
from .engine_error_payload_name import EngineErrorPayloadName


class EngineErrorPayload(UniversalBaseModel):
    name: EngineErrorPayloadName
    code: EngineErrorPayloadCode
    message: str
    details: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
