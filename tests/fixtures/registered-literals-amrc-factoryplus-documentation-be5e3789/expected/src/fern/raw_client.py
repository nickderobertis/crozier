

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.get_cluster_cluster_status_response import GetClusterClusterStatusResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_bootstrap_script_url_for_a_cluster(
        self, cluster: typing.Optional[str], *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        This endpoint is used to fetch the URL to a script to use to bootstrap the edge cluster. The URL returned may contain authentication and may only be valid for a certain length of time. The script needs to be fetched from the returned URL using GET and run using a Bourne shell, with `kubectl` in the PATH and configured to access the edge cluster.

        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster)}/bootstrap-url",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def fetch_cluster_setup_status(
        self, cluster: typing.Optional[str], *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetClusterClusterStatusResponse]:
        """
        The _Edge cluster setup status_ Config Store entries should not normally be accessible except to the Cluster Manager itself. This endpoint is suitable for polling to find out when a cluster is ready to be bootstrapped. Do not rely on any fields other than those documented in the response.

        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetClusterClusterStatusResponse]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetClusterClusterStatusResponse,
                    parse_obj_as(
                        type_=GetClusterClusterStatusResponse,
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

    def update_a_secret_value_on_an_edge_cluster(
        self,
        cluster: typing.Optional[str],
        namespace: typing.Optional[str],
        name: typing.Optional[str],
        key: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        This endpoint accepts secret information, as a binary blob, and arranges to securely make it available as a Kubernetes Secret on the edge cluster. Once encrypted there is no way to retrieve the information without access to the private key on the edge cluster.

        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster UUID

        namespace : typing.Optional[str]
            Kubernetes namespace of Secret to modify

        name : typing.Optional[str]
            Kubernetes name of Secret to modify

        key : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster)}/secret/{encode_path_param(namespace)}/{encode_path_param(name)}/{encode_path_param(key)}",
            method="PUT",
            content=request,
            headers={
                "content-type": "application/octet-stream",
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

    def delete_a_secret_value_from_an_edge_cluster(
        self,
        cluster: typing.Optional[str],
        namespace: typing.Optional[str],
        name: typing.Optional[str],
        key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        The requested key will be removed from the Secret. If the Secret is now empty, the entire Secret will be removed. A successful response from this endpoint does not indicate that the key has actually been removed on the edge cluster yet.

        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster UUID

        namespace : typing.Optional[str]
            Kubernetes namespace of Secret to modify

        name : typing.Optional[str]
            Kubernetes name of Secret to modify

        key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster)}/secret/{encode_path_param(namespace)}/{encode_path_param(name)}/{encode_path_param(key)}",
            method="DELETE",
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

    async def fetch_bootstrap_script_url_for_a_cluster(
        self, cluster: typing.Optional[str], *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        This endpoint is used to fetch the URL to a script to use to bootstrap the edge cluster. The URL returned may contain authentication and may only be valid for a certain length of time. The script needs to be fetched from the returned URL using GET and run using a Bourne shell, with `kubectl` in the PATH and configured to access the edge cluster.

        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster)}/bootstrap-url",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def fetch_cluster_setup_status(
        self, cluster: typing.Optional[str], *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetClusterClusterStatusResponse]:
        """
        The _Edge cluster setup status_ Config Store entries should not normally be accessible except to the Cluster Manager itself. This endpoint is suitable for polling to find out when a cluster is ready to be bootstrapped. Do not rely on any fields other than those documented in the response.

        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetClusterClusterStatusResponse]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetClusterClusterStatusResponse,
                    parse_obj_as(
                        type_=GetClusterClusterStatusResponse,
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

    async def update_a_secret_value_on_an_edge_cluster(
        self,
        cluster: typing.Optional[str],
        namespace: typing.Optional[str],
        name: typing.Optional[str],
        key: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        This endpoint accepts secret information, as a binary blob, and arranges to securely make it available as a Kubernetes Secret on the edge cluster. Once encrypted there is no way to retrieve the information without access to the private key on the edge cluster.

        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster UUID

        namespace : typing.Optional[str]
            Kubernetes namespace of Secret to modify

        name : typing.Optional[str]
            Kubernetes name of Secret to modify

        key : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster)}/secret/{encode_path_param(namespace)}/{encode_path_param(name)}/{encode_path_param(key)}",
            method="PUT",
            content=request,
            headers={
                "content-type": "application/octet-stream",
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

    async def delete_a_secret_value_from_an_edge_cluster(
        self,
        cluster: typing.Optional[str],
        namespace: typing.Optional[str],
        name: typing.Optional[str],
        key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        The requested key will be removed from the Secret. If the Secret is now empty, the entire Secret will be removed. A successful response from this endpoint does not indicate that the key has actually been removed on the edge cluster yet.

        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster UUID

        namespace : typing.Optional[str]
            Kubernetes namespace of Secret to modify

        name : typing.Optional[str]
            Kubernetes name of Secret to modify

        key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"cluster/{encode_path_param(cluster)}/secret/{encode_path_param(namespace)}/{encode_path_param(name)}/{encode_path_param(key)}",
            method="DELETE",
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
