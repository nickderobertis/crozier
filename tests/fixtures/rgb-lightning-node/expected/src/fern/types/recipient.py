

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assignment import Assignment
from .witness_data import WitnessData


class Recipient(UniversalBaseModel):
    recipient_id: str
    witness_data: typing.Optional[WitnessData] = None
    assignment: Assignment
    transport_endpoints: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
