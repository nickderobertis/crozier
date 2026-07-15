

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_resources_item import ApiResourcesItem
from .api_status import ApiStatus
from .api_type import ApiType


class Api(UniversalBaseModel):
    api_reference_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the API reference of the API.
    """

    categories: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of categories the API belongs to.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the API.
    """

    events: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of event types this API supports.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the API.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the API.
    """

    postman_collection_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the Postman collection of the API.
    """

    resources: typing.Optional[typing.List[ApiResourcesItem]] = pydantic.Field(default=None)
    """
    List of resources supported in this API.
    """

    spec_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the latest OpenAPI specification of the API.
    """

    status: typing.Optional[ApiStatus] = None
    type: typing.Optional[ApiType] = pydantic.Field(default=None)
    """
    Indicates whether the API is a Unified API. If unified_api is false, the API is a Platform API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
