

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paystub_address import PaystubAddress
from .taxpayer_id import TaxpayerId


class Employee(UniversalBaseModel):
    """
    Data about the employee.
    """

    address: PaystubAddress
    marital_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Marital status of the employee - either `single` or `married`.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the employee.
    """

    taxpayer_id: typing.Optional[TaxpayerId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
