

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .common_event_association import CommonEventAssociation
from .common_event_read import CommonEventRead


class CommonEventWrite(CommonEventRead):
    associations: typing.Optional[CommonEventAssociation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
