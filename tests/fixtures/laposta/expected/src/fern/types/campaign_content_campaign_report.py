

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CampaignContentCampaignReport(UniversalBaseModel):
    """
    Alleen bij het vullen van content, en alleen als er iets op te merken viel.
    """

    javascript: typing.Optional[bool] = None
    flash: typing.Optional[bool] = None
    no_unsubscribe: typing.Optional[bool] = None
    empty_unsubscribe: typing.Optional[bool] = None
    css: typing.Optional[typing.List[str]] = None
    images: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
