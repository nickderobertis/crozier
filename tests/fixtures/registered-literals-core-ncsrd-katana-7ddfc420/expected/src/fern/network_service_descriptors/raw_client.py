

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..types.nsd import Nsd
from pydantic import ValidationError


class RawNetworkServiceDescriptorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def returns_a_list_of_the_available_network_service_descriptors_on_the_all_nfv_os_registered_on_the_sm(
        self,
        *,
        nsd_id: typing.Optional[str] = None,
        nfvo_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Nsd]]:
        """
        Parameters
        ----------
        nsd_id : typing.Optional[str]
            The id for a specific NSD

        nfvo_id : typing.Optional[str]
            The id for a specific NFVO

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Nsd]]
            Successful Operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "nslist",
            method="GET",
            params={
                "nsd-id": nsd_id,
                "nfvo-id": nfvo_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Nsd],
                    parse_obj_as(
                        type_=typing.List[Nsd],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawNetworkServiceDescriptorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def returns_a_list_of_the_available_network_service_descriptors_on_the_all_nfv_os_registered_on_the_sm(
        self,
        *,
        nsd_id: typing.Optional[str] = None,
        nfvo_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Nsd]]:
        """
        Parameters
        ----------
        nsd_id : typing.Optional[str]
            The id for a specific NSD

        nfvo_id : typing.Optional[str]
            The id for a specific NFVO

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Nsd]]
            Successful Operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "nslist",
            method="GET",
            params={
                "nsd-id": nsd_id,
                "nfvo-id": nfvo_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Nsd],
                    parse_obj_as(
                        type_=typing.List[Nsd],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
