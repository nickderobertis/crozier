

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.pagination import AsyncPager, SyncPager
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.crane import Crane
from .types.crane_page import CranePage
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_cranes(
        self, *, after: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncPager[Crane, CranePage]:
        """
        Parameters
        ----------
        after : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Crane, CranePage]
            One page of cranes.
        """
        _response = self._client_wrapper.httpx_client.request(
            "cranes",
            method="GET",
            params={
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    CranePage,
                    parse_obj_as(
                        type_=CranePage,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.cranes
                _parsed_next = _parsed_response.next
                _has_next = _parsed_next is not None and _parsed_next != ""
                _get_next = lambda: self.list_cranes(
                    after=_parsed_next,
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

    async def list_cranes(
        self, *, after: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPager[Crane, CranePage]:
        """
        Parameters
        ----------
        after : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Crane, CranePage]
            One page of cranes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "cranes",
            method="GET",
            params={
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    CranePage,
                    parse_obj_as(
                        type_=CranePage,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.cranes
                _parsed_next = _parsed_response.next
                _has_next = _parsed_next is not None and _parsed_next != ""

                async def _get_next():
                    return await self.list_cranes(
                        after=_parsed_next,
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
