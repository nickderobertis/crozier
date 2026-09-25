

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_doors_state_state import RemoteDoorsStateState


class RemoteDoorsState(UniversalBaseModel):
    """
    Remote vehicle door (lock/unlock) state.
    _Disclaimer_ : "Forced" parameter is only applicable to lock the doors and is now deprecated because not applicable to all vehicles. It will be ignored to unlock the doors if set.
    Some additionnal details will be added in the callback when this parameter is considered.
    """

    state: RemoteDoorsStateState
    forced: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
