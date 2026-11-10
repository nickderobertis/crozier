

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .income_verification_payroll_flow_type import IncomeVerificationPayrollFlowType


class LinkTokenCreateRequestIncomeVerificationPayrollIncome(UniversalBaseModel):
    """
    Specifies options for initializing Link for use with Payroll Income.
    """

    flow_types: typing.Optional[typing.List[IncomeVerificationPayrollFlowType]] = pydantic.Field(default=None)
    """
    The types of payroll income verification to enable for the Link session. If none are specified, then users will see both document and digital payroll income.
    """

    is_update_mode: typing.Optional[bool] = pydantic.Field(default=None)
    """
    An identifier to indicate whether the income verification Link token will be used for an update or not
    """

    item_id_to_update: typing.Optional[str] = pydantic.Field(default=None)
    """
    Uniquely identify a payroll income item to update with. It should only be used for update mode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
