

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_implemented_error import NotImplementedError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.register_result import RegisterResult
from ..types.result import Result
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRegistryApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def register_product_dpp(
        self,
        *,
        unique_product_identifier: str,
        digital_product_passport_id: str,
        unique_economic_operator_identifier: str,
        dpp_api_endpoint: str,
        backup_unique_economic_operator_identifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RegisterResult]:
        """
        Registers a new DPP at the DPP registry (served by the registry server) and returns a unique registration identifier.

        Parameters
        ----------
        unique_product_identifier : str
            Unique product identifier per EN 18219.

        digital_product_passport_id : str
            The DPP instance identifier.

        unique_economic_operator_identifier : str
            Economic operator identifier per EN 18219.

        dpp_api_endpoint : str
            URL of the DPP API service hosting this DPP.

        backup_unique_economic_operator_identifier : typing.Optional[str]
            Economic operator identifier of the back-up operator per EN 18219.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RegisterResult]
            DPP registered.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/registerDPP",
            method="POST",
            json={
                "uniqueProductIdentifier": unique_product_identifier,
                "digitalProductPassportId": digital_product_passport_id,
                "uniqueEconomicOperatorIdentifier": unique_economic_operator_identifier,
                "backupUniqueEconomicOperatorIdentifier": backup_unique_economic_operator_identifier,
                "dppApiEndpoint": dpp_api_endpoint,
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
                    RegisterResult,
                    parse_obj_as(
                        type_=RegisterResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
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


class AsyncRawRegistryApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def register_product_dpp(
        self,
        *,
        unique_product_identifier: str,
        digital_product_passport_id: str,
        unique_economic_operator_identifier: str,
        dpp_api_endpoint: str,
        backup_unique_economic_operator_identifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RegisterResult]:
        """
        Registers a new DPP at the DPP registry (served by the registry server) and returns a unique registration identifier.

        Parameters
        ----------
        unique_product_identifier : str
            Unique product identifier per EN 18219.

        digital_product_passport_id : str
            The DPP instance identifier.

        unique_economic_operator_identifier : str
            Economic operator identifier per EN 18219.

        dpp_api_endpoint : str
            URL of the DPP API service hosting this DPP.

        backup_unique_economic_operator_identifier : typing.Optional[str]
            Economic operator identifier of the back-up operator per EN 18219.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RegisterResult]
            DPP registered.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/registerDPP",
            method="POST",
            json={
                "uniqueProductIdentifier": unique_product_identifier,
                "digitalProductPassportId": digital_product_passport_id,
                "uniqueEconomicOperatorIdentifier": unique_economic_operator_identifier,
                "backupUniqueEconomicOperatorIdentifier": backup_unique_economic_operator_identifier,
                "dppApiEndpoint": dpp_api_endpoint,
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
                    RegisterResult,
                    parse_obj_as(
                        type_=RegisterResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 501:
                raise NotImplementedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Result,
                        parse_obj_as(
                            type_=Result,
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
