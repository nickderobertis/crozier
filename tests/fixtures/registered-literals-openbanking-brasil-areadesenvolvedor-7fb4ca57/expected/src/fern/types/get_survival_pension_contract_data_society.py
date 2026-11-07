

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cnpj_number import CnpjNumber


class GetSurvivalPensionContractDataSociety(UniversalBaseModel):
    """
    Conjunto de informações relativas à seguradora do produto de open insurance
    """

    name: str = pydantic.Field()
    """
    Nome da Sociedade Seguradora.
    """

    cnpj_number: typing_extensions.Annotated[
        CnpjNumber, FieldMetadata(alias="cnpjNumber"), pydantic.Field(alias="cnpjNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
