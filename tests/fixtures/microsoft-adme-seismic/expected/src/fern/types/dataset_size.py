

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DatasetSize(UniversalBaseModel):
    computed_size: float = pydantic.Field()
    """
    The size of the dataset in bytes..
    """

    computed_size_date: str = pydantic.Field()
    """
    The date of when the dateset size was computed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
