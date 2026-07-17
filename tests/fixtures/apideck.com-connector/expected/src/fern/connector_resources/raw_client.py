

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.get_connector_resource_response import GetConnectorResourceResponse
from ..types.not_found_response import NotFoundResponse
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unified_api_id import UnifiedApiId
from pydantic import ValidationError


class RawConnectorResourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def one(
        self,
        id: str,
        resource_id: str,
        *,
        unified_api: typing.Optional[UnifiedApiId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetConnectorResourceResponse]:
        """
        Get Connector Resource

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        resource_id : str
            ID of the resource you are acting upon.

        unified_api : typing.Optional[UnifiedApiId]
            Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetConnectorResourceResponse]
            ConnectorResources
        """
        _response = self._client_wrapper.httpx_client.request(
            f"connector/connectors/{encode_path_param(id)}/resources/{encode_path_param(resource_id)}",
            method="GET",
            params={
                "unified_api": unified_api,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectorResourceResponse,
                    parse_obj_as(
                        type_=GetConnectorResourceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
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


class AsyncRawConnectorResourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def one(
        self,
        id: str,
        resource_id: str,
        *,
        unified_api: typing.Optional[UnifiedApiId] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetConnectorResourceResponse]:
        """
        Get Connector Resource

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        resource_id : str
            ID of the resource you are acting upon.

        unified_api : typing.Optional[UnifiedApiId]
            Specify unified API for the connector resource. This is useful when a resource appears in multiple APIs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetConnectorResourceResponse]
            ConnectorResources
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"connector/connectors/{encode_path_param(id)}/resources/{encode_path_param(resource_id)}",
            method="GET",
            params={
                "unified_api": unified_api,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetConnectorResourceResponse,
                    parse_obj_as(
                        type_=GetConnectorResourceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
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
