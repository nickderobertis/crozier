

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survival_pension_loading_antecipated import SurvivalPensionLoadingAntecipated
from .survival_pension_loading_late import SurvivalPensionLoadingLate


class SurvivalPensionCosts(UniversalBaseModel):
    """
    Custos
    """

    loading_antecipated: typing_extensions.Annotated[
        SurvivalPensionLoadingAntecipated,
        FieldMetadata(alias="loadingAntecipated"),
        pydantic.Field(alias="loadingAntecipated"),
    ]
    loading_late: typing_extensions.Annotated[
        SurvivalPensionLoadingLate, FieldMetadata(alias="loadingLate"), pydantic.Field(alias="loadingLate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
