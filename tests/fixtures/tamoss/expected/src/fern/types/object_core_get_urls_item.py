

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .storage_backend import StorageBackend
from .uuid_ import Uuid


class ObjectCoreGetUrlsItem(StorageBackend):
    storage_id: typing.Optional[Uuid] = pydantic.Field(default=None)
    """
    Storage Backend identifier
    """

    url: str = pydantic.Field()
    """
    A URL to which a GET request can be made to directly retrieve the contents of the media object. Clients should include credentials if the provide URL is on the same origin as the API endpoint. This URL SHOULD support the inclusion of checksums in headers as supported by advertised Storage Backend product. See AppNote 0048 for more details.
    """

    presigned: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, this URL is pre-signed. If this parameter is unset, the URL is NOT pre-signed. The presigned URL SHALL remain valid for the timeframe advertised in [`min_presigned_url_timeout` at the `/service`](#/operations/GET_service) endpoint, which is subject to a specified minimum (see service endpoint schema).
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Label identifying this URL. If the URL is controlled by the service instance, this is the Storage Backend's label. If the URL is uncontrolled, this is the label provided when a client registered the URL. If the 'label' is not set then this URL can't be filtered for using the 'accept_get_urls' API query parameter.
    """

    controlled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, this URL is on a Storage Backend controlled by this service instance. If `false`, this URL is uncontrolled and does not have it's lifecycle managed by this instance. If this parameter is unset, assume `true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
