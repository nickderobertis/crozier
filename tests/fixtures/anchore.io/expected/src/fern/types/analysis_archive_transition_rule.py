

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .analysis_archive_transition_rule_exclude import AnalysisArchiveTransitionRuleExclude
from .analysis_archive_transition_rule_transition import AnalysisArchiveTransitionRuleTransition
from .image_selector import ImageSelector


class AnalysisArchiveTransitionRule(UniversalBaseModel):
    """
    A rule for auto-archiving image analysis by time and/or tag-history
    """

    analysis_age_days: typing.Optional[int] = pydantic.Field(default=None)
    """
    Matches if the analysis is strictly older than this number of days
    """

    created_at: typing.Optional[dt.datetime] = None
    exclude: typing.Optional[AnalysisArchiveTransitionRuleExclude] = None
    last_updated: typing.Optional[dt.datetime] = None
    max_images_per_account: typing.Optional[int] = pydantic.Field(default=None)
    """
    This is the maximum number of image analyses an account can have. Can only be set on system_global rules
    """

    rule_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for archive rule
    """

    selector: typing.Optional[ImageSelector] = None
    system_global: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the rule applies to all accounts in the system. This is only available to admin users to update/modify, but all users with permission to list rules can see them
    """

    tag_versions_newer: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of images mapped to the tag that are newer
    """

    transition: AnalysisArchiveTransitionRuleTransition = pydantic.Field()
    """
    The type of transition to make. If "archive", then archive an image from the working set and remove it from the working set. If "delete", then match against archived images and delete from the archive if match.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
