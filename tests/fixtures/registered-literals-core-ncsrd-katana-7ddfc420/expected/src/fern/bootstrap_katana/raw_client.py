

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.internal_server_error import InternalServerError
from ..types.ems import Ems
from ..types.net_func import NetFunc
from ..types.nfvo import Nfvo
from ..types.vim import Vim
from ..types.wim import Wim
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBootstrapKatanaClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def configure_katana_using_one_json_file_note_that_the_locations_must_be_already_added(
        self,
        *,
        vim: typing.Optional[typing.Sequence[Vim]] = OMIT,
        nfvo: typing.Optional[typing.Sequence[Nfvo]] = OMIT,
        wim: typing.Optional[typing.Sequence[Wim]] = OMIT,
        ems: typing.Optional[typing.Sequence[Ems]] = OMIT,
        function: typing.Optional[typing.Sequence[NetFunc]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        vim : typing.Optional[typing.Sequence[Vim]]
            A list with the VIM components to be added

        nfvo : typing.Optional[typing.Sequence[Nfvo]]
            A list with the NFVO components to be added

        wim : typing.Optional[typing.Sequence[Wim]]
            A list with the WIM components to be added

        ems : typing.Optional[typing.Sequence[Ems]]
            A list with the EMS components to be added

        function : typing.Optional[typing.Sequence[NetFunc]]
            A list with the Network Functions to be added

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "bootstrap",
            method="POST",
            json={
                "vim": convert_and_respect_annotation_metadata(
                    object_=vim, annotation=typing.Sequence[Vim], direction="write"
                ),
                "nfvo": convert_and_respect_annotation_metadata(
                    object_=nfvo, annotation=typing.Sequence[Nfvo], direction="write"
                ),
                "wim": convert_and_respect_annotation_metadata(
                    object_=wim, annotation=typing.Sequence[Wim], direction="write"
                ),
                "ems": convert_and_respect_annotation_metadata(
                    object_=ems, annotation=typing.Sequence[Ems], direction="write"
                ),
                "function": convert_and_respect_annotation_metadata(
                    object_=function, annotation=typing.Sequence[NetFunc], direction="write"
                ),
            },
            headers={
                "content-type": "Application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawBootstrapKatanaClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def configure_katana_using_one_json_file_note_that_the_locations_must_be_already_added(
        self,
        *,
        vim: typing.Optional[typing.Sequence[Vim]] = OMIT,
        nfvo: typing.Optional[typing.Sequence[Nfvo]] = OMIT,
        wim: typing.Optional[typing.Sequence[Wim]] = OMIT,
        ems: typing.Optional[typing.Sequence[Ems]] = OMIT,
        function: typing.Optional[typing.Sequence[NetFunc]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        vim : typing.Optional[typing.Sequence[Vim]]
            A list with the VIM components to be added

        nfvo : typing.Optional[typing.Sequence[Nfvo]]
            A list with the NFVO components to be added

        wim : typing.Optional[typing.Sequence[Wim]]
            A list with the WIM components to be added

        ems : typing.Optional[typing.Sequence[Ems]]
            A list with the EMS components to be added

        function : typing.Optional[typing.Sequence[NetFunc]]
            A list with the Network Functions to be added

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "bootstrap",
            method="POST",
            json={
                "vim": convert_and_respect_annotation_metadata(
                    object_=vim, annotation=typing.Sequence[Vim], direction="write"
                ),
                "nfvo": convert_and_respect_annotation_metadata(
                    object_=nfvo, annotation=typing.Sequence[Nfvo], direction="write"
                ),
                "wim": convert_and_respect_annotation_metadata(
                    object_=wim, annotation=typing.Sequence[Wim], direction="write"
                ),
                "ems": convert_and_respect_annotation_metadata(
                    object_=ems, annotation=typing.Sequence[Ems], direction="write"
                ),
                "function": convert_and_respect_annotation_metadata(
                    object_=function, annotation=typing.Sequence[NetFunc], direction="write"
                ),
            },
            headers={
                "content-type": "Application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
