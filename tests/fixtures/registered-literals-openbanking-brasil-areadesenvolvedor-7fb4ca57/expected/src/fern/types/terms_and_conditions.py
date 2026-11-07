

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .susep_process_number import SusepProcessNumber


class TermsAndConditions(UniversalBaseModel):
    susep_process_number: typing_extensions.Annotated[
        SusepProcessNumber, FieldMetadata(alias="susepProcessNumber"), pydantic.Field(alias="susepProcessNumber")
    ]
    detail: str = pydantic.Field()
    """
    Representam as Condições Gerais, Condições Especiais e Condições ou Cláusulas Particulares de um mesmo produto. (Circular SUSEP 321/06). Campo aberto (possibilidade de incluir URL)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
