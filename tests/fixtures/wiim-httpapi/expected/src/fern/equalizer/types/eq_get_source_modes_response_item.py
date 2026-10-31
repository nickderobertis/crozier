

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class EqGetSourceModesResponseItem(UniversalBaseModel):
    source_name: typing.Optional[str] = None
    name_lr: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="NameLR"), pydantic.Field(alias="NameLR")
    ] = None
    eq_stat: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="EQStat"), pydantic.Field(alias="EQStat")
    ] = None
    name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Name"), pydantic.Field(alias="Name")
    ] = None
    plugin_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pluginURI"), pydantic.Field(alias="pluginURI")
    ] = None
    channel_mode: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="channelMode"), pydantic.Field(alias="channelMode")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
