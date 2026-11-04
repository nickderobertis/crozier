

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attachment_permalink_match_result import AttachmentPermalinkMatchResult


class AttachmentPermalinkMatchList(UniversalBaseModel):
    """
    Ordered Attachment permalink match results.
    """

    items: typing.Optional[typing.List[AttachmentPermalinkMatchResult]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
