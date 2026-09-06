

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.api_paged_response_update_system_models_update_group_subscription import (
    ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
)
from ..types.update_system_models_update_group_subscription import UpdateSystemModelsUpdateGroupSubscription
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUpdategroupsubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getupdategroupsubscriptions(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        package_type_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID.

        package_type_id : typing.Optional[str]
            Optional. Filter by Package Type ID.

        client_id : typing.Optional[str]
            Optional. Filter by Client ID.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupSubscriptions",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "PackageTypeID": package_type_id,
                "ClientID": client_id,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def postupdategroupsubscription(
        self,
        *,
        client_id: str,
        include: bool,
        package_type_id: str,
        update_group_id: str,
        update_group_subscription_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ClientID.

        include : bool
            True to receive content of type indicated by PackageTypeID.

        package_type_id : str
            The PackageType to set subscription status for

        update_group_id : str
            The Update Group this subscription is relevant for.

        update_group_subscription_id : typing.Optional[int]
            The Update Group Subscription ID.  This ID will be automatically assigned when creating an Update Group Subscription.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupSubscriptions",
            method="POST",
            json={
                "ClientID": client_id,
                "Include": include,
                "PackageTypeID": package_type_id,
                "UpdateGroupID": update_group_id,
                "UpdateGroupSubscriptionID": update_group_subscription_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def postupdategroupsubscriptions(
        self,
        *,
        request: typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[UpdateSystemModelsUpdateGroupSubscription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupSubscriptions/Batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def putupdategroupsubscriptions(
        self,
        *,
        request: typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[UpdateSystemModelsUpdateGroupSubscription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupSubscriptions/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getupdategroupsubscription(
        self, update_group_subscription_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsUpdateGroupSubscription]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id : int
            The Update Group Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsUpdateGroupSubscription]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroupSubscriptions/{encode_path_param(update_group_subscription_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsUpdateGroupSubscription,
                    parse_obj_as(
                        type_=UpdateSystemModelsUpdateGroupSubscription,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def putupdategroupsubscription(
        self,
        update_group_subscription_id_: int,
        *,
        client_id: str,
        include: bool,
        package_type_id: str,
        update_group_id: str,
        update_group_subscription_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id_ : int
            The Update Group Subscription ID

        client_id : str
            The ClientID.

        include : bool
            True to receive content of type indicated by PackageTypeID.

        package_type_id : str
            The PackageType to set subscription status for

        update_group_id : str
            The Update Group this subscription is relevant for.

        update_group_subscription_id : typing.Optional[int]
            The Update Group Subscription ID.  This ID will be automatically assigned when creating an Update Group Subscription.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroupSubscriptions/{encode_path_param(update_group_subscription_id_)}",
            method="PUT",
            json={
                "ClientID": client_id,
                "Include": include,
                "PackageTypeID": package_type_id,
                "UpdateGroupID": update_group_id,
                "UpdateGroupSubscriptionID": update_group_subscription_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deleteupdategroupsubscription(
        self, update_group_subscription_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id : int
            The Update Group Subscription ID to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroupSubscriptions/{encode_path_param(update_group_subscription_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawUpdategroupsubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getupdategroupsubscriptions(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        package_type_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID.

        package_type_id : typing.Optional[str]
            Optional. Filter by Package Type ID.

        client_id : typing.Optional[str]
            Optional. Filter by Client ID.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupSubscriptions",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "PackageTypeID": package_type_id,
                "ClientID": client_id,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def postupdategroupsubscription(
        self,
        *,
        client_id: str,
        include: bool,
        package_type_id: str,
        update_group_id: str,
        update_group_subscription_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ClientID.

        include : bool
            True to receive content of type indicated by PackageTypeID.

        package_type_id : str
            The PackageType to set subscription status for

        update_group_id : str
            The Update Group this subscription is relevant for.

        update_group_subscription_id : typing.Optional[int]
            The Update Group Subscription ID.  This ID will be automatically assigned when creating an Update Group Subscription.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupSubscriptions",
            method="POST",
            json={
                "ClientID": client_id,
                "Include": include,
                "PackageTypeID": package_type_id,
                "UpdateGroupID": update_group_id,
                "UpdateGroupSubscriptionID": update_group_subscription_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def postupdategroupsubscriptions(
        self,
        *,
        request: typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[UpdateSystemModelsUpdateGroupSubscription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupSubscriptions/Batch",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def putupdategroupsubscriptions(
        self,
        *,
        request: typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[UpdateSystemModelsUpdateGroupSubscription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroupSubscriptions/Batch",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getupdategroupsubscription(
        self, update_group_subscription_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsUpdateGroupSubscription]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id : int
            The Update Group Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsUpdateGroupSubscription]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroupSubscriptions/{encode_path_param(update_group_subscription_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsUpdateGroupSubscription,
                    parse_obj_as(
                        type_=UpdateSystemModelsUpdateGroupSubscription,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def putupdategroupsubscription(
        self,
        update_group_subscription_id_: int,
        *,
        client_id: str,
        include: bool,
        package_type_id: str,
        update_group_id: str,
        update_group_subscription_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id_ : int
            The Update Group Subscription ID

        client_id : str
            The ClientID.

        include : bool
            True to receive content of type indicated by PackageTypeID.

        package_type_id : str
            The PackageType to set subscription status for

        update_group_id : str
            The Update Group this subscription is relevant for.

        update_group_subscription_id : typing.Optional[int]
            The Update Group Subscription ID.  This ID will be automatically assigned when creating an Update Group Subscription.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroupSubscriptions/{encode_path_param(update_group_subscription_id_)}",
            method="PUT",
            json={
                "ClientID": client_id,
                "Include": include,
                "PackageTypeID": package_type_id,
                "UpdateGroupID": update_group_id,
                "UpdateGroupSubscriptionID": update_group_subscription_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deleteupdategroupsubscription(
        self, update_group_subscription_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id : int
            The Update Group Subscription ID to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroupSubscriptions/{encode_path_param(update_group_subscription_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
