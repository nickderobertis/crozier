

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metrics_this_week import MetricsThisWeek


class Metrics(UniversalBaseModel):
    """
    List of basic metrics
    """

    datasets: typing.Optional[typing.List[typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Data used for charting etc
    """

    fixed_pct: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="fixedPct")] = pydantic.Field(
        default=None
    )
    """
    Percentage of all APIs where auto fixes have been applied
    """

    fixes: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of fixes applied across all APIs
    """

    invalid: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of newly invalid APIs
    """

    issues: typing.Optional[int] = pydantic.Field(default=None)
    """
    Open GitHub issues on our main repo
    """

    num_ap_is: typing_extensions.Annotated[int, FieldMetadata(alias="numAPIs")] = pydantic.Field()
    """
    Number of unique APIs
    """

    num_drivers: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="numDrivers")] = pydantic.Field(
        default=None
    )
    """
    Number of methods of API retrieval
    """

    num_endpoints: typing_extensions.Annotated[int, FieldMetadata(alias="numEndpoints")] = pydantic.Field()
    """
    Total number of endpoints inside all definitions
    """

    num_providers: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="numProviders")] = (
        pydantic.Field(default=None)
    )
    """
    Number of API providers in directory
    """

    num_specs: typing_extensions.Annotated[int, FieldMetadata(alias="numSpecs")] = pydantic.Field()
    """
    Number of API definitions including different versions of the same API
    """

    stars: typing.Optional[int] = pydantic.Field(default=None)
    """
    GitHub stars for our main repo
    """

    this_week: typing_extensions.Annotated[typing.Optional[MetricsThisWeek], FieldMetadata(alias="thisWeek")] = (
        pydantic.Field(default=None)
    )
    """
    Summary totals for the last 7 days
    """

    unofficial: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of unofficial APIs
    """

    unreachable: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of unreachable (4XX,5XX status) APIs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
