

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_readiness_response_database import HealthReadinessResponseDatabase
from .health_readiness_response_status import HealthReadinessResponseStatus


class HealthReadinessResponse(UniversalBaseModel):
    """
    Readiness payload — composition installed and the database answers.
    """

    status: HealthReadinessResponseStatus
    database: HealthReadinessResponseDatabase

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
