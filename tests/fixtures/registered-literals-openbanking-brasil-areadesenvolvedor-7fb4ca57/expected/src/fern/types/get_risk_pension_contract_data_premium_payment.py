

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_risk_pension_contract_data_premium_payment_frequencies_item import (
    GetRiskPensionContractDataPremiumPaymentFrequenciesItem,
)
from .get_risk_pension_contract_data_premium_payment_payment_methods_item import (
    GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem,
)


class GetRiskPensionContractDataPremiumPayment(UniversalBaseModel):
    payment_methods: typing_extensions.Annotated[
        typing.List[GetRiskPensionContractDataPremiumPaymentPaymentMethodsItem],
        FieldMetadata(alias="paymentMethods"),
        pydantic.Field(alias="paymentMethods"),
    ]
    frequencies: typing.List[GetRiskPensionContractDataPremiumPaymentFrequenciesItem]
    contribution_tax: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contributionTax"),
        pydantic.Field(
            alias="contributionTax",
            description="Distribuição de frequência relativa aos valores referentes às taxas cobradas, nos termos do Anexo III.",
        ),
    ] = None
    """
    Distribuição de frequência relativa aos valores referentes às taxas cobradas, nos termos do Anexo III.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
