

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Tax(UniversalBaseModel):
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of the tax.
    """

    employer: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Paid by employer.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the tax.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
