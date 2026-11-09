

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_info_db_status import HealthInfoDbStatus


class HealthInfoDb(UniversalBaseModel):
    """
    DB connection status
    """

    status: typing.Optional[HealthInfoDbStatus] = pydantic.Field(default=None)
    """
    Health status of DB connection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
