

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetPersonalizedSurveyLinkResponseData(UniversalBaseModel):
    survey_url: typing_extensions.Annotated[str, FieldMetadata(alias="surveyUrl"), pydantic.Field(alias="surveyUrl")]
    expires_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="The date and time the link expires, null if no expiration"),
    ] = None
    """
    The date and time the link expires, null if no expiration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
