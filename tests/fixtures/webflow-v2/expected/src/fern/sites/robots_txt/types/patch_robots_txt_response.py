

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patch_robots_txt_response_rules_item import PatchRobotsTxtResponseRulesItem


class PatchRobotsTxtResponse(UniversalBaseModel):
    """
    The robots.txt file for a given site
    """

    rules: typing.Optional[typing.List[PatchRobotsTxtResponseRulesItem]] = pydantic.Field(default=None)
    """
    List of rules for user agents.
    """

    sitemap: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to the sitemap.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
