

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .room_corr_get_response_eq_band_item import RoomCorrGetResponseEqBandItem


class RoomCorrGetResponse(UniversalBaseModel):
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Status of the response, typically "OK" if the request was successful.
    """

    eq_level: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="EQLevel"),
        pydantic.Field(alias="EQLevel", description="The current EQ level setting."),
    ] = None
    """
    The current EQ level setting.
    """

    source_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the current audio source.
    """

    eq_stat: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EQStat"),
        pydantic.Field(alias="EQStat", description='The status of the EQ, such as "On" or "Off".'),
    ] = None
    """
    The status of the EQ, such as "On" or "Off".
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(alias="Name", description="The name of the current room correction profile."),
    ] = None
    """
    The name of the current room correction profile.
    """

    plugin_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pluginURI"),
        pydantic.Field(alias="pluginURI", description="The URI of the plugin used for room correction."),
    ] = None
    """
    The URI of the plugin used for room correction.
    """

    channel_mode: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="channelMode"),
        pydantic.Field(alias="channelMode", description='The channel mode, such as "Stereo".'),
    ] = None
    """
    The channel mode, such as "Stereo".
    """

    eq_band: typing_extensions.Annotated[
        typing.Optional[typing.List[RoomCorrGetResponseEqBandItem]],
        FieldMetadata(alias="EQBand"),
        pydantic.Field(alias="EQBand"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
