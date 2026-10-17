

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1pgbouncer_config_response_output_pool_mode import V1PgbouncerConfigResponseOutputPoolMode


class V1PgbouncerConfigResponseOutput(UniversalBaseModel):
    default_pool_size: typing.Optional[int] = None
    ignore_startup_parameters: typing.Optional[str] = None
    max_client_conn: typing.Optional[int] = None
    pool_mode: typing.Optional[V1PgbouncerConfigResponseOutputPoolMode] = None
    connection_string: typing.Optional[str] = None
    server_idle_timeout: typing.Optional[int] = None
    server_lifetime: typing.Optional[int] = None
    query_wait_timeout: typing.Optional[int] = None
    reserve_pool_size: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
