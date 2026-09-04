

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .risk_profile_esg_preferences_esg_importance import RiskProfileEsgPreferencesEsgImportance


class RiskProfileEsgPreferences(UniversalBaseModel):
    consider_esg_factors: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="considerEsgFactors"), pydantic.Field(alias="considerEsgFactors")
    ] = None
    esg_importance: typing_extensions.Annotated[
        typing.Optional[RiskProfileEsgPreferencesEsgImportance],
        FieldMetadata(alias="esgImportance"),
        pydantic.Field(alias="esgImportance"),
    ] = None
    exclusions: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
