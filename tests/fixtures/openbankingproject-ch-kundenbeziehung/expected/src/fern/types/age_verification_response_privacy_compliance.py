

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AgeVerificationResponsePrivacyCompliance(UniversalBaseModel):
    gdpr_compliant: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="gdprCompliant"), pydantic.Field(alias="gdprCompliant")
    ] = None
    data_minimization_applied: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="dataMinimizationApplied"),
        pydantic.Field(alias="dataMinimizationApplied"),
    ] = None
    actual_age_disclosed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="actualAgeDisclosed"), pydantic.Field(alias="actualAgeDisclosed")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
