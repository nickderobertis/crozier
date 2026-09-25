

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.group_permission_setting import GroupPermissionSetting


class RegisterQueueResponseServerSupportedPermissionSettings(UniversalBaseModel):
    """
    Present if `realm` is present in `fetch_event_types`.

    Metadata detailing the valid values for permission settings that
    use [group-setting values](/api/group-setting-values). Clients
    should use these data as explained in the
    [main documentation](/api/group-setting-values#permitted-values)
    to determine what values to present as possible values for these
    settings in UI components.

    **Changes**: Before Zulip 10.0 (feature level 326), this part of
    the response had a documented-as-unstable format not suitable
    for general client use, and should be ignored.

    New in Zulip 8.0 (feature level 221).
    """

    realm: typing.Optional[typing.Dict[str, GroupPermissionSetting]] = pydantic.Field(default=None)
    """
    Configuration for realm level group permission settings.
    """

    stream: typing.Optional[typing.Dict[str, GroupPermissionSetting]] = pydantic.Field(default=None)
    """
    Configuration for channel level group permission settings.
    """

    group: typing.Optional[typing.Dict[str, GroupPermissionSetting]] = pydantic.Field(default=None)
    """
    Configuration for group level group permission settings.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
