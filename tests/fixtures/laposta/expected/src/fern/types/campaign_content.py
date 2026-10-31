

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .campaign_content_campaign import CampaignContentCampaign


class CampaignContent(UniversalBaseModel):
    """
    The content of a campaign in html and in plain text.
    """

    campaign: typing.Optional[CampaignContentCampaign] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
