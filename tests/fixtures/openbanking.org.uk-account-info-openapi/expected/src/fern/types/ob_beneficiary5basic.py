

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .beneficiary_id import BeneficiaryId
from .ob_beneficiary_type1code import ObBeneficiaryType1Code
from .ob_supplementary_data1 import ObSupplementaryData1
from .reference import Reference


class ObBeneficiary5Basic(UniversalBaseModel):
    account_id: typing_extensions.Annotated[
        typing.Optional[AccountId], FieldMetadata(alias="AccountId"), pydantic.Field(alias="AccountId")
    ] = None
    beneficiary_id: typing_extensions.Annotated[
        typing.Optional[BeneficiaryId], FieldMetadata(alias="BeneficiaryId"), pydantic.Field(alias="BeneficiaryId")
    ] = None
    beneficiary_type: typing_extensions.Annotated[
        typing.Optional[ObBeneficiaryType1Code],
        FieldMetadata(alias="BeneficiaryType"),
        pydantic.Field(alias="BeneficiaryType"),
    ] = None
    reference: typing_extensions.Annotated[
        typing.Optional[Reference], FieldMetadata(alias="Reference"), pydantic.Field(alias="Reference")
    ] = None
    supplementary_data: typing_extensions.Annotated[
        typing.Optional[ObSupplementaryData1],
        FieldMetadata(alias="SupplementaryData"),
        pydantic.Field(alias="SupplementaryData"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
