

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sequence_create_request_data_attributes import SequenceCreateRequestDataAttributes


class SequenceCreateRequestData(UniversalBaseModel):
    type: str
    attributes: SequenceCreateRequestDataAttributes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
