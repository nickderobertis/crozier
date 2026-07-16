

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .beneficiary_id import BeneficiaryId
from .ob_beneficiary_type1code import ObBeneficiaryType1Code
from .ob_branch_and_financial_institution_identification60 import ObBranchAndFinancialInstitutionIdentification60
from .ob_cash_account50 import ObCashAccount50
from .ob_supplementary_data1 import ObSupplementaryData1
from .reference import Reference


class ObBeneficiary5(UniversalBaseModel):
    account_id: typing_extensions.Annotated[typing.Optional[AccountId], FieldMetadata(alias="AccountId")] = None
    beneficiary_id: typing_extensions.Annotated[
        typing.Optional[BeneficiaryId], FieldMetadata(alias="BeneficiaryId")
    ] = None
    beneficiary_type: typing_extensions.Annotated[
        typing.Optional[ObBeneficiaryType1Code], FieldMetadata(alias="BeneficiaryType")
    ] = None
    creditor_account: typing_extensions.Annotated[
        typing.Optional[ObCashAccount50], FieldMetadata(alias="CreditorAccount")
    ] = None
    creditor_agent: typing_extensions.Annotated[
        typing.Optional[ObBranchAndFinancialInstitutionIdentification60], FieldMetadata(alias="CreditorAgent")
    ] = None
    reference: typing_extensions.Annotated[typing.Optional[Reference], FieldMetadata(alias="Reference")] = None
    supplementary_data: typing_extensions.Annotated[
        typing.Optional[ObSupplementaryData1], FieldMetadata(alias="SupplementaryData")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
