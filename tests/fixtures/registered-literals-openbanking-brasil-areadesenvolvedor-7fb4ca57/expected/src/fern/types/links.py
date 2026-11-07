

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Links(UniversalBaseModel):
    """
    Referências para outros recusos da API requisitada.
    """

    self_: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="URI completo que gerou a resposta atual."),
    ]
    """
    URI completo que gerou a resposta atual.
    """

    first: typing.Optional[str] = pydantic.Field(default=None)
    """
    URI da primeira página que originou essa lista de resultados. Restrição - Obrigatório quando não for a primeira página da resposta
    """

    prev: typing.Optional[str] = pydantic.Field(default=None)
    """
    URI da página anterior dessa lista de resultados. Restrição -     Obrigatório quando não for a primeira página da resposta
    """

    next: typing.Optional[str] = pydantic.Field(default=None)
    """
    URI da próxima página dessa lista de resultados. Restrição - Obrigatório quando não for a última página da resposta
    """

    last: typing.Optional[str] = pydantic.Field(default=None)
    """
    URI da última página dessa lista de resultados. Restrição - Obrigatório quando não for a última página da resposta
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
