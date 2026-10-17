

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetHeaterMetricsResponseMetricsItemChannelsItem(UniversalBaseModel):
    channel: float = pydantic.Field()
    """
    Channel number
    """

    power_watts: typing_extensions.Annotated[
        float, FieldMetadata(alias="powerWatts"), pydantic.Field(alias="powerWatts", description="Power in Watts")
    ]
    """
    Power in Watts
    """

    power_percent: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="powerPercent"),
        pydantic.Field(
            alias="powerPercent",
            description="Requested power as a percentage (0-100). Reflects PID output or manual setting.",
        ),
    ]
    """
    Requested power as a percentage (0-100). Reflects PID output or manual setting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
