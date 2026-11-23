

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .exposure_unit import ExposureUnit
from .filter_band import FilterBand
from .image_size import ImageSize
from .presence import Presence
from .session_calibrations_value_item import SessionCalibrationsValueItem
from .session_reading_batches_item_item import SessionReadingBatchesItemItem
from .session_readings_by_owner_value_value import SessionReadingsByOwnerValueValue


class Session(UniversalBaseModel):
    id: str
    size: typing.Optional[ImageSize] = None
    presence: typing.Optional[Presence] = None
    unit: typing.Optional[ExposureUnit] = None
    filter: typing.Optional[FilterBand] = None
    readings_by_owner: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, SessionReadingsByOwnerValueValue]]],
        FieldMetadata(alias="readingsByOwner"),
        pydantic.Field(alias="readingsByOwner", description="Readings keyed by owner, then by instrument."),
    ] = None
    """
    Readings keyed by owner, then by instrument.
    """

    reading_batches: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[SessionReadingBatchesItemItem]]],
        FieldMetadata(alias="readingBatches"),
        pydantic.Field(alias="readingBatches", description="Readings in batches of batches."),
    ] = None
    """
    Readings in batches of batches.
    """

    calibrations: typing.Optional[typing.Dict[str, typing.List[SessionCalibrationsValueItem]]] = pydantic.Field(
        default=None
    )
    """
    Calibration values, grouped.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
