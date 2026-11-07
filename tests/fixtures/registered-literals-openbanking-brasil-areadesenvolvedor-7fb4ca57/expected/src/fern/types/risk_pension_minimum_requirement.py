

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .risk_pension_minimum_requirement_contract_type import RiskPensionMinimumRequirementContractType


class RiskPensionMinimumRequirement(UniversalBaseModel):
    contract_type: typing_extensions.Annotated[
        RiskPensionMinimumRequirementContractType,
        FieldMetadata(alias="contractType"),
        pydantic.Field(
            alias="contractType",
            description="O tipo de serviço contratado. A considerar os domínios abaixo&#58;<br><ol><li>Coletivo Averbado</li><li>Coletivo Instituído</li><li>Individual</li></ol>",
        ),
    ]
    """
    O tipo de serviço contratado. A considerar os domínios abaixo&#58;<br><ol><li>Coletivo Averbado</li><li>Coletivo Instituído</li><li>Individual</li></ol>
    """

    contracting_min_requirement: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contractingMinRequirement"),
        pydantic.Field(
            alias="contractingMinRequirement",
            description="Campo aberto contendo todos os requisitos mínimos para contratação (possibilidade de incluir URL).",
        ),
    ] = None
    """
    Campo aberto contendo todos os requisitos mínimos para contratação (possibilidade de incluir URL).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
