

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Ubo(UniversalBaseModel):
    date_of_birth: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date of birth of the ultimate beneficiary owner.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the ultimate beneficiary owner.
    """

    nationality: typing.Optional[str] = pydantic.Field(default=None)
    """
    The nationality of the ultimate beneficiary owner.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
