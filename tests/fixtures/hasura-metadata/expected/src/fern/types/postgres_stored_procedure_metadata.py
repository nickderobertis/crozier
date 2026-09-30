

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .postgres_nullable_scalar_type import PostgresNullableScalarType
from .stored_procedure_config import StoredProcedureConfig


class PostgresStoredProcedureMetadata(UniversalBaseModel):
    """
    A stored procedure as represented in metadata.
    """

    arguments: typing.Optional[typing.Dict[str, PostgresNullableScalarType]] = pydantic.Field(default=None)
    """
    Free variables in the expression and their types
    """

    configuration: StoredProcedureConfig
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the stored procedure which appears in the graphql schema
    """

    returns: str = pydantic.Field()
    """
    Return type (table) of the expression
    """

    stored_procedure: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The name of the SQL stored procedure
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
