

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cable_termination_cable_end import CableTerminationCableEnd


class CableTermination(UniversalBaseModel):
    cable: int
    cable_end: CableTerminationCableEnd
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    termination: typing.Optional[typing.Dict[str, typing.Any]] = None
    termination_id: int
    termination_type: str
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
