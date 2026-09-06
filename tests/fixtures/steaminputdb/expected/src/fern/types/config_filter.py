

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigFilter(UniversalBaseModel):
    app_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only search configurations for this specific Steam App ID (Non-Steam Games use their name as AppID)
    """

    creator: typing.Optional[str] = pydantic.Field(default=None)
    """
    Filter results to only include configurations created by the specified Steam User ID
    """

    excluded_tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Filter results to only include configurations that do not have any of the specified tags
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Filter results to only include configurations with all of the specified tags
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
