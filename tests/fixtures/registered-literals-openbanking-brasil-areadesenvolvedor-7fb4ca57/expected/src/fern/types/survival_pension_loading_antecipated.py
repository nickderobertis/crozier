

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SurvivalPensionLoadingAntecipated(UniversalBaseModel):
    """
    Carregamento antecipado.
    """

    min_value: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="minValue"),
        pydantic.Field(
            alias="minValue",
            description="Percentual mínimo de carregamento cobrada quando do pagamento do prêmio/ contribuição. Em %.",
        ),
    ]
    """
    Percentual mínimo de carregamento cobrada quando do pagamento do prêmio/ contribuição. Em %.
    """

    max_value: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="maxValue"),
        pydantic.Field(
            alias="maxValue",
            description="Percentual máximo de carregamento cobrada quando do pagamento do prêmio/ contribuição. Em %.",
        ),
    ]
    """
    Percentual máximo de carregamento cobrada quando do pagamento do prêmio/ contribuição. Em %.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
