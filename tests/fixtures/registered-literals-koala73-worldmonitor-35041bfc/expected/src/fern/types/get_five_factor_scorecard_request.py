

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetFiveFactorScorecardRequest(UniversalBaseModel):
    country_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="countryCode"),
        pydantic.Field(alias="countryCode", description="ISO 3166-1 alpha-2 country code for the requested scorecard."),
    ]
    """
    ISO 3166-1 alpha-2 country code for the requested scorecard.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
