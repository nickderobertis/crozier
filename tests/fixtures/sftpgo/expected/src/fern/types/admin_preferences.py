

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AdminPreferences(UniversalBaseModel):
    hide_user_page_sections: typing.Optional[int] = pydantic.Field(default=None)
    """
    Allow to hide some sections from the user page. These are not security settings and are not enforced server side in any way. They are only intended to simplify the user page in the WebAdmin UI. 1 means hide groups section, 2 means hide filesystem section, "users_base_dir" must be set in the config file otherwise this setting is ignored, 4 means hide virtual folders section, 8 means hide profile section, 16 means hide ACLs section, 32 means hide disk and bandwidth quota limits section, 64 means hide advanced settings section. The settings can be combined
    """

    default_users_expiration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Defines the default expiration for newly created users as number of days. 0 means no expiration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
