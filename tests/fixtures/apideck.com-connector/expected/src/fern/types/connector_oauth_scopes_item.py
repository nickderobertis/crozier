

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectorOauthScopesItem(UniversalBaseModel):
    default_apis: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of Unified APIs that request this OAuth Scope by default. Application owners can customize the requested scopes.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the OAuth scope.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label of the OAuth scope.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
