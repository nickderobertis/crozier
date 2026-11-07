

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SourceChargeAdditionalData(UniversalBaseModel):
    """
    Additional data that enchances the information of a given charge.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    type: str = pydantic.Field()
    """
    Describes what type of additional data.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Value of additional data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
