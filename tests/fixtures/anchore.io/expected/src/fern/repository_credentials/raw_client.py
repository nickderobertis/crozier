

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.subscription_list import SubscriptionList


class RawRepositoryCredentialsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_repository(
        self,
        *,
        repository: str,
        autosubscribe: typing.Optional[bool] = None,
        dryrun: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriptionList]:
        """


        Parameters
        ----------
        repository : str
            full repository to add e.g. docker.io/library/alpine

        autosubscribe : typing.Optional[bool]
            flag to enable/disable auto tag_update activation when new images from a repo are added

        dryrun : typing.Optional[bool]
            flag to return tags in the repository without actually watching the repository, default is false

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionList]
            Repository and discovered tags added
        """
        _response = self._client_wrapper.httpx_client.request(
            "repositories",
            method="POST",
            params={
                "repository": repository,
                "autosubscribe": autosubscribe,
                "dryrun": dryrun,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionList,
                    parse_obj_as(
                        type_=SubscriptionList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawRepositoryCredentialsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_repository(
        self,
        *,
        repository: str,
        autosubscribe: typing.Optional[bool] = None,
        dryrun: typing.Optional[bool] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriptionList]:
        """


        Parameters
        ----------
        repository : str
            full repository to add e.g. docker.io/library/alpine

        autosubscribe : typing.Optional[bool]
            flag to enable/disable auto tag_update activation when new images from a repo are added

        dryrun : typing.Optional[bool]
            flag to return tags in the repository without actually watching the repository, default is false

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionList]
            Repository and discovered tags added
        """
        _response = await self._client_wrapper.httpx_client.request(
            "repositories",
            method="POST",
            params={
                "repository": repository,
                "autosubscribe": autosubscribe,
                "dryrun": dryrun,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionList,
                    parse_obj_as(
                        type_=SubscriptionList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
