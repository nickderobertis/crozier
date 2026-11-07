

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_postgres_config_aws import DestinationPostgresConfigAws


class DestinationPostgresConfig(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Postgres connection string
    """

    connection_string: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated alias for url; prefer url
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description='Target schema name (e.g. "stripe")'),
    ] = None
    """
    Target schema name (e.g. "stripe")
    """

    batch_size: typing.Optional[float] = pydantic.Field(default=None)
    """
    Records to buffer before flushing
    """

    aws: typing.Optional[DestinationPostgresConfigAws] = pydantic.Field(default=None)
    """
    AWS RDS IAM authentication config
    """

    ssl_ca_pem: typing.Optional[str] = pydantic.Field(default=None)
    """
    PEM-encoded CA certificate for SSL verification (required for verify-ca / verify-full with a private CA)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
