

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SurvivalPensionLoadingLate(UniversalBaseModel):
    """
    Carregamento postecipado.
    """

    min_value: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="minValue"),
        pydantic.Field(
            alias="minValue",
            description="Percentual mínimo de taxa de carregamento cobrado quando da efetivação de resgate ou portabilidade.",
        ),
    ]
    """
    Percentual mínimo de taxa de carregamento cobrado quando da efetivação de resgate ou portabilidade.
    """

    max_value: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="maxValue"),
        pydantic.Field(
            alias="maxValue",
            description="Percentual máximo de taxa de carregamento cobrado quando da efetivação de resgate ou portabilidade.",
        ),
    ]
    """
    Percentual máximo de taxa de carregamento cobrado quando da efetivação de resgate ou portabilidade.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
