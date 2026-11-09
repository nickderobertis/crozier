

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_screening_hit_emails import EntityScreeningHitEmails
from .match_summary import MatchSummary


class EntityScreeningHitEmailsItems(UniversalBaseModel):
    """
    Analyzed emails for the associated hit
    """

    analysis: typing.Optional[MatchSummary] = None
    data: typing.Optional[EntityScreeningHitEmails] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
