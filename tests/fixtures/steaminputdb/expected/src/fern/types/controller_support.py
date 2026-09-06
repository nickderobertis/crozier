

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ControllerSupport(UniversalBaseModel):
    ds4wired_support: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="ds4_wired_support"), pydantic.Field(alias="ds4_wired_support")
    ] = None
    ds4wireless_support: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="ds4_wireless_support"), pydantic.Field(alias="ds4_wireless_support")
    ] = None
    ds5wired_support: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="ds5_wired_support"), pydantic.Field(alias="ds5_wired_support")
    ] = None
    ds5wireless_support: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="ds5_wireless_support"), pydantic.Field(alias="ds5_wireless_support")
    ] = None
    steam_input_api_support: typing.Optional[bool] = None
    support_level: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
