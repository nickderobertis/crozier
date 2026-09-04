

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.pagination import AsyncPager, SyncPager
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...types.widget import Widget
from ...types.widget_page import WidgetPage
from pydantic import ValidationError


class RawWidgetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, page_token: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncPager[Widget, WidgetPage]:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Opaque cursor from a previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Widget, WidgetPage]
            A page of widgets.
        """
        _response = self._client_wrapper.httpx_client.request(
            "widgets",
            method="GET",
            params={
                "page_token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    WidgetPage,
                    parse_obj_as(
                        type_=WidgetPage,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = False
                _get_next = None
                if _parsed_response.pagination is not None:
                    _parsed_next = _parsed_response.pagination.next_page_token
                    _has_next = _parsed_next is not None and _parsed_next != ""
                    _get_next = lambda: self.list(
                        page_token=_parsed_next,
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


class AsyncRawWidgetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, page_token: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPager[Widget, WidgetPage]:
        """
        Parameters
        ----------
        page_token : typing.Optional[str]
            Opaque cursor from a previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Widget, WidgetPage]
            A page of widgets.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "widgets",
            method="GET",
            params={
                "page_token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    WidgetPage,
                    parse_obj_as(
                        type_=WidgetPage,
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = False
                _get_next = None
                if _parsed_response.pagination is not None:
                    _parsed_next = _parsed_response.pagination.next_page_token
                    _has_next = _parsed_next is not None and _parsed_next != ""

                    async def _get_next():
                        return await self.list(
                            page_token=_parsed_next,
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
