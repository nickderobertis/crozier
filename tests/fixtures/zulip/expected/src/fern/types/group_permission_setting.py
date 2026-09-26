

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GroupPermissionSetting(UniversalBaseModel):
    """
    Configuration for a group permission setting specifying the groups
    to which the setting can be set to and the default values for the
    setting.

    **Changes**: Removed `allow_owners_group` field in Zulip 10.0 (feature level 326), as we now
    support anonymous user groups. Previously, the `role:owners` system group was
    not offered when `allow_owners_group` was false.

    Removed unnecessary `id_field_name` field in Zulip 10.0 (feature level 326). Previously,
    this always had the value of `"{setting_name}_id"`; it was an internal implementation
    detail of the server not intended to be included in the API.
    """

    require_system_group: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the setting can only be set to a system user group.
    """

    allow_internet_group: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the setting can be set to `role:internet` system group.
    """

    allow_nobody_group: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the setting can be set to `role:nobody` system group.
    """

    allow_everyone_group: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the setting can be set to `role:everyone` system group.
    
    If false, guest users cannot exercise this permission even if they are part of
    the [group-setting value](/api/group-setting-values) for this setting.
    """

    default_group_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the default system group for the setting.
    
    For some group settings, this can be `"group_creator"`. In that
    case, the default for the setting is an anonymous group whose
    only member is the group's creator.
    
    For some channel settings, this can be `"channel_creator"`.
    In that case:
    
    - If the channel's [`creator_id`][channel-response] is not `null`, default for the
      setting is an anonymous group with the channel creator as
      the only member.
    - If the channel's [`creator_id`][channel-response] is `null`, default for the setting
      is `role:nobody` system group.
    
    **Changes**: In Zulip 12.0 (feature level 427), renamed
    `"stream_creator_or_nobody"` value to `"channel_creator"`.
    
    [channel-response]: /api/get-stream-by-id#response
    """

    default_for_system_groups: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the default group for the setting for system groups.
    
    This is non-null only for group-level settings.
    """

    allowed_system_groups: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of names of system groups to which the setting can
    be set to.
    
    If the list is empty, the setting can be set to system groups
    based on the other boolean fields.
    
    **Changes**: New in Zulip 8.0 (feature level 225).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
