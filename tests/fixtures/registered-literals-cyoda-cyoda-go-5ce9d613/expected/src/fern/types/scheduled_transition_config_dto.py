

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScheduledTransitionConfigDto(UniversalBaseModel):
    delay_ms: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="delayMs"),
        pydantic.Field(alias="delayMs", description="Delay in milliseconds before executing the transition"),
    ]
    """
    Delay in milliseconds before executing the transition
    """

    transition: str = pydantic.Field()
    """
    The transition to execute after waiting delayMs
    """

    timeout_ms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="timeoutMs"),
        pydantic.Field(
            alias="timeoutMs",
            description="Timeout in milliseconds for executing the transition task, after which it will be expired",
        ),
    ] = None
    """
    Timeout in milliseconds for executing the transition task, after which it will be expired
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
