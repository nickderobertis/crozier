

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .notification_control import NotificationControl


class GbrQosFlowInformation(UniversalBaseModel):
    max_fbr_dl: typing_extensions.Annotated[str, FieldMetadata(alias="maxFbrDl"), pydantic.Field(alias="maxFbrDl")]
    max_fbr_ul: typing_extensions.Annotated[str, FieldMetadata(alias="maxFbrUl"), pydantic.Field(alias="maxFbrUl")]
    gua_fbr_dl: typing_extensions.Annotated[str, FieldMetadata(alias="guaFbrDl"), pydantic.Field(alias="guaFbrDl")]
    gua_fbr_ul: typing_extensions.Annotated[str, FieldMetadata(alias="guaFbrUl"), pydantic.Field(alias="guaFbrUl")]
    notif_control: typing_extensions.Annotated[
        typing.Optional[NotificationControl], FieldMetadata(alias="notifControl"), pydantic.Field(alias="notifControl")
    ] = None
    max_packet_loss_rate_dl: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxPacketLossRateDl"), pydantic.Field(alias="maxPacketLossRateDl")
    ] = None
    max_packet_loss_rate_ul: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxPacketLossRateUl"), pydantic.Field(alias="maxPacketLossRateUl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
