

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remote_stolen_immobilization import RemoteStolenImmobilization
from .remote_stolen_tracking_period import RemoteStolenTrackingPeriod


class RemoteStolen(UniversalBaseModel):
    """
    Remote operation to update stolen state, immobilization and configuration information. Only one attribute can be used at a time.
    """

    stolen: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Declare the vehicle stolen or not (set at ```True``` to report as stolen).
    """

    tracking_period: typing_extensions.Annotated[
        typing.Optional[RemoteStolenTrackingPeriod],
        FieldMetadata(alias="trackingPeriod"),
        pydantic.Field(
            alias="trackingPeriod",
            description="Modify vehicle data collection frequency through tracking timer attributes.",
        ),
    ] = None
    """
    Modify vehicle data collection frequency through tracking timer attributes.
    """

    immobilization: typing.Optional[RemoteStolenImmobilization] = pydantic.Field(default=None)
    """
    Requesting the stolen vehicle for immobilization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
