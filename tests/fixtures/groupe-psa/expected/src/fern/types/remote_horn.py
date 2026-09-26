

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_horn_state import RemoteHornState


class RemoteHorn(UniversalBaseModel):
    """
    Remote vehicle horn activation.
    """

    state: RemoteHornState = pydantic.Field()
    """
    Activate or unactivate this remote horn.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
