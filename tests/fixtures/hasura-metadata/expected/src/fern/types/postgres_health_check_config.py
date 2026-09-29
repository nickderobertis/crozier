

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_check_test_sql import HealthCheckTestSql


class PostgresHealthCheckConfig(UniversalBaseModel):
    interval: float
    retries: typing.Optional[float] = None
    retry_interval: typing.Optional[float] = None
    test: typing.Optional[HealthCheckTestSql] = None
    timeout: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
