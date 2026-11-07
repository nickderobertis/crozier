

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cnpj_number import CnpjNumber
from .currency_code import CurrencyCode
from .survival_pension_investiment_fund_type_performance_fee import SurvivalPensionInvestimentFundTypePerformanceFee


class SurvivalPensionInvestimentFund(UniversalBaseModel):
    """
    Fundos de Investimento (por fundo).
    """

    cnpj_number: typing_extensions.Annotated[
        typing.Optional[CnpjNumber], FieldMetadata(alias="cnpjNumber"), pydantic.Field(alias="cnpjNumber")
    ] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:
    - Nome Fantasia
    """

    maximum_administration_fee: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="maximumAdministrationFee"),
        pydantic.Field(
            alias="maximumAdministrationFee",
            description="Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:\n  - Taxa Máxima de Administração - em %",
        ),
    ] = None
    """
    Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:
      - Taxa Máxima de Administração - em %
    """

    type_performance_fee: typing_extensions.Annotated[
        typing.Optional[SurvivalPensionInvestimentFundTypePerformanceFee],
        FieldMetadata(alias="typePerformanceFee"),
        pydantic.Field(
            alias="typePerformanceFee",
            description="Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:\n   - Tipo de taxa de performance",
        ),
    ] = None
    """
    Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:
       - Tipo de taxa de performance
    """

    maximum_performance_fee: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="maximumPerformanceFee"),
        pydantic.Field(
            alias="maximumPerformanceFee",
            description="Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando: \n  - Taxa Máxima de Performance - em %",
        ),
    ] = None
    """
    Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando: 
      - Taxa Máxima de Performance - em %
    """

    eligibility_rule: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="eligibilityRule"),
        pydantic.Field(
            alias="eligibilityRule",
            description="Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:\n  - Regra de Elegibilidade",
        ),
    ] = None
    """
    Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando:
      - Regra de Elegibilidade
    """

    minimum_contribution_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minimumContributionAmount"),
        pydantic.Field(
            alias="minimumContributionAmount",
            description="Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando: \n  - Valor Mínimo de Contribuição",
        ),
    ] = None
    """
    Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando: 
      - Valor Mínimo de Contribuição
    """

    minimum_mathematical_provision_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minimumMathematicalProvisionAmount"),
        pydantic.Field(
            alias="minimumMathematicalProvisionAmount",
            description="Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando: \n  - Valor Mínimo do Saldo Provisão matemática",
        ),
    ] = None
    """
    Lista com as informações do(s) Fundo(s) de Investimento(s) disponíveis para o período de diferimento/acumulação, contemplando: 
      - Valor Mínimo do Saldo Provisão matemática
    """

    currency: typing.Optional[CurrencyCode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
