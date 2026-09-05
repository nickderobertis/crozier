

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connected_account_integration_response import ConnectedAccountIntegrationResponse
from .connected_account_providers import ConnectedAccountProviders
from .connected_account_visibility import ConnectedAccountVisibility


class ConnectedAccountResponse(UniversalBaseModel):
    id: str
    name: typing.Optional[str] = None
    type: ConnectedAccountProviders
    friend_sync: bool
    integrations: typing.Optional[typing.List[ConnectedAccountIntegrationResponse]] = None
    show_activity: bool
    two_way_link: bool
    verified: bool
    visibility: ConnectedAccountVisibility
    revoked: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
