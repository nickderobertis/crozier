

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HealthcheckResult(UniversalBaseModel):
    """
    HealthcheckResult stores information about a single run of a healthcheck probe
    """

    start: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="Start"),
        pydantic.Field(
            alias="Start",
            description="Date and time at which this check started in\n[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds.",
        ),
    ] = None
    """
    Date and time at which this check started in
    [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds.
    """

    end: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="End"),
        pydantic.Field(
            alias="End",
            description="Date and time at which this check ended in\n[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds.",
        ),
    ] = None
    """
    Date and time at which this check ended in
    [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds.
    """

    exit_code: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ExitCode"),
        pydantic.Field(
            alias="ExitCode",
            description="ExitCode meanings:\n\n- `0` healthy\n- `1` unhealthy\n- `2` reserved (considered unhealthy)\n- other values: error running probe",
        ),
    ] = None
    """
    ExitCode meanings:
    
    - `0` healthy
    - `1` unhealthy
    - `2` reserved (considered unhealthy)
    - other values: error running probe
    """

    output: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Output"),
        pydantic.Field(alias="Output", description="Output from last check"),
    ] = None
    """
    Output from last check
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
