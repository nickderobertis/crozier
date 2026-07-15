

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectorUnifiedApisItemOauthScopesItem(UniversalBaseModel):
    """
    OAuth scopes required for the connector. Add these scopes to your OAuth app.
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
