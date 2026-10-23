

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .survey_styling_background import SurveyStylingBackground
from .survey_styling_brand_color import SurveyStylingBrandColor
from .survey_styling_card_arrangement import SurveyStylingCardArrangement
from .survey_styling_card_background_color import SurveyStylingCardBackgroundColor
from .survey_styling_card_border_color import SurveyStylingCardBorderColor
from .survey_styling_highlight_border_color import SurveyStylingHighlightBorderColor
from .survey_styling_input_border_color import SurveyStylingInputBorderColor
from .survey_styling_logo import SurveyStylingLogo


class SurveyStyling(UniversalBaseModel):
    """
    Survey styling configuration
    """

    brand_color: typing_extensions.Annotated[
        typing.Optional[SurveyStylingBrandColor], FieldMetadata(alias="brandColor"), pydantic.Field(alias="brandColor")
    ] = None
    input_border_color: typing_extensions.Annotated[
        typing.Optional[SurveyStylingInputBorderColor],
        FieldMetadata(alias="inputBorderColor"),
        pydantic.Field(alias="inputBorderColor"),
    ] = None
    card_background_color: typing_extensions.Annotated[
        typing.Optional[SurveyStylingCardBackgroundColor],
        FieldMetadata(alias="cardBackgroundColor"),
        pydantic.Field(alias="cardBackgroundColor"),
    ] = None
    card_border_color: typing_extensions.Annotated[
        typing.Optional[SurveyStylingCardBorderColor],
        FieldMetadata(alias="cardBorderColor"),
        pydantic.Field(alias="cardBorderColor"),
    ] = None
    highlight_border_color: typing_extensions.Annotated[
        typing.Optional[SurveyStylingHighlightBorderColor],
        FieldMetadata(alias="highlightBorderColor"),
        pydantic.Field(alias="highlightBorderColor"),
    ] = None
    is_dark_mode_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDarkModeEnabled"), pydantic.Field(alias="isDarkModeEnabled")
    ] = None
    roundness: typing.Optional[float] = None
    card_arrangement: typing_extensions.Annotated[
        typing.Optional[SurveyStylingCardArrangement],
        FieldMetadata(alias="cardArrangement"),
        pydantic.Field(alias="cardArrangement"),
    ] = None
    background: typing.Optional[SurveyStylingBackground] = None
    hide_progress_bar: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hideProgressBar"), pydantic.Field(alias="hideProgressBar")
    ] = None
    is_logo_hidden: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isLogoHidden"), pydantic.Field(alias="isLogoHidden")
    ] = None
    logo: typing.Optional[SurveyStylingLogo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
