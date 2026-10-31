

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SkuCost(UniversalBaseModel):
    """
    Describes metadata for retrieving price info.
    """

    meter_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="meterId"),
        pydantic.Field(alias="meterId", description="Meter id of the Sku."),
    ] = None
    """
    Meter id of the Sku.
    """

    meter_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="meterType"),
        pydantic.Field(alias="meterType", description="The type of the meter."),
    ] = None
    """
    The type of the meter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
