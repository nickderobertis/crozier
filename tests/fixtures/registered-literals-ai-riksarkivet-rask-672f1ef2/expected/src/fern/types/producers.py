

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .producer_info import ProducerInfo


class Producers(UniversalBaseModel):
    """
    The runs that produced ``dataset``.
    """

    dataset: str
    producers: typing.List[ProducerInfo]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
