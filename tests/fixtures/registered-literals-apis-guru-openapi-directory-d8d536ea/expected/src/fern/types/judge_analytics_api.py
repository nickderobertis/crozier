

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JudgeAnalyticsApi(UniversalBaseModel):
    associated_norm_attorneys_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormAttorneysAPI"), pydantic.Field(alias="associatedNormAttorneysAPI")
    ]
    associated_norm_law_firms_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormLawFirmsAPI"), pydantic.Field(alias="associatedNormLawFirmsAPI")
    ]
    associated_norm_parties_api: typing_extensions.Annotated[
        str, FieldMetadata(alias="associatedNormPartiesAPI"), pydantic.Field(alias="associatedNormPartiesAPI")
    ]
    norm_judge_api: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="normJudgeAPI"),
        pydantic.Field(alias="normJudgeAPI", description="Link to Details for the Judge."),
    ]
    """
    Link to Details for the Judge.
    """

    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
