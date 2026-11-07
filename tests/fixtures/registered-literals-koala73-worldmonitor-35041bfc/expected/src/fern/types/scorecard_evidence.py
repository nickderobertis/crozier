

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .scorecard_observation import ScorecardObservation


class ScorecardEvidence(UniversalBaseModel):
    input_id: typing_extensions.Annotated[str, FieldMetadata(alias="inputId"), pydantic.Field(alias="inputId")]
    available: bool
    value: float
    has_value: typing_extensions.Annotated[bool, FieldMetadata(alias="hasValue"), pydantic.Field(alias="hasValue")]
    year: int
    unit: str
    source: str
    source_key: typing_extensions.Annotated[str, FieldMetadata(alias="sourceKey"), pydantic.Field(alias="sourceKey")]
    unavailable_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="unavailableReason"), pydantic.Field(alias="unavailableReason")
    ]
    quality: str
    observations: typing.List[ScorecardObservation]
    country_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="countryCode"),
        pydantic.Field(
            alias="countryCode",
            description="ISO-2 member that supplied this evidence. Empty only on a country scorecard.",
        ),
    ]
    """
    ISO-2 member that supplied this evidence. Empty only on a country scorecard.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
