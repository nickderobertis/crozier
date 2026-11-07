

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .version_bump import VersionBump


class AnalyzeCommitDiffResponse(UniversalBaseModel):
    message: str = pydantic.Field()
    """
    The AI-generated commit message summarizing the changes in the diff
    """

    changelog_entry: typing.Optional[str] = pydantic.Field(default=None)
    """
    User-facing release note for CHANGELOG.md and GitHub Releases. Describes the impact on SDK consumers, not implementation details. Empty string for PATCH and NO_CHANGE.
    """

    version_bump: VersionBump = pydantic.Field()
    """
    The recommended semantic version bump: MAJOR for breaking changes, MINOR for new features, PATCH for bug fixes and other changes, NO_CHANGE for empty diffs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
