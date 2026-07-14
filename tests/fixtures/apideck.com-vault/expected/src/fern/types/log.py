

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .log_operation import LogOperation
from .log_service import LogService
from .log_unified_api import LogUnifiedApi


class Log(UniversalBaseModel):
    api_style: str = pydantic.Field()
    """
    Indicates if the request was made via REST or Graphql endpoint.
    """

    base_url: str = pydantic.Field()
    """
    The Apideck base URL the request was made to.
    """

    child_request: bool = pydantic.Field()
    """
    Indicates whether or not this is a child or parent request.
    """

    consumer_id: str = pydantic.Field()
    """
    The consumer Id associated with the request.
    """

    duration: float = pydantic.Field()
    """
    The entire execution time in milliseconds it took to call the Apideck service provider.
    """

    error_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    If error occurred, this is brief explanation
    """

    execution: int = pydantic.Field()
    """
    The entire execution time in milliseconds it took to make the request.
    """

    has_children: bool = pydantic.Field()
    """
    When request is a parent request, this indicates if there are child requests associated.
    """

    http_method: str = pydantic.Field()
    """
    HTTP Method of request.
    """

    id: str = pydantic.Field()
    """
    UUID acting as Request Identifier.
    """

    latency: float = pydantic.Field()
    """
    Latency added by making this request via Unified Api.
    """

    operation: LogOperation = pydantic.Field()
    """
    The request as defined in OpenApi Spec.
    """

    parent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    When request is a child request, this UUID indicates it's parent request.
    """

    path: str = pydantic.Field()
    """
    The path component of the URI the request was made to.
    """

    sandbox: bool = pydantic.Field()
    """
    Indicates whether the request was made using Apidecks sandbox credentials or not.
    """

    service: LogService = pydantic.Field()
    """
    Apideck service provider associated with request.
    """

    source_ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP address of the source of the request.
    """

    status_code: int = pydantic.Field()
    """
    HTTP Status code that was returned.
    """

    success: bool = pydantic.Field()
    """
    Whether or not the request was successful.
    """

    timestamp: str = pydantic.Field()
    """
    ISO Date and time when the request was made.
    """

    unified_api: LogUnifiedApi = pydantic.Field()
    """
    Which Unified Api request was made to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
