

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cvssv2scores import Cvssv2Scores
from .cvssv3scores import Cvssv3Scores


class VendorDataObject(UniversalBaseModel):
    cvss_v2: typing.Optional[Cvssv2Scores] = None
    cvss_v3: typing.Optional[Cvssv3Scores] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Vendor Vulnerability ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
