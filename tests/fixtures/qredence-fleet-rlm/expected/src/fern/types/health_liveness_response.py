

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_liveness_response_status import HealthLivenessResponseStatus


class HealthLivenessResponse(UniversalBaseModel):
    """
    Liveness payload — the process is serving HTTP; no dependency checks.
    """

    status: HealthLivenessResponseStatus
    app: str
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
