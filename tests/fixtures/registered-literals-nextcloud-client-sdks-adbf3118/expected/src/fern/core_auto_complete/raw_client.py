

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_auto_complete_get200response import CoreAutoCompleteGet200Response
from pydantic import ValidationError


class RawCoreAutoCompleteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        search: str,
        item_type: typing.Optional[str] = None,
        item_id: typing.Optional[str] = None,
        sorter: typing.Optional[str] = None,
        share_types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreAutoCompleteGet200Response]:
        """
        Parameters
        ----------
        search : str
            Text to search for

        item_type : typing.Optional[str]
            Type of the items to search for

        item_id : typing.Optional[str]
            ID of the items to search for

        sorter : typing.Optional[str]
            can be piped, top prio first, e.g.: "commenters|share-recipients"

        share_types : typing.Optional[str]
            Types of shares to search for

        limit : typing.Optional[int]
            Maximum number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreAutoCompleteGet200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/core/autocomplete/get",
            method="GET",
            params={
                "search": search,
                "itemType": item_type,
                "itemId": item_id,
                "sorter": sorter,
                "shareTypes": share_types,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreAutoCompleteGet200Response,
                    parse_obj_as(
                        type_=CoreAutoCompleteGet200Response,
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


class AsyncRawCoreAutoCompleteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        search: str,
        item_type: typing.Optional[str] = None,
        item_id: typing.Optional[str] = None,
        sorter: typing.Optional[str] = None,
        share_types: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreAutoCompleteGet200Response]:
        """
        Parameters
        ----------
        search : str
            Text to search for

        item_type : typing.Optional[str]
            Type of the items to search for

        item_id : typing.Optional[str]
            ID of the items to search for

        sorter : typing.Optional[str]
            can be piped, top prio first, e.g.: "commenters|share-recipients"

        share_types : typing.Optional[str]
            Types of shares to search for

        limit : typing.Optional[int]
            Maximum number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreAutoCompleteGet200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/core/autocomplete/get",
            method="GET",
            params={
                "search": search,
                "itemType": item_type,
                "itemId": item_id,
                "sorter": sorter,
                "shareTypes": share_types,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreAutoCompleteGet200Response,
                    parse_obj_as(
                        type_=CoreAutoCompleteGet200Response,
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
