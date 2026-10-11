

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_operations_response import ListOperationsResponse
from ..types.operation import Operation
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
from .types.speech_projects_locations_operations_get_request_alt import SpeechProjectsLocationsOperationsGetRequestAlt
from .types.speech_projects_locations_operations_get_request_xgafv import (
    SpeechProjectsLocationsOperationsGetRequestXgafv,
)
from .types.speech_projects_locations_operations_list_request_alt import SpeechProjectsLocationsOperationsListRequestAlt
from .types.speech_projects_locations_operations_list_request_xgafv import (
    SpeechProjectsLocationsOperationsListRequestXgafv,
)


class ProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectsClient
        """
        return self._raw_client

    def speech_projects_locations_operations_get(
        self,
        name: str,
        *,
        xgafv: typing.Optional[SpeechProjectsLocationsOperationsGetRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[SpeechProjectsLocationsOperationsGetRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Operation:
        """
        Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

        Parameters
        ----------
        name : str
            The name of the operation resource.

        xgafv : typing.Optional[SpeechProjectsLocationsOperationsGetRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[SpeechProjectsLocationsOperationsGetRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Operation
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.speech_projects_locations_operations_get(
            name="name",
        )
        """
        _response = self._raw_client.speech_projects_locations_operations_get(
            name,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            request_options=request_options,
        )
        return _response.data

    def speech_projects_locations_operations_list(
        self,
        name: str,
        *,
        xgafv: typing.Optional[SpeechProjectsLocationsOperationsListRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[SpeechProjectsLocationsOperationsListRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListOperationsResponse:
        """
        Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/* /operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

        Parameters
        ----------
        name : str
            The name of the operation's parent resource.

        xgafv : typing.Optional[SpeechProjectsLocationsOperationsListRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[SpeechProjectsLocationsOperationsListRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        filter : typing.Optional[str]
            The standard list filter.

        page_size : typing.Optional[int]
            The standard list page size.

        page_token : typing.Optional[str]
            The standard list page token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOperationsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.speech_projects_locations_operations_list(
            name="name",
        )
        """
        _response = self._raw_client.speech_projects_locations_operations_list(
            name,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            filter=filter,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data


class AsyncProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectsClient
        """
        return self._raw_client

    async def speech_projects_locations_operations_get(
        self,
        name: str,
        *,
        xgafv: typing.Optional[SpeechProjectsLocationsOperationsGetRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[SpeechProjectsLocationsOperationsGetRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Operation:
        """
        Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

        Parameters
        ----------
        name : str
            The name of the operation resource.

        xgafv : typing.Optional[SpeechProjectsLocationsOperationsGetRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[SpeechProjectsLocationsOperationsGetRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Operation
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.speech_projects_locations_operations_get(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.speech_projects_locations_operations_get(
            name,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            request_options=request_options,
        )
        return _response.data

    async def speech_projects_locations_operations_list(
        self,
        name: str,
        *,
        xgafv: typing.Optional[SpeechProjectsLocationsOperationsListRequestXgafv] = None,
        access_token: typing.Optional[str] = None,
        alt: typing.Optional[SpeechProjectsLocationsOperationsListRequestAlt] = None,
        callback: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        oauth_token: typing.Optional[str] = None,
        pretty_print: typing.Optional[bool] = None,
        quota_user: typing.Optional[str] = None,
        upload_protocol: typing.Optional[str] = None,
        upload_type: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListOperationsResponse:
        """
        Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/* /operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

        Parameters
        ----------
        name : str
            The name of the operation's parent resource.

        xgafv : typing.Optional[SpeechProjectsLocationsOperationsListRequestXgafv]
            V1 error format.

        access_token : typing.Optional[str]
            OAuth access token.

        alt : typing.Optional[SpeechProjectsLocationsOperationsListRequestAlt]
            Data format for response.

        callback : typing.Optional[str]
            JSONP

        fields : typing.Optional[str]
            Selector specifying which fields to include in a partial response.

        key : typing.Optional[str]
            API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

        oauth_token : typing.Optional[str]
            OAuth 2.0 token for the current user.

        pretty_print : typing.Optional[bool]
            Returns response with indentations and line breaks.

        quota_user : typing.Optional[str]
            Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

        upload_protocol : typing.Optional[str]
            Upload protocol for media (e.g. "raw", "multipart").

        upload_type : typing.Optional[str]
            Legacy upload protocol for media (e.g. "media", "multipart").

        filter : typing.Optional[str]
            The standard list filter.

        page_size : typing.Optional[int]
            The standard list page size.

        page_token : typing.Optional[str]
            The standard list page token.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListOperationsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.speech_projects_locations_operations_list(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.speech_projects_locations_operations_list(
            name,
            xgafv=xgafv,
            access_token=access_token,
            alt=alt,
            callback=callback,
            fields=fields,
            key=key,
            oauth_token=oauth_token,
            pretty_print=pretty_print,
            quota_user=quota_user,
            upload_protocol=upload_protocol,
            upload_type=upload_type,
            filter=filter,
            page_size=page_size,
            page_token=page_token,
            request_options=request_options,
        )
        return _response.data
