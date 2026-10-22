

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SurveyWelcomeCard(UniversalBaseModel):
    """
    The welcome card configuration
    """

    enabled: bool
    time_to_finish: typing_extensions.Annotated[
        bool, FieldMetadata(alias="timeToFinish"), pydantic.Field(alias="timeToFinish")
    ]
    show_response_count: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showResponseCount"), pydantic.Field(alias="showResponseCount")
    ]
    headline: typing.Optional[typing.Dict[str, str]] = None
    subheader: typing.Optional[typing.Dict[str, str]] = None
    file_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fileUrl"), pydantic.Field(alias="fileUrl")
    ] = None
    button_label: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="buttonLabel"), pydantic.Field(alias="buttonLabel")
    ] = None
    video_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoUrl"), pydantic.Field(alias="videoUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
