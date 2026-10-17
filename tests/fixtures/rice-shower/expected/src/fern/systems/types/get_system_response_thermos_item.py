

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetSystemResponseThermosItem(UniversalBaseModel):
    channel: float = pydantic.Field()
    """
    Thermometer channel number
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display label for this thermometer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
