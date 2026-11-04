

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .time_ns_deployment_time import TimeNsDeploymentTime


class Time(UniversalBaseModel):
    """
    The Slice Deployment time
    """

    ns_deployment_time: typing_extensions.Annotated[
        typing.Optional[TimeNsDeploymentTime],
        FieldMetadata(alias="NS_Deployment_Time"),
        pydantic.Field(alias="NS_Deployment_Time"),
    ] = None
    placement_time: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Placement_Time"),
        pydantic.Field(alias="Placement_Time", description="Seconds"),
    ] = None
    """
    Seconds
    """

    provisioning_time: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Provisioning_Time"),
        pydantic.Field(alias="Provisioning_Time", description="Seconds"),
    ] = None
    """
    Seconds
    """

    radio_configuration_time: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Radio_Configuration_Time"),
        pydantic.Field(alias="Radio_Configuration_Time", description="Seconds"),
    ] = None
    """
    Seconds
    """

    slice_deployment_time: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Slice_Deployment_Time"),
        pydantic.Field(alias="Slice_Deployment_Time", description="Seconds"),
    ] = None
    """
    Seconds
    """

    wan_deployment_time: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="WAN_Deployment_Time"),
        pydantic.Field(alias="WAN_Deployment_Time", description="Seconds"),
    ] = None
    """
    Seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
