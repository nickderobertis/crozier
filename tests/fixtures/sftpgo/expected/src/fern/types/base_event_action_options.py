

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_action_command_config import EventActionCommandConfig
from .event_action_data_retention_config import EventActionDataRetentionConfig
from .event_action_email_config import EventActionEmailConfig
from .event_action_filesystem_config import EventActionFilesystemConfig
from .event_action_http_config import EventActionHttpConfig
from .event_action_idp_account_check import EventActionIdpAccountCheck
from .event_action_password_expiration import EventActionPasswordExpiration
from .event_action_user_inactivity import EventActionUserInactivity


class BaseEventActionOptions(UniversalBaseModel):
    http_config: typing.Optional[EventActionHttpConfig] = None
    cmd_config: typing.Optional[EventActionCommandConfig] = None
    email_config: typing.Optional[EventActionEmailConfig] = None
    retention_config: typing.Optional[EventActionDataRetentionConfig] = None
    fs_config: typing.Optional[EventActionFilesystemConfig] = None
    pwd_expiration_config: typing.Optional[EventActionPasswordExpiration] = None
    user_inactivity_config: typing.Optional[EventActionUserInactivity] = None
    idp_config: typing.Optional[EventActionIdpAccountCheck] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
