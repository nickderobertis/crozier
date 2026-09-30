

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connection_template import ConnectionTemplate
from .extensions_schema import ExtensionsSchema
from .postgres_source_conn_info import PostgresSourceConnInfo


class PostgresConnConfiguration(UniversalBaseModel):
    """
    https://hasura.io/docs/latest/graphql/core/api-reference/syntax-defs.html#pgconfiguration
    """

    connection_info: PostgresSourceConnInfo
    connection_set: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    connection set used for connection template (supported only for cloud/enterprise edition)
    PostgresConnectionSet
    """

    connection_template: typing.Optional[ConnectionTemplate] = None
    extensions_schema: typing.Optional[ExtensionsSchema] = None
    read_replicas: typing.Optional[typing.List[PostgresSourceConnInfo]] = pydantic.Field(default=None)
    """
    Optional list of read replica configuration (supported only in cloud/enterprise versions)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
