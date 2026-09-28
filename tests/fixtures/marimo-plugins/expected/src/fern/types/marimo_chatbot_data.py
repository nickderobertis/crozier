

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_chatbot_data_allow_attachments import MarimoChatbotDataAllowAttachments
from .marimo_chatbot_data_config import MarimoChatbotDataConfig


class MarimoChatbotData(UniversalBaseModel):
    prompts: typing.Optional[typing.List[str]] = None
    show_configuration_controls: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showConfigurationControls"), pydantic.Field(alias="showConfigurationControls")
    ]
    max_height: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxHeight"), pydantic.Field(alias="maxHeight")
    ] = None
    config: MarimoChatbotDataConfig
    allow_attachments: typing_extensions.Annotated[
        MarimoChatbotDataAllowAttachments,
        FieldMetadata(alias="allowAttachments"),
        pydantic.Field(alias="allowAttachments"),
    ]
    disabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
