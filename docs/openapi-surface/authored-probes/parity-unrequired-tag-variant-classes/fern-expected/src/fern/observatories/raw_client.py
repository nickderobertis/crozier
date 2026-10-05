

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.observatory import Observatory
from ..types.observatory_instruments_item import ObservatoryInstrumentsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawObservatoriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def register_observatory(
        self,
        *,
        site: str,
        instruments: typing.Optional[typing.Sequence[ObservatoryInstrumentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Observatory]:
        """
        Parameters
        ----------
        site : str

        instruments : typing.Optional[typing.Sequence[ObservatoryInstrumentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Observatory]
            The registered observatory.
        """
        _response = self._client_wrapper.httpx_client.request(
            "observatories",
            method="POST",
            json={
                "site": site,
                "instruments": convert_and_respect_annotation_metadata(
                    object_=instruments, annotation=typing.Sequence[ObservatoryInstrumentsItem], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Observatory,
                    parse_obj_as(
                        type_=Observatory,
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


class AsyncRawObservatoriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def register_observatory(
        self,
        *,
        site: str,
        instruments: typing.Optional[typing.Sequence[ObservatoryInstrumentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Observatory]:
        """
        Parameters
        ----------
        site : str

        instruments : typing.Optional[typing.Sequence[ObservatoryInstrumentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Observatory]
            The registered observatory.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "observatories",
            method="POST",
            json={
                "site": site,
                "instruments": convert_and_respect_annotation_metadata(
                    object_=instruments, annotation=typing.Sequence[ObservatoryInstrumentsItem], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Observatory,
                    parse_obj_as(
                        type_=Observatory,
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
