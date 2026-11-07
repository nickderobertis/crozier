

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .presentation_network_security import PresentationNetworkSecurity


class PresentationNetworkListResponseDataSupportedSecurityItem(UniversalBaseModel):
    value: PresentationNetworkSecurity
    label: str
    enterprise: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
