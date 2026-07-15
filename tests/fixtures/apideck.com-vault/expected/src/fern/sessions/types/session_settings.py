

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.unified_api_id import UnifiedApiId
from .session_settings_allow_actions_item import SessionSettingsAllowActionsItem


class SessionSettings(UniversalBaseModel):
    """
    Settings to change the way the Vault is displayed.
    """

    allow_actions: typing.Optional[typing.List[SessionSettingsAllowActionsItem]] = pydantic.Field(default=None)
    """
    Hide actions from your users in [Vault](/apis/vault/reference#section/Get-Started). Actions in `allow_actions` will be shown on a connection in Vault.
    Available actions are: `delete`, `disconnect`, `reauthorize` and `disable`.
    Empty array will hide all actions. By default all actions are visible.
    """

    auto_redirect: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Automatically redirect to redirect uri after the connection has been configured as callable. Defaults to `false`.
    """

    hide_guides: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Hide Apideck connection guides in [Vault](/apis/vault/reference#section/Get-Started). Defaults to `false`.
    """

    hide_resource_settings: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean that controls the display of the configurable resources for an integration. When set to true, the resource configuration options will be hidden and not shown to the user. When set to false, the resource configuration options will be displayed to the user.
    """

    isolation_mode: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Configure [Vault](/apis/vault/reference#section/Get-Started) to run in isolation mode, meaning it only shows the connection settings and hides the navigation items.
    """

    sandbox_mode: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Configure [Vault](/apis/vault/reference#section/Get-Started) to show a banner informing the logged in user is in a test environment.
    """

    session_length: typing.Optional[str] = pydantic.Field(default=None)
    """
    The duration of time the session is valid for (maximum 1 week).
    """

    show_logs: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Configure [Vault](/apis/vault/reference#section/Get-Started) to show the logs page. Defaults to `true`.
    """

    show_sidebar: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Configure [Vault](/apis/vault/reference#section/Get-Started) to show the sidebar. Defaults to `true`.
    """

    show_suggestions: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Configure [Vault](/apis/vault/reference#section/Get-Started) to show the suggestions page. Defaults to `false`.
    """

    unified_apis: typing.Optional[typing.List[UnifiedApiId]] = pydantic.Field(default=None)
    """
    Provide the IDs of the Unified APIs you want to be visible. Leaving it empty or omitting this field will show all Unified APIs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
