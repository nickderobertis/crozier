

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .kyc_check_address_summary import KycCheckAddressSummary
from .kyc_check_date_of_birth_summary import KycCheckDateOfBirthSummary
from .kyc_check_id_number_summary import KycCheckIdNumberSummary
from .kyc_check_name_summary import KycCheckNameSummary
from .kyc_check_phone_summary import KycCheckPhoneSummary


class KycCheckDetails(UniversalBaseModel):
    """
    Additional information for the `kyc_check` step. This field will be `null` unless `steps.kyc_check` has reached a terminal state of either `success` or `failed`.
    """

    address: KycCheckAddressSummary
    date_of_birth: KycCheckDateOfBirthSummary
    id_number: KycCheckIdNumberSummary
    name: KycCheckNameSummary
    phone_number: KycCheckPhoneSummary
    status: str = pydantic.Field()
    """
    The outcome status for the associated Identity Verification attempt's `kyc_check` step. This field will always have the same value as `steps.kyc_check`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
