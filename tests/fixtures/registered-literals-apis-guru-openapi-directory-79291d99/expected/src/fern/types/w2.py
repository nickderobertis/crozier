

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .employee import Employee
from .paystub_employer import PaystubEmployer
from .w2box12 import W2Box12
from .w2state_and_local_wages import W2StateAndLocalWages


class W2(UniversalBaseModel):
    """
    W2 is an object that represents income data taken from a W2 tax document.
    """

    allocated_tips: typing.Optional[str] = pydantic.Field(default=None)
    """
    Allocated tips.
    """

    box12: typing_extensions.Annotated[
        typing.Optional[typing.List[W2Box12]], FieldMetadata(alias="box_12"), pydantic.Field(alias="box_12")
    ] = None
    box9: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="box_9"),
        pydantic.Field(alias="box_9", description="Contents from box 9 on the W2."),
    ] = None
    """
    Contents from box 9 on the W2.
    """

    dependent_care_benefits: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dependent care benefits.
    """

    employee: typing.Optional[Employee] = None
    employer: typing.Optional[PaystubEmployer] = None
    employer_id_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    An employee identification number or EIN.
    """

    federal_income_tax_withheld: typing.Optional[str] = pydantic.Field(default=None)
    """
    Federal income tax withheld for the tax year.
    """

    medicare_tax_withheld: typing.Optional[str] = pydantic.Field(default=None)
    """
    Medicare tax withheld for the tax year.
    """

    medicare_wages_and_tips: typing.Optional[str] = pydantic.Field(default=None)
    """
    Wages and tips from medicare.
    """

    nonqualified_plans: typing.Optional[str] = pydantic.Field(default=None)
    """
    Nonqualified plans.
    """

    other: typing.Optional[str] = pydantic.Field(default=None)
    """
    Other.
    """

    retirement_plan: typing.Optional[str] = pydantic.Field(default=None)
    """
    Retirement plan.
    """

    social_security_tax_withheld: typing.Optional[str] = pydantic.Field(default=None)
    """
    Social security tax withheld for the tax year.
    """

    social_security_tips: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tips from social security.
    """

    social_security_wages: typing.Optional[str] = pydantic.Field(default=None)
    """
    Wages from social security.
    """

    state_and_local_wages: typing.Optional[typing.List[W2StateAndLocalWages]] = None
    statutory_employee: typing.Optional[str] = pydantic.Field(default=None)
    """
    Statutory employee.
    """

    tax_year: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tax year of the W2 document.
    """

    third_party_sick_pay: typing.Optional[str] = pydantic.Field(default=None)
    """
    Third party sick pay.
    """

    wages_tips_other_comp: typing.Optional[str] = pydantic.Field(default=None)
    """
    Wages from tips and other compensation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
