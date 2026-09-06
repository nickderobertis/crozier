

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .google_cloud_servicebroker_v1alpha1binding import GoogleCloudServicebrokerV1Alpha1Binding


class GoogleCloudServicebrokerV1Alpha1ListBindingsResponse(UniversalBaseModel):
    """
    The response for the `ListBindings()` method.
    """

    bindings: typing.Optional[typing.List[GoogleCloudServicebrokerV1Alpha1Binding]] = pydantic.Field(default=None)
    """
    The list of the bindings in the instance.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Used to communicate description of the response. Usually for non-standard
    error codes.
    https://github.com/openservicebrokerapi/servicebroker/blob/master/spec.md#service-broker-errors
    """

    next_page_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageToken"),
        pydantic.Field(
            alias="nextPageToken",
            description="This token allows you to get the next page of results for list requests.\nIf the number of results is larger than `pageSize`, use the `nextPageToken`\nas a value for the query parameter `pageToken` in the next list request.\nSubsequent list requests will have their own `nextPageToken` to continue\npaging through the results",
        ),
    ] = None
    """
    This token allows you to get the next page of results for list requests.
    If the number of results is larger than `pageSize`, use the `nextPageToken`
    as a value for the query parameter `pageToken` in the next list request.
    Subsequent list requests will have their own `nextPageToken` to continue
    paging through the results
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
