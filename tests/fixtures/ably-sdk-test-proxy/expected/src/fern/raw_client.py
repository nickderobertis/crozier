

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.fault_simulation_dto import FaultSimulationDto
from pydantic import ValidationError


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_faults(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[typing.List[str]]:
        """
        Lists all of the faults that the proxy is capable of simulating.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            Successful operation. Returns a list of all fault names.
        """
        _response = self._client_wrapper.httpx_client.request(
            "faults",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def create_fault_simulation(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FaultSimulationDto]:
        """
        A fault simulation implements a specific type of connectivity fault that might occur during the use of the Asset Tracking SDK. In order to simulate a fault, it creates and manipulates a proxy that transparently sits between the client and the Ably Realtime service. The fault simulation returned by this endpoint provides details of how a client can connect to its proxy.

        Faults also specify what state Trackables should enter during a fault and after it has been resolved, so that assertions can be made while testing common use-cases.

        A fault simulation does not have any effect on the connection’s behaviour until it is _enabled_. To enable a fault simulation, use the `POST /fault-simulations/{id}/enable` endpoint.

        At the moment, all created proxies listen on the same port, so it is not possible to have multiple proxies active simultaneously – in order to create a new fault simulation you must first clean up the previous one using the `POST /fault-simulations/{id}/clean-up` endpoint. This is a limitation of the current implementation, which will be resolved in the future.

        Parameters
        ----------
        name : str
            Name of fault to create a simulation for. This must be one of the fault names returned by the `GET /faults` endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FaultSimulationDto]
            Successful operation. Returns a representation of the created fault simulation and details of how to connect to its proxy.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"faults/{encode_path_param(name)}/simulation",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FaultSimulationDto,
                    parse_obj_as(
                        type_=FaultSimulationDto,
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

    def enable_fault_simulation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Breaks the proxy using the fault-specific failure conditions.

        Parameters
        ----------
        id : str
            ID of fault simulation to enable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fault-simulations/{encode_path_param(id)}/enable",
            method="POST",
            request_options=request_options,
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

    def resolve_fault_simulation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Restores the proxy to normal functionality.

        Parameters
        ----------
        id : str
            ID of fault simulation to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fault-simulations/{encode_path_param(id)}/resolve",
            method="POST",
            request_options=request_options,
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

    def clean_up_fault_simulation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Stops the proxy. This should be called at the end of each test case that creates a fault simulation.

        Parameters
        ----------
        id : str
            ID of fault simulation to clean up

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"fault-simulations/{encode_path_param(id)}/clean-up",
            method="POST",
            request_options=request_options,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_faults(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Lists all of the faults that the proxy is capable of simulating.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            Successful operation. Returns a list of all fault names.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "faults",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def create_fault_simulation(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FaultSimulationDto]:
        """
        A fault simulation implements a specific type of connectivity fault that might occur during the use of the Asset Tracking SDK. In order to simulate a fault, it creates and manipulates a proxy that transparently sits between the client and the Ably Realtime service. The fault simulation returned by this endpoint provides details of how a client can connect to its proxy.

        Faults also specify what state Trackables should enter during a fault and after it has been resolved, so that assertions can be made while testing common use-cases.

        A fault simulation does not have any effect on the connection’s behaviour until it is _enabled_. To enable a fault simulation, use the `POST /fault-simulations/{id}/enable` endpoint.

        At the moment, all created proxies listen on the same port, so it is not possible to have multiple proxies active simultaneously – in order to create a new fault simulation you must first clean up the previous one using the `POST /fault-simulations/{id}/clean-up` endpoint. This is a limitation of the current implementation, which will be resolved in the future.

        Parameters
        ----------
        name : str
            Name of fault to create a simulation for. This must be one of the fault names returned by the `GET /faults` endpoint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FaultSimulationDto]
            Successful operation. Returns a representation of the created fault simulation and details of how to connect to its proxy.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"faults/{encode_path_param(name)}/simulation",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FaultSimulationDto,
                    parse_obj_as(
                        type_=FaultSimulationDto,
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

    async def enable_fault_simulation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Breaks the proxy using the fault-specific failure conditions.

        Parameters
        ----------
        id : str
            ID of fault simulation to enable

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fault-simulations/{encode_path_param(id)}/enable",
            method="POST",
            request_options=request_options,
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

    async def resolve_fault_simulation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Restores the proxy to normal functionality.

        Parameters
        ----------
        id : str
            ID of fault simulation to resolve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fault-simulations/{encode_path_param(id)}/resolve",
            method="POST",
            request_options=request_options,
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

    async def clean_up_fault_simulation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Stops the proxy. This should be called at the end of each test case that creates a fault simulation.

        Parameters
        ----------
        id : str
            ID of fault simulation to clean up

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"fault-simulations/{encode_path_param(id)}/clean-up",
            method="POST",
            request_options=request_options,
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
