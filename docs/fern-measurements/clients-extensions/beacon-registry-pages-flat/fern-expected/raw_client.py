

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.pagination import AsyncPager, SyncPager
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.beacon_page import BeaconPage
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_beacons(
        self, *, page: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncPager[str, BeaconPage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[str, BeaconPage]
            One page of beacons.
        """
        page = page if page is not None else 1

        _response = self._client_wrapper.httpx_client.request(
            "beacons",
            method="GET",
            params={
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    BeaconPage,
                    parse_obj_as(
                        type_=BeaconPage,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.beacons
                _has_next = len(_items or []) > 0
                _get_next = lambda: self.list_beacons(
                    page=page + 1,
                    request_options=request_options,
                )
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_beacons(
        self, *, page: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPager[str, BeaconPage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[str, BeaconPage]
            One page of beacons.
        """
        page = page if page is not None else 1

        _response = await self._client_wrapper.httpx_client.request(
            "beacons",
            method="GET",
            params={
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    BeaconPage,
                    parse_obj_as(
                        type_=BeaconPage,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.beacons
                _has_next = len(_items or []) > 0

                async def _get_next():
                    return await self.list_beacons(
                        page=page + 1,
                        request_options=request_options,
                    )

                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next, response=_parsed_response)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
