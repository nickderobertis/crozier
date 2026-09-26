

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .position_base_properties_fix_status import PositionBasePropertiesFixStatus
from .position_base_properties_type import PositionBasePropertiesType
from .vin import Vin


class PositionBaseProperties(UniversalBaseModel):
    vin: typing.Optional[Vin] = None
    heading: typing.Optional[int] = pydantic.Field(default=None)
    """
    Course angle expressed in degree.
    """

    signal_quality: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="signalQuality"), pydantic.Field(alias="signalQuality")
    ] = None
    type: typing.Optional[PositionBasePropertiesType] = None
    fix_status: typing_extensions.Annotated[
        typing.Optional[PositionBasePropertiesFixStatus],
        FieldMetadata(alias="fixStatus"),
        pydantic.Field(
            alias="fixStatus",
            description="Fix status information is only returned when position type is set to Acquire. Horizontal & altitude position can be determined in 3D fix status mode where it is only horizontal position in 2D mode.",
        ),
    ] = None
    """
    Fix status information is only returned when position type is set to Acquire. Horizontal & altitude position can be determined in 3D fix status mode where it is only horizontal position in 2D mode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
