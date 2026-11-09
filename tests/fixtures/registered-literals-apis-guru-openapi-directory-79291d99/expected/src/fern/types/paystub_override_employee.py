

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paystub_override_employee_address import PaystubOverrideEmployeeAddress


class PaystubOverrideEmployee(UniversalBaseModel):
    """
    The employee on the paystub.
    """

    address: typing.Optional[PaystubOverrideEmployeeAddress] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the employee.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
