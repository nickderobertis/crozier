

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .button import Button
from .form_title_payload_cover_settings import FormTitlePayloadCoverSettings
from .html import Html
from .mention import Mention


class FormTitlePayload(UniversalBaseModel):
    """
    Payload for FORM_TITLE block type. Used for the main form title with optional logo and cover image.
    """

    html: typing.Optional[Html] = None
    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the logo image displayed as form branding. Recommended size: 200x200 pixels. Rendered as a circular image.
    """

    cover: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of a full-width cover image displayed at the top of the form. Recommended minimum width: 1500 pixels.
    """

    cover_settings: typing_extensions.Annotated[
        typing.Optional[FormTitlePayloadCoverSettings],
        FieldMetadata(alias="coverSettings"),
        pydantic.Field(alias="coverSettings"),
    ] = None
    mentions: typing.Optional[typing.List[Mention]] = None
    button: typing.Optional[Button] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
