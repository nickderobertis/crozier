

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HttpOverrideForwardedRequestRequestModifierResponseModifierCondition(UniversalBaseModel):
    """
    apply this modifier only when the in-flight response (and optionally the original request) match
    """

    status_code: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="statusCode"),
        pydantic.Field(alias="statusCode", description="response status code must equal this value"),
    ] = None
    """
    response status code must equal this value
    """

    status_code_range: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="statusCodeRange"),
        pydantic.Field(
            alias="statusCodeRange", description="response status code must fall in this class range, e.g. 2xx or 5xx"
        ),
    ] = None
    """
    response status code must fall in this class range, e.g. 2xx or 5xx
    """

    response_has_header: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="responseHasHeader"),
        pydantic.Field(
            alias="responseHasHeader",
            description="response must carry a header with this name (any value, case-insensitive)",
        ),
    ] = None
    """
    response must carry a header with this name (any value, case-insensitive)
    """

    request_has_header: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requestHasHeader"),
        pydantic.Field(
            alias="requestHasHeader",
            description="request must carry a header with this name (any value, case-insensitive)",
        ),
    ] = None
    """
    request must carry a header with this name (any value, case-insensitive)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
