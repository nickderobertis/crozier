

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .trajectory_station_out import TrajectoryStationOut


class ConvertTrajectoryResponse(UniversalBaseModel):
    input_kind: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inputKind"), pydantic.Field(alias="inputKind")
    ] = None
    local_crs: typing_extensions.Annotated[str, FieldMetadata(alias="localCRS"), pydantic.Field(alias="localCRS")]
    method: str
    operations_applied: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="operationsApplied"),
        pydantic.Field(alias="operationsApplied"),
    ] = None
    stations: typing.List[TrajectoryStationOut]
    trajectory_crs: typing_extensions.Annotated[
        str, FieldMetadata(alias="trajectoryCRS"), pydantic.Field(alias="trajectoryCRS")
    ]
    unit_dls: typing_extensions.Annotated[str, FieldMetadata(alias="unitDls"), pydantic.Field(alias="unitDls")]
    unit_xy: typing_extensions.Annotated[str, FieldMetadata(alias="unitXY"), pydantic.Field(alias="unitXY")]
    unit_z: typing_extensions.Annotated[str, FieldMetadata(alias="unitZ"), pydantic.Field(alias="unitZ")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
