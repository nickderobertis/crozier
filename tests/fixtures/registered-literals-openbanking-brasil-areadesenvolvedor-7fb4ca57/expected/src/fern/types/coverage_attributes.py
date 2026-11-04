

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .coverage_attributes_indemnity_payment_frequencies_item import CoverageAttributesIndemnityPaymentFrequenciesItem
from .coverage_attributes_indemnity_payment_methods_item import CoverageAttributesIndemnityPaymentMethodsItem
from .enum_excluded_risks import EnumExcludedRisks
from .grace_period import GracePeriod
from .insurance_pension_coverage_deductible import InsurancePensionCoverageDeductible
from .insurance_pension_coverage_differentiated_deductible import InsurancePensionCoverageDifferentiatedDeductible
from .insurance_pension_enum_indemnifiable_period_type import InsurancePensionEnumIndemnifiablePeriodType
from .insurance_pension_max_value import InsurancePensionMaxValue
from .insurance_pension_min_value import InsurancePensionMinValue


class CoverageAttributes(UniversalBaseModel):
    """
    Atributos da cobertura
    """

    indemnity_payment_methods: typing_extensions.Annotated[
        typing.Optional[typing.List[CoverageAttributesIndemnityPaymentMethodsItem]],
        FieldMetadata(alias="indemnityPaymentMethods"),
        pydantic.Field(
            alias="indemnityPaymentMethods",
            description="Listagem da forma de pagamento da indenização para cada combinação de modalidade/cobertura do produto",
        ),
    ] = None
    """
    Listagem da forma de pagamento da indenização para cada combinação de modalidade/cobertura do produto
    """

    indemnity_payment_frequencies: typing_extensions.Annotated[
        typing.Optional[typing.List[CoverageAttributesIndemnityPaymentFrequenciesItem]],
        FieldMetadata(alias="indemnityPaymentFrequencies"),
        pydantic.Field(
            alias="indemnityPaymentFrequencies",
            description="Listagem de tipos de frequência de pagamento de indenização para cada combinação de modalidade/cobertura do produto",
        ),
    ] = None
    """
    Listagem de tipos de frequência de pagamento de indenização para cada combinação de modalidade/cobertura do produto
    """

    min_value: typing_extensions.Annotated[
        InsurancePensionMinValue, FieldMetadata(alias="minValue"), pydantic.Field(alias="minValue")
    ]
    max_value: typing_extensions.Annotated[
        InsurancePensionMaxValue, FieldMetadata(alias="maxValue"), pydantic.Field(alias="maxValue")
    ]
    indemnifiable_periods: typing_extensions.Annotated[
        typing.Optional[typing.List[InsurancePensionEnumIndemnifiablePeriodType]],
        FieldMetadata(alias="indemnifiablePeriods"),
        pydantic.Field(alias="indemnifiablePeriods"),
    ] = None
    maximum_qty_indemnifiable_installments: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maximumQtyIndemnifiableInstallments"),
        pydantic.Field(
            alias="maximumQtyIndemnifiableInstallments",
            description="Caso o período indenizável seja relacionado a parcelas, listagem de número máximo de parcelas indenizáveis para cada combinação de modalidade/ cobertura do produto.",
        ),
    ] = None
    """
    Caso o período indenizável seja relacionado a parcelas, listagem de número máximo de parcelas indenizáveis para cada combinação de modalidade/ cobertura do produto.
    """

    grace_period: typing_extensions.Annotated[
        GracePeriod, FieldMetadata(alias="gracePeriod"), pydantic.Field(alias="gracePeriod")
    ]
    differentiated_grace_period: typing_extensions.Annotated[
        typing.Optional[GracePeriod],
        FieldMetadata(alias="differentiatedGracePeriod"),
        pydantic.Field(alias="differentiatedGracePeriod"),
    ] = None
    deductible_days: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="deductibleDays"),
        pydantic.Field(
            alias="deductibleDays",
            description="Listagem de franquia em dias para cada combinação de modalidade/cobertura do produto.",
        ),
    ] = None
    """
    Listagem de franquia em dias para cada combinação de modalidade/cobertura do produto.
    """

    differentiated_deductible_days: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="differentiatedDeductibleDays"),
        pydantic.Field(
            alias="differentiatedDeductibleDays",
            description="Detalhamento da franquia em dias diferentes para cada cobertura que exista alguma especificidade.<br>Caso a seguradora não tenha essa diferenciação, não retornará nada no campo.",
        ),
    ] = None
    """
    Detalhamento da franquia em dias diferentes para cada cobertura que exista alguma especificidade.<br>Caso a seguradora não tenha essa diferenciação, não retornará nada no campo.
    """

    deductible: typing.Optional[InsurancePensionCoverageDeductible] = None
    differentiated_deductible: typing_extensions.Annotated[
        typing.Optional[InsurancePensionCoverageDifferentiatedDeductible],
        FieldMetadata(alias="differentiatedDeductible"),
        pydantic.Field(alias="differentiatedDeductible"),
    ] = None
    excluded_risks: typing_extensions.Annotated[
        typing.Optional[typing.List[EnumExcludedRisks]],
        FieldMetadata(alias="excludedRisks"),
        pydantic.Field(alias="excludedRisks"),
    ] = None
    excluded_risks_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="excludedRisksURL"),
        pydantic.Field(alias="excludedRisksURL", description="Campo aberto (possibilidade de incluir URL)."),
    ] = None
    """
    Campo aberto (possibilidade de incluir URL).
    """

    allow_apart_purchase: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowApartPurchase"),
        pydantic.Field(
            alias="allowApartPurchase", description="Indicar se a cobertura pode ser contratada isoladamente ou não."
        ),
    ] = None
    """
    Indicar se a cobertura pode ser contratada isoladamente ou não.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
