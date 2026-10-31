

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .campaign_content_campaign_report import CampaignContentCampaignReport


class CampaignContentCampaign(UniversalBaseModel):
    account_id: typing.Optional[str] = None
    campaign_id: typing.Optional[str] = None
    html: typing.Optional[str] = None
    plaintext: typing.Optional[str] = None
    report: typing.Optional[CampaignContentCampaignReport] = pydantic.Field(default=None)
    """
    Alleen bij het vullen van content, en alleen als er iets op te merken viel.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
