

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataV2(UniversalBaseModel):
    actions: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    action definitions which extend Hasura's schema with custom business logic using custom queries and mutations
    
    
    array of values of unspecified type - this is a placeholder that will eventually be replaced with a more detailed description
    """

    allowlist: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    safe GraphQL operations - when allow lists are enabled only these operations are allowed
    
    
    array of values of unspecified type - this is a placeholder that will eventually be replaced with a more detailed description
    """

    cron_triggers: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    reliably trigger HTTP endpoints to run custom business logic periodically based on a cron schedule
    
    
    array of values of unspecified type - this is a placeholder that will eventually be replaced with a more detailed description
    """

    custom_types: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    custom type definitions
    
    
    object with unspecified properties - this is a placeholder that will eventually be replaced with a more detailed description
    """

    functions: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    user-defined SQL functions
    
    
    array of values of unspecified type - this is a placeholder that will eventually be replaced with a more detailed description
    """

    query_collections: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    group queries using query collections
    
    
    array of values of unspecified type - this is a placeholder that will eventually be replaced with a more detailed description
    """

    remote_schemas: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    merge remote GraphQL schemas and provide a unified GraphQL API
    
    
    array of values of unspecified type - this is a placeholder that will eventually be replaced with a more detailed description
    """

    tables: typing.List[typing.Dict[str, typing.Any]] = pydantic.Field()
    """
    configured database tables
    
    
    array of values of unspecified type - this is a placeholder that will eventually be replaced with a more detailed description
    """

    version: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
