

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.sandbox_user_company import SandboxUserCompany
from ..types.sandbox_user_company_create import SandboxUserCompanyCreate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSandboxUserCompanyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_sandbox_user_company(
        self, *, request: SandboxUserCompany, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SandboxUserCompanyCreate]:
        """
        Used to create a sandbox userCompany.

        Parameters
        ----------
        request : SandboxUserCompany

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SandboxUserCompanyCreate]
            Used to create a sandbox userCompany.
        """
        _response = self._client_wrapper.httpx_client.request(
            "sandbox-user-company",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SandboxUserCompanyCreate,
                    parse_obj_as(
                        type_=SandboxUserCompanyCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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


class AsyncRawSandboxUserCompanyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_sandbox_user_company(
        self, *, request: SandboxUserCompany, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SandboxUserCompanyCreate]:
        """
        Used to create a sandbox userCompany.

        Parameters
        ----------
        request : SandboxUserCompany

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SandboxUserCompanyCreate]
            Used to create a sandbox userCompany.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sandbox-user-company",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SandboxUserCompanyCreate,
                    parse_obj_as(
                        type_=SandboxUserCompanyCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
