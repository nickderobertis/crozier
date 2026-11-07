

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .coverage_attributes import CoverageAttributes
from .enum_risk_pension_coverage_type import EnumRiskPensionCoverageType


class Coverage(UniversalBaseModel):
    type: EnumRiskPensionCoverageType
    type_additional_infos: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="typeAdditionalInfos"),
        pydantic.Field(
            alias="typeAdditionalInfos",
            description="Lista de textos para complementar informação relativa ao campo type, quando for selecionada a opção 'OUTROS'.\nRestrição: Campo de preenchimento obrigatório se 'type' estiver preenchida a opção 'OUTROS'",
        ),
    ] = None
    """
    Lista de textos para complementar informação relativa ao campo type, quando for selecionada a opção 'OUTROS'.
    Restrição: Campo de preenchimento obrigatório se 'type' estiver preenchida a opção 'OUTROS'
    """

    attributes: CoverageAttributes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
