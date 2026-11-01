

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Lamp(UniversalBaseModel):
    rotations: typing.Optional[int] = None
    flash_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="flashCount"), pydantic.Field(alias="flashCount")
    ] = None
    bulbs: typing.Optional[float] = None
    lens_rings: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lensRings"), pydantic.Field(alias="lensRings")
    ] = None
    keeper_shifts: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="keeperShifts"), pydantic.Field(alias="keeperShifts")
    ] = None
    beam_years: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="beamYears"), pydantic.Field(alias="beamYears")
    ] = None
    wattage: typing.Optional[float] = None
    range: typing.Optional[float] = None
    height_meters: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="heightMeters"), pydantic.Field(alias="heightMeters")
    ] = None
    sweep_rate: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="sweepRate"), pydantic.Field(alias="sweepRate")
    ] = None
    tower_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="towerIds"), pydantic.Field(alias="towerIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
