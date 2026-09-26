

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2EnrichmentProviderOutcome(UniversalBaseModel):
    """
    One provider's result within an enrichment cascade.
    """

    id: str = pydantic.Field()
    """
    Provider identifier, e.g. `hunter`.
    """

    label: str = pydantic.Field()
    """
    Human-readable provider name.
    """

    tool_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="toolId"),
        pydantic.Field(alias="toolId", description="Sim tool identifier the provider ran."),
    ]
    """
    Sim tool identifier the provider ran.
    """

    status: str = pydantic.Field()
    """
    Provider outcome: `matched`, `no_match`, `skipped`, `error`, or `not_run`. Handle unrecognized values, since additional statuses may be returned.
    """

    cost: float = pydantic.Field()
    """
    Hosted-key cost in USD this provider incurred; zero when Sim did not bill it.
    """

    duration_ms: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="durationMs"),
        pydantic.Field(alias="durationMs", description="Wall-clock milliseconds this provider took; zero if skipped."),
    ]
    """
    Wall-clock milliseconds this provider took; zero if skipped.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Failure reason when `status` is `error`, else null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
