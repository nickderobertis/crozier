

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateSettingsRequestTargetUsers(UniversalBaseModel):
    """
    An object specifying the collection of users whose settings should be modified,
    for modification of other users' settings by an organization administrator.
    When this parameter is absent, this API endpoint always modifies the current
    user's own settings.

    **Changes**: New in Zulip 12.0 (feature level 444).
    """

    user_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    A list of integer user IDs representing individual users whose settings will be updated.
    """

    group_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    A list of integer group IDs representing user groups, where settings will be applied to
    all active members of the specified groups.
    """

    skip_if_already_edited: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to skip editing the settings of users who have previously edited their settings,
    which can be useful for adjusting a default without overriding users' own directly
    expressed preferences.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
