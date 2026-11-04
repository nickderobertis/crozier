

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cnpj_number import CnpjNumber


class Participant(UniversalBaseModel):
    """
    Conjunto de informações relativas ao participante do produto de open banking
    """

    brand: str = pydantic.Field()
    """
    Nome da marca reportada pelo participante do Open Banking. O conceito a que se refere a 'marca' é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes.
    """

    name: str = pydantic.Field()
    """
    Nome do participante do Open Banking.
    """

    cnpj_number: typing_extensions.Annotated[
        CnpjNumber, FieldMetadata(alias="cnpjNumber"), pydantic.Field(alias="cnpjNumber")
    ]
    url_complementary_list: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="urlComplementaryList"), pydantic.Field(alias="urlComplementaryList")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
