

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataV1(UniversalBaseModel):
    functions: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    user-defined SQL functions
    
    
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

    version: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
