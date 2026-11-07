

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survival_pension_minimum_requirements_contract_type import SurvivalPensionMinimumRequirementsContractType


class SurvivalPensionMinimumRequirements(UniversalBaseModel):
    contract_type: typing_extensions.Annotated[
        SurvivalPensionMinimumRequirementsContractType,
        FieldMetadata(alias="contractType"),
        pydantic.Field(
            alias="contractType",
            description="O tipo de serviço contratado. A considerar os domínios abaixo:\n1. Coletivo Averbado;\n2. Individual.\n3. Ambas",
        ),
    ]
    """
    O tipo de serviço contratado. A considerar os domínios abaixo:
    1. Coletivo Averbado;
    2. Individual.
    3. Ambas
    """

    participant_qualified: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="participantQualified"),
        pydantic.Field(
            alias="participantQualified",
            description="Indicação se o plano é destinado para participante qualificado. A considerar os domínios abaixo:\n1. true\n2. false",
        ),
    ]
    """
    Indicação se o plano é destinado para participante qualificado. A considerar os domínios abaixo:
    1. true
    2. false
    """

    contracting_min_requirement: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contractingMinRequirement"),
        pydantic.Field(alias="contractingMinRequirement", description="Campo aberto (possibilidade de incluir URL)"),
    ] = None
    """
    Campo aberto (possibilidade de incluir URL)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
