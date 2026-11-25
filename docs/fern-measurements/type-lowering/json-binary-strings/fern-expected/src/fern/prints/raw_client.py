

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.print import Print
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPrintsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def submit_print(
        self,
        *,
        instructions: str,
        negative: typing.Optional[bytes] = OMIT,
        contacts: typing.Optional[typing.Sequence[str]] = OMIT,
        layers: typing.Optional[typing.Dict[str, str]] = OMIT,
        mask: typing.Optional[bytes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Print]:
        """
        Parameters
        ----------
        instructions : str

        negative : typing.Optional[bytes]

        contacts : typing.Optional[typing.Sequence[str]]

        layers : typing.Optional[typing.Dict[str, str]]

        mask : typing.Optional[bytes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Print]
            The developed print.
        """
        _response = self._client_wrapper.httpx_client.request(
            "prints",
            method="POST",
            json={
                "negative": negative,
                "contacts": contacts,
                "layers": layers,
                "mask": mask,
                "instructions": instructions,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Print,
                    parse_obj_as(
                        type_=Print,
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


class AsyncRawPrintsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def submit_print(
        self,
        *,
        instructions: str,
        negative: typing.Optional[bytes] = OMIT,
        contacts: typing.Optional[typing.Sequence[str]] = OMIT,
        layers: typing.Optional[typing.Dict[str, str]] = OMIT,
        mask: typing.Optional[bytes] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Print]:
        """
        Parameters
        ----------
        instructions : str

        negative : typing.Optional[bytes]

        contacts : typing.Optional[typing.Sequence[str]]

        layers : typing.Optional[typing.Dict[str, str]]

        mask : typing.Optional[bytes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Print]
            The developed print.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "prints",
            method="POST",
            json={
                "negative": negative,
                "contacts": contacts,
                "layers": layers,
                "mask": mask,
                "instructions": instructions,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Print,
                    parse_obj_as(
                        type_=Print,
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
