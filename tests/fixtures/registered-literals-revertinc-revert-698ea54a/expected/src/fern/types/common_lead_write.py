

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .common_lead_association import CommonLeadAssociation
from .common_lead_read import CommonLeadRead


class CommonLeadWrite(CommonLeadRead):
    associations: typing.Optional[CommonLeadAssociation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
