

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.loan import Loan
from .types.scan import Scan
from .types.shelf import Shelf
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_shelf(
        self,
        branch_path_param: str,
        shelf_path_param: str,
        *,
        shelf: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Shelf]:
        """
        Parameters
        ----------
        branch_path_param : str
            The branch the shelf stands in.

        shelf_path_param : str
            The shelf's code.

        shelf : typing.Optional[str]
            The shelf this one overflows from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Shelf]
            The shelf.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"branches/{encode_path_param(branch_path_param)}/shelves/{encode_path_param(shelf_path_param)}",
            method="GET",
            params={
                "shelf": shelf,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Shelf,
                    parse_obj_as(
                        type_=Shelf,
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

    def list_edition_scans(
        self,
        branch_path_param: str,
        edition_path_param: str,
        *,
        edition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Scan]]:
        """
        Parameters
        ----------
        branch_path_param : str
            The branch that scanned the edition.

        edition_path_param : str
            The edition scanned.

        edition : typing.Optional[str]
            The edition the reader app currently shows.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Scan]]
            The scanned pages.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"branches/{encode_path_param(branch_path_param)}/editions/{encode_path_param(edition_path_param)}/scans",
            method="GET",
            headers={
                "edition": str(edition) if edition is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Scan],
                    parse_obj_as(
                        type_=typing.List[Scan],
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

    def list_loans(
        self,
        *,
        patron: str,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Loan]]:
        """
        Parameters
        ----------
        patron : str
            The patron whose loans are listed.

        page_size : typing.Optional[int]
            How many loans to list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Loan]]
            The patron's loans.
        """
        _response = self._client_wrapper.httpx_client.request(
            "loans",
            method="GET",
            params={
                "patron": patron,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Loan],
                    parse_obj_as(
                        type_=typing.List[Loan],
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_shelf(
        self,
        branch_path_param: str,
        shelf_path_param: str,
        *,
        shelf: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Shelf]:
        """
        Parameters
        ----------
        branch_path_param : str
            The branch the shelf stands in.

        shelf_path_param : str
            The shelf's code.

        shelf : typing.Optional[str]
            The shelf this one overflows from.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Shelf]
            The shelf.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"branches/{encode_path_param(branch_path_param)}/shelves/{encode_path_param(shelf_path_param)}",
            method="GET",
            params={
                "shelf": shelf,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Shelf,
                    parse_obj_as(
                        type_=Shelf,
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

    async def list_edition_scans(
        self,
        branch_path_param: str,
        edition_path_param: str,
        *,
        edition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Scan]]:
        """
        Parameters
        ----------
        branch_path_param : str
            The branch that scanned the edition.

        edition_path_param : str
            The edition scanned.

        edition : typing.Optional[str]
            The edition the reader app currently shows.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Scan]]
            The scanned pages.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"branches/{encode_path_param(branch_path_param)}/editions/{encode_path_param(edition_path_param)}/scans",
            method="GET",
            headers={
                "edition": str(edition) if edition is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Scan],
                    parse_obj_as(
                        type_=typing.List[Scan],
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

    async def list_loans(
        self,
        *,
        patron: str,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Loan]]:
        """
        Parameters
        ----------
        patron : str
            The patron whose loans are listed.

        page_size : typing.Optional[int]
            How many loans to list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Loan]]
            The patron's loans.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "loans",
            method="GET",
            params={
                "patron": patron,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Loan],
                    parse_obj_as(
                        type_=typing.List[Loan],
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
