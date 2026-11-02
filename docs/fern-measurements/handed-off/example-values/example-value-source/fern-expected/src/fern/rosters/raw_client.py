

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.roster_entry import RosterEntry
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRostersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_roster_entry(
        self,
        id: str,
        *,
        watch_token: str,
        request: RosterEntry,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        A required header on an operation whose body has no worked example.

        Parameters
        ----------
        id : str

        watch_token : str

        request : RosterEntry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"rosters/{encode_path_param(id)}/entries",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=RosterEntry, direction="write"),
            headers={
                "content-type": "application/json",
                "X-Watch-Token": str(watch_token) if watch_token is not None else None,
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


class AsyncRawRostersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_roster_entry(
        self,
        id: str,
        *,
        watch_token: str,
        request: RosterEntry,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        A required header on an operation whose body has no worked example.

        Parameters
        ----------
        id : str

        watch_token : str

        request : RosterEntry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"rosters/{encode_path_param(id)}/entries",
            method="POST",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=RosterEntry, direction="write"),
            headers={
                "content-type": "application/json",
                "X-Watch-Token": str(watch_token) if watch_token is not None else None,
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
