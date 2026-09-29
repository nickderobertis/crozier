

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bigquery_nullable_scalar_type import BigqueryNullableScalarType
from .rel_def_rel_manual_config_big_query import RelDefRelManualConfigBigQuery


class BigqueryNativeQueryMetadata(UniversalBaseModel):
    """
    A native query as represented in metadata.
    """

    arguments: typing.Optional[typing.Dict[str, BigqueryNullableScalarType]] = pydantic.Field(default=None)
    """
    Free variables in the expression and their types
    """

    array_relationships: typing.Optional[typing.List[RelDefRelManualConfigBigQuery]] = None
    code: str = pydantic.Field()
    """
    Native code expression (SQL) to run
    An interpolated query expressed in native code (SQL)
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the native query which appears in the graphql schema
    """

    object_relationships: typing.Optional[typing.List[RelDefRelManualConfigBigQuery]] = None
    returns: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Return type (table) of the expression
    A name or definition of a Logical Model
    value with unspecified type - this is a placeholder that will eventually be replaced with a more detailed description
    """

    root_field_name: str = pydantic.Field()
    """
    Root field name for the native query
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
