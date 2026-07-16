

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .applications_series import ApplicationsSeries


class ApplicationsApiUsage(UniversalBaseModel):
    api_calls: typing_extensions.Annotated[
        typing.Optional[typing.List[ApplicationsSeries]],
        FieldMetadata(alias="apiCalls"),
        pydantic.Field(alias="apiCalls", description="Counts for on API calls made for the time range."),
    ] = None
    """
    Counts for on API calls made for the time range.
    """

    throttled_requests: typing_extensions.Annotated[
        typing.Optional[typing.List[ApplicationsSeries]],
        FieldMetadata(alias="throttledRequests"),
        pydantic.Field(
            alias="throttledRequests",
            description="Instances of blocked requests or requests that crossed the warn threshold during the time range.",
        ),
    ] = None
    """
    Instances of blocked requests or requests that crossed the warn threshold during the time range.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
