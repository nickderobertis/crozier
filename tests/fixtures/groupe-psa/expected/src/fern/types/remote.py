

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remote_charging import RemoteCharging
from .remote_doors_state import RemoteDoorsState
from .remote_horn import RemoteHorn
from .remote_lights import RemoteLights
from .remote_navigation import RemoteNavigation
from .remote_preconditioning import RemotePreconditioning
from .remote_set_immobilization import RemoteSetImmobilization
from .remote_stolen import RemoteStolen
from .remote_wake_up import RemoteWakeUp


class Remote(UniversalBaseModel):
    """
    Remote vehicle activation. ```Only one action``` (horn, precond, door...) is supported at a time.
    """

    label: typing.Optional[str] = None
    preconditioning: typing.Optional[RemotePreconditioning] = None
    immobilization: typing.Optional[RemoteSetImmobilization] = None
    door: typing.Optional[RemoteDoorsState] = None
    horn: typing.Optional[RemoteHorn] = None
    charging: typing.Optional[RemoteCharging] = None
    stolen: typing.Optional[RemoteStolen] = None
    lights: typing.Optional[RemoteLights] = None
    wake_up: typing_extensions.Annotated[
        typing.Optional[RemoteWakeUp], FieldMetadata(alias="wakeUp"), pydantic.Field(alias="wakeUp")
    ] = None
    navigation: typing.Optional[RemoteNavigation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
