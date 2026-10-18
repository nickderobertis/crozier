

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetSystemScrapeStatusResponseThermo(UniversalBaseModel):
    success_last1m: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="successLast1M"),
        pydantic.Field(alias="successLast1M", description="Number of successful scrapes in the last 1 minute"),
    ]
    """
    Number of successful scrapes in the last 1 minute
    """

    success_last10m: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="successLast10M"),
        pydantic.Field(alias="successLast10M", description="Number of successful scrapes in the last 10 minutes"),
    ]
    """
    Number of successful scrapes in the last 10 minutes
    """

    success_total: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="successTotal"),
        pydantic.Field(alias="successTotal", description="Total number of successful scrapes since service start"),
    ]
    """
    Total number of successful scrapes since service start
    """

    errors_last1m: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="errorsLast1M"),
        pydantic.Field(alias="errorsLast1M", description="Number of failed scrapes in the last 1 minute"),
    ]
    """
    Number of failed scrapes in the last 1 minute
    """

    errors_last10m: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="errorsLast10M"),
        pydantic.Field(alias="errorsLast10M", description="Number of failed scrapes in the last 10 minutes"),
    ]
    """
    Number of failed scrapes in the last 10 minutes
    """

    errors_total: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="errorsTotal"),
        pydantic.Field(alias="errorsTotal", description="Total number of failed scrapes since service start"),
    ]
    """
    Total number of failed scrapes since service start
    """

    last_error: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastError"),
        pydantic.Field(alias="lastError", description="Timestamp of the last error, or null if none"),
    ] = None
    """
    Timestamp of the last error, or null if none
    """

    last_error_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastErrorMessage"),
        pydantic.Field(alias="lastErrorMessage", description="Message of the last error, or null if none"),
    ] = None
    """
    Message of the last error, or null if none
    """

    error_count_per_channel: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="errorCountPerChannel"),
        pydantic.Field(
            alias="errorCountPerChannel",
            description="Mapping of channel number to cumulative error count for that channel",
        ),
    ]
    """
    Mapping of channel number to cumulative error count for that channel
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
