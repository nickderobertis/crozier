

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class SurveyGetResultResponse(UniversalBaseModel):
    id: str
    survey_id: typing_extensions.Annotated[str, FieldMetadata(alias="surveyId"), pydantic.Field(alias="surveyId")]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionId"), pydantic.Field(alias="sessionId")]
    payload: typing.Dict[str, typing.Any]
    browser: typing.Optional[str] = None
    os: typing.Optional[str] = None
    language: typing.Optional[str] = None
    ip: typing.Optional[str] = None
    country: typing.Optional[str] = None
    subdivision1: typing.Optional[str] = None
    subdivision2: typing.Optional[str] = None
    city: typing.Optional[str] = None
    longitude: typing.Optional[float] = None
    latitude: typing.Optional[float] = None
    accuracy_radius: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="accuracyRadius"), pydantic.Field(alias="accuracyRadius")
    ] = None
    ai_category: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="aiCategory"), pydantic.Field(alias="aiCategory")
    ] = None
    ai_translation: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="aiTranslation"), pydantic.Field(alias="aiTranslation")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
