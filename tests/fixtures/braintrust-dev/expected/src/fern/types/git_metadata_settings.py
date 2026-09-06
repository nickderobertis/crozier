

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .git_metadata_settings_collect import GitMetadataSettingsCollect
from .git_metadata_settings_fields_item import GitMetadataSettingsFieldsItem


class GitMetadataSettings(UniversalBaseModel):
    """
    Optional settings for collecting git metadata. By default, will collect all git metadata fields allowed in org-level settings.
    """

    collect: GitMetadataSettingsCollect
    fields: typing.Optional[typing.List[GitMetadataSettingsFieldsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
