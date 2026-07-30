

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency import Currency


class JobSalary(UniversalBaseModel):
    currency: typing.Optional[Currency] = None
    max: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum salary payable for the job role.
    """

    min: typing.Optional[int] = pydantic.Field(default=None)
    """
    Minimum salary payable for the job role.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
