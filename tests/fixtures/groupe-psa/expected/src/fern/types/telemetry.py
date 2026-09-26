

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .created_at_field import CreatedAtField
from .environment_base import EnvironmentBase
from .privacy_base import PrivacyBase
from .telemetry_embedded import TelemetryEmbedded
from .telemetry_links import TelemetryLinks
from .telemetry_vehicle import TelemetryVehicle


class Telemetry(CreatedAtField):
    links: typing_extensions.Annotated[TelemetryLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    privacy: typing.Optional[PrivacyBase] = None
    vehicle: typing.Optional[TelemetryVehicle] = None
    environment: typing.Optional[EnvironmentBase] = None
    embedded: typing_extensions.Annotated[
        typing.Optional[TelemetryEmbedded], FieldMetadata(alias="_embedded"), pydantic.Field(alias="_embedded")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
