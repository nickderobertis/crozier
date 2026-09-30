

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CockroachNullableScalarType(UniversalBaseModel):
    """
    A scalar type that can be nullable with an optional description
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description text which appears in the GraphQL Schema
    """

    nullable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the type is nullable
    """

    type: str = pydantic.Field()
    """
    The base scalar type
    Postgres Scalar Types
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
