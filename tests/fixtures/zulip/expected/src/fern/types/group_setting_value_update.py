

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .group_setting_value_update_new import GroupSettingValueUpdateNew
from .group_setting_value_update_old import GroupSettingValueUpdateOld


class GroupSettingValueUpdate(UniversalBaseModel):
    new: GroupSettingValueUpdateNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[GroupSettingValueUpdateOld] = pydantic.Field(default=None)
    """
    The expected current [group-setting value](/api/group-setting-values)
    for who has this permission.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
