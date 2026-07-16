

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SuperMembership(UniversalBaseModel):
    employee_number: typing_extensions.Annotated[str, FieldMetadata(alias="EmployeeNumber")] = pydantic.Field()
    """
    The membership number assigned to the employee by the super fund.
    """

    super_fund_id: typing_extensions.Annotated[str, FieldMetadata(alias="SuperFundID")] = pydantic.Field()
    """
    Xero identifier for super fund
    """

    super_membership_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="SuperMembershipID")] = (
        pydantic.Field(default=None)
    )
    """
    Xero unique identifier for Super membership
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
