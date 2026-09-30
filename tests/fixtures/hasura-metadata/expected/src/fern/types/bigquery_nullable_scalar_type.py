

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BigqueryNullableScalarType(UniversalBaseModel):
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

    type: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The base scalar type
    A scalar type for BigQuery
    value with unspecified type - this is a placeholder that will eventually be replaced with a more detailed description
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
