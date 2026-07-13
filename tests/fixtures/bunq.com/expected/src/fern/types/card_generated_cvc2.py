

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CardGeneratedCvc2(UniversalBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of generated cvc2. Can be STATIC or GENERATED.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
