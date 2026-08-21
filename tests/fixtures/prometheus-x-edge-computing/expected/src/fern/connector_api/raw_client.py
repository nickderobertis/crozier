

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.consent_id import ConsentId
from ..types.contract_id import ContractId
from ..types.data_id import DataId
from ..types.data_provider_id import DataProviderId
from ..types.function import Function
from ..types.function_id import FunctionId
from ..types.privacy_zone_data import PrivacyZoneData
from ..types.private_data import PrivateData
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConnectorApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_pz_data(
        self,
        *,
        data_provider: typing.Optional[DataProviderId] = OMIT,
        private_data: typing.Optional[DataId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PrivacyZoneData]:
        """


        Parameters
        ----------
        data_provider : typing.Optional[DataProviderId]

        private_data : typing.Optional[DataId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrivacyZoneData]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "getPZData",
            method="POST",
            json={
                "data_provider": data_provider,
                "private_data": private_data,
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
                    PrivacyZoneData,
                    parse_obj_as(
                        type_=PrivacyZoneData,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def request_function(
        self,
        *,
        function: typing.Optional[FunctionId] = OMIT,
        func_contract: typing.Optional[ContractId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Function]:
        """


        Parameters
        ----------
        function : typing.Optional[FunctionId]

        func_contract : typing.Optional[ContractId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Function]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "requestFunction",
            method="POST",
            json={
                "function": function,
                "func_contract": func_contract,
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
                    Function,
                    parse_obj_as(
                        type_=Function,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def request_privacy_preserving_data(
        self,
        *,
        private_data: typing.Optional[DataId] = OMIT,
        data_contract: typing.Optional[ContractId] = OMIT,
        consent: typing.Optional[ConsentId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PrivateData]:
        """


        Parameters
        ----------
        private_data : typing.Optional[DataId]

        data_contract : typing.Optional[ContractId]

        consent : typing.Optional[ConsentId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrivateData]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "requestPrivacyPreservingData",
            method="POST",
            json={
                "private_data": private_data,
                "data_contract": data_contract,
                "consent": consent,
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
                    PrivateData,
                    parse_obj_as(
                        type_=PrivateData,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawConnectorApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_pz_data(
        self,
        *,
        data_provider: typing.Optional[DataProviderId] = OMIT,
        private_data: typing.Optional[DataId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PrivacyZoneData]:
        """


        Parameters
        ----------
        data_provider : typing.Optional[DataProviderId]

        private_data : typing.Optional[DataId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrivacyZoneData]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "getPZData",
            method="POST",
            json={
                "data_provider": data_provider,
                "private_data": private_data,
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
                    PrivacyZoneData,
                    parse_obj_as(
                        type_=PrivacyZoneData,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def request_function(
        self,
        *,
        function: typing.Optional[FunctionId] = OMIT,
        func_contract: typing.Optional[ContractId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Function]:
        """


        Parameters
        ----------
        function : typing.Optional[FunctionId]

        func_contract : typing.Optional[ContractId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Function]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "requestFunction",
            method="POST",
            json={
                "function": function,
                "func_contract": func_contract,
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
                    Function,
                    parse_obj_as(
                        type_=Function,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def request_privacy_preserving_data(
        self,
        *,
        private_data: typing.Optional[DataId] = OMIT,
        data_contract: typing.Optional[ContractId] = OMIT,
        consent: typing.Optional[ConsentId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PrivateData]:
        """


        Parameters
        ----------
        private_data : typing.Optional[DataId]

        data_contract : typing.Optional[ContractId]

        consent : typing.Optional[ConsentId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrivateData]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "requestPrivacyPreservingData",
            method="POST",
            json={
                "private_data": private_data,
                "data_contract": data_contract,
                "consent": consent,
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
                    PrivateData,
                    parse_obj_as(
                        type_=PrivateData,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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
