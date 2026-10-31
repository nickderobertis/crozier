

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetActiveSoundCardOutputModeResponse(UniversalBaseModel):
    index: typing.Optional[str] = pydantic.Field(default=None)
    """
    The index of the active sound card output mode
    """

    mode: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the active sound card output mode
    """

    card_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cardId"),
        pydantic.Field(alias="cardId", description="The card ID of the active sound card output mode"),
    ] = None
    """
    The card ID of the active sound card output mode
    """

    dev_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="devName"),
        pydantic.Field(alias="devName", description="The device name of the active sound card output mode"),
    ] = None
    """
    The device name of the active sound card output mode
    """

    bt_source: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="btSource"), pydantic.Field(alias="btSource", description="Unknown")
    ] = None
    """
    Unknown
    """

    audio_cast: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="audioCast"), pydantic.Field(alias="audioCast", description="Unknown")
    ] = None
    """
    Unknown
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
