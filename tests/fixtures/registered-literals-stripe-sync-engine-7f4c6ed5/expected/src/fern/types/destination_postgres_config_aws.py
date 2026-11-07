

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DestinationPostgresConfigAws(UniversalBaseModel):
    """
    AWS RDS IAM authentication config
    """

    host: str = pydantic.Field()
    """
    Postgres host for RDS IAM auth
    """

    port: typing.Optional[float] = pydantic.Field(default=None)
    """
    Postgres port for RDS IAM auth
    """

    database: str = pydantic.Field()
    """
    Database name for RDS IAM auth
    """

    user: str = pydantic.Field()
    """
    Database user for RDS IAM auth
    """

    region: str = pydantic.Field()
    """
    AWS region for RDS instance
    """

    role_arn: typing.Optional[str] = pydantic.Field(default=None)
    """
    IAM role ARN to assume (cross-account)
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    External ID for STS AssumeRole
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
