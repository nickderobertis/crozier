

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .applicant_websites_item_type import ApplicantWebsitesItemType


class ApplicantWebsitesItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    type: typing.Optional[ApplicantWebsitesItemType] = None
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
