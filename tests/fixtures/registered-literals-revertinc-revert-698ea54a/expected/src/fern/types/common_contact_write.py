

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .common_contact_association import CommonContactAssociation
from .common_contact_read import CommonContactRead


class CommonContactWrite(CommonContactRead):
    associations: typing.Optional[CommonContactAssociation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
