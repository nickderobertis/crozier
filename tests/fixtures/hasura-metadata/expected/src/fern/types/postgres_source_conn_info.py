

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pg_client_certs import PgClientCerts
from .postgres_pool_settings import PostgresPoolSettings
from .postgres_source_conn_info_database_url import PostgresSourceConnInfoDatabaseUrl
from .tx_isolation import TxIsolation


class PostgresSourceConnInfo(UniversalBaseModel):
    """
    https://hasura.io/docs/latest/graphql/core/api-reference/syntax-defs.html#pgsourceconnectioninfo
    """

    database_url: PostgresSourceConnInfoDatabaseUrl = pydantic.Field()
    """
    The database connection URL as a string, from an environment variable, as connection parameters, or dynamically read from a file at connect time.
    """

    isolation_level: typing.Optional[TxIsolation] = None
    pool_settings: typing.Optional[PostgresPoolSettings] = None
    ssl_configuration: typing.Optional[PgClientCerts] = None
    use_prepared_statements: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to true the server prepares statement before executing on the source database (default: false). For more details, refer to the Postgres docs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
