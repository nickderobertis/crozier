

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .big_query_function_name import BigQueryFunctionName
from .function_config import FunctionConfig
from .function_permission_info import FunctionPermissionInfo


class BigqueryFunctionMetadata(UniversalBaseModel):
    """
    A custom SQL function to add to the GraphQL schema with configuration.

    https://hasura.io/docs/latest/graphql/core/api-reference/schema-metadata-api/custom-functions.html#args-syntax
    """

    comment: typing.Optional[str] = None
    configuration: typing.Optional[FunctionConfig] = None
    function: BigQueryFunctionName
    permissions: typing.Optional[typing.List[FunctionPermissionInfo]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
