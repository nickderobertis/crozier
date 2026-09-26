

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.config_state_response import ConfigStateResponse
from ..types.endpoint_secret_response import EndpointSecretResponse
from ..types.endpoint_stanza import EndpointStanza
from ..types.http_validation_error import HttpValidationError
from ..types.probe_candidate_response import ProbeCandidateResponse
from ..types.provider_health_row import ProviderHealthRow
from ..types.provider_probe_response import ProviderProbeResponse
from ..types.providers_summary_response import ProvidersSummaryResponse
from ..types.save_endpoints_response import SaveEndpointsResponse
from ..types.store_secret_response import StoreSecretResponse
from .types.create_endpoint_request_protocol import CreateEndpointRequestProtocol
from .types.probe_candidate_request_protocol import ProbeCandidateRequestProtocol
from .types.update_endpoint_request_protocol import UpdateEndpointRequestProtocol
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_config_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConfigStateResponse]:
        """
        Return the on-disk YAML body and its SHA-256 checksum.

        Kept for legacy/admin tools that need an explicit config-body save path.
        Bootstrapping the live config file is a lifespan concern
        (``apps.api.main._bootstrap_config_if_missing``), so this route is
        side-effect-free; if the file truly doesn't exist, 404.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigStateResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/providers/config-state",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigStateResponse,
                    parse_obj_as(
                        type_=ConfigStateResponse,
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

    def save_endpoints(
        self, *, expected_sha256: str, new_yaml: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SaveEndpointsResponse]:
        """
        Save the new config YAML body.  ADR-010 v2 lock+checksum semantics.

        Parameters
        ----------
        expected_sha256 : str

        new_yaml : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SaveEndpointsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/providers/endpoints",
            method="POST",
            json={
                "expected_sha256": expected_sha256,
                "new_yaml": new_yaml,
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
                    SaveEndpointsResponse,
                    parse_obj_as(
                        type_=SaveEndpointsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_endpoint(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointStanza]:
        """
        Return the structured stanza for *role* so the UI can prefill the edit modal.

        Parameters
        ----------
        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointStanza]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/providers/endpoints/{encode_path_param(role)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointStanza,
                    parse_obj_as(
                        type_=EndpointStanza,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def create_endpoint(
        self,
        role: str,
        *,
        api_key: str,
        base_url: str,
        model: str,
        name: str,
        protocol: CreateEndpointRequestProtocol,
        adapter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SaveEndpointsResponse]:
        """
        Create a single role stanza without exposing YAML editing to the UI.

        Parameters
        ----------
        role : str

        api_key : str

        base_url : str

        model : str

        name : str

        protocol : CreateEndpointRequestProtocol

        adapter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SaveEndpointsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/providers/endpoints/{encode_path_param(role)}",
            method="POST",
            json={
                "adapter": adapter,
                "api_key": api_key,
                "base_url": base_url,
                "model": model,
                "name": name,
                "protocol": protocol,
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
                    SaveEndpointsResponse,
                    parse_obj_as(
                        type_=SaveEndpointsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_endpoint(
        self,
        role: str,
        *,
        base_url: str,
        model: str,
        name: str,
        protocol: UpdateEndpointRequestProtocol,
        adapter: typing.Optional[str] = OMIT,
        api_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SaveEndpointsResponse]:
        """
        Replace a single role's stanza.

        ``api_key`` semantics: ``None``, empty string, and whitespace-only all
        mean "preserve the existing env-var binding on disk".  Any other value
        is persisted to the secrets store and the YAML's ``api_key_env`` is
        rewritten to the derived env name.  To explicitly unbind, DELETE the
        role and re-POST.

        Parameters
        ----------
        role : str

        base_url : str

        model : str

        name : str

        protocol : UpdateEndpointRequestProtocol

        adapter : typing.Optional[str]

        api_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SaveEndpointsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/providers/endpoints/{encode_path_param(role)}",
            method="PUT",
            json={
                "adapter": adapter,
                "api_key": api_key,
                "base_url": base_url,
                "model": model,
                "name": name,
                "protocol": protocol,
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
                    SaveEndpointsResponse,
                    parse_obj_as(
                        type_=SaveEndpointsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def delete_endpoint(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SaveEndpointsResponse]:
        """
        Remove a role's stanza from config.yaml and re-boot the registry.

        Read-modify-write under the same lock+checksum protocol as POST.  Missing
        role → 404.  Required roles (``REQUIRED_ROLES``) → 409; deleting them
        would crash the next startup with ERR-PROV-001.  Use PUT to swap settings.

        Parameters
        ----------
        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SaveEndpointsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/providers/endpoints/{encode_path_param(role)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SaveEndpointsResponse,
                    parse_obj_as(
                        type_=SaveEndpointsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_endpoint_secret(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointSecretResponse]:
        """
        Return the locally saved secret for *role*.

        Only keys saved through ``data/secrets.json`` are revealable.  If the
        endpoint is backed by a shell/environment variable, the UI can still probe
        it via ``api_key_env`` but the plaintext value is not exposed here.

        Parameters
        ----------
        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointSecretResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/providers/endpoints/{encode_path_param(role)}/secret",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointSecretResponse,
                    parse_obj_as(
                        type_=EndpointSecretResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_provider_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ProviderHealthRow]]:
        """
        Per-role health snapshot derived from ``app.state.registry``.

        Latency probes are not yet implemented (status/latency_ms stubbed to
        None).  When a known role has no binding, the row carries the role
        name in ``unbound`` so the frontend can render the warning chip.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ProviderHealthRow]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/providers/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProviderHealthRow],
                    parse_obj_as(
                        type_=typing.List[ProviderHealthRow],
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

    def list_provider_models(
        self, *, role: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProviderProbeResponse]:
        """
        Probe registry-bound adapter model catalogs.

        Each adapter hits its own ``/models`` endpoint (OpenAI: ``{base_url}/models``,
        Anthropic: ``{base_url}/v1/models``). Passing ``?role=llm`` probes just one
        role so the UI can test a row without waiting for every configured backend.

        Parameters
        ----------
        role : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderProbeResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/providers/models",
            method="GET",
            params={
                "role": role,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProviderProbeResponse,
                    parse_obj_as(
                        type_=ProviderProbeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def probe_candidate(
        self,
        *,
        base_url: str,
        protocol: ProbeCandidateRequestProtocol,
        adapter: typing.Optional[str] = OMIT,
        api_key: typing.Optional[str] = OMIT,
        api_key_env: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProbeCandidateResponse]:
        """
        Probe a candidate (un-registered) endpoint and return its model catalog.

        Accepts either an existing ``api_key_env`` name (looked up via
        ``os.environ``) or an inline ``api_key`` (used directly for the probe but
        never persisted).  The inline path lets the AddEndpointModal probe a
        freshly-pasted key before the operator commits to saving it.

        Adapter contract: ``probe()`` never raises — failures surface as
        ``ok=False`` with an ``error`` string.

        Parameters
        ----------
        base_url : str

        protocol : ProbeCandidateRequestProtocol

        adapter : typing.Optional[str]

        api_key : typing.Optional[str]

        api_key_env : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProbeCandidateResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/providers/probe",
            method="POST",
            json={
                "adapter": adapter,
                "api_key": api_key,
                "api_key_env": api_key_env,
                "base_url": base_url,
                "protocol": protocol,
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
                    ProbeCandidateResponse,
                    parse_obj_as(
                        type_=ProbeCandidateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def store_secret(
        self, *, api_key: str, name: str, role: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StoreSecretResponse]:
        """
        Persist an API key to the gitignored secrets store + inject into env.

        Derives a deterministic env-var name from ``role`` + ``name`` so the
        operator never has to invent one.  The plaintext key lives only in
        ``data/secrets.json`` (gitignored); ``config.yaml`` continues to store
        only the env-var name per ADR-011.

        Parameters
        ----------
        api_key : str

        name : str

        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StoreSecretResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/providers/secrets",
            method="POST",
            json={
                "api_key": api_key,
                "name": name,
                "role": role,
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
                    StoreSecretResponse,
                    parse_obj_as(
                        type_=StoreSecretResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_provider_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvidersSummaryResponse]:
        """
        Summary of the on-disk ``config.yaml``.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvidersSummaryResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/providers/summary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvidersSummaryResponse,
                    parse_obj_as(
                        type_=ProvidersSummaryResponse,
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


class AsyncRawProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_config_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConfigStateResponse]:
        """
        Return the on-disk YAML body and its SHA-256 checksum.

        Kept for legacy/admin tools that need an explicit config-body save path.
        Bootstrapping the live config file is a lifespan concern
        (``apps.api.main._bootstrap_config_if_missing``), so this route is
        side-effect-free; if the file truly doesn't exist, 404.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigStateResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/providers/config-state",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigStateResponse,
                    parse_obj_as(
                        type_=ConfigStateResponse,
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

    async def save_endpoints(
        self, *, expected_sha256: str, new_yaml: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SaveEndpointsResponse]:
        """
        Save the new config YAML body.  ADR-010 v2 lock+checksum semantics.

        Parameters
        ----------
        expected_sha256 : str

        new_yaml : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SaveEndpointsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/providers/endpoints",
            method="POST",
            json={
                "expected_sha256": expected_sha256,
                "new_yaml": new_yaml,
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
                    SaveEndpointsResponse,
                    parse_obj_as(
                        type_=SaveEndpointsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_endpoint(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointStanza]:
        """
        Return the structured stanza for *role* so the UI can prefill the edit modal.

        Parameters
        ----------
        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointStanza]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/providers/endpoints/{encode_path_param(role)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointStanza,
                    parse_obj_as(
                        type_=EndpointStanza,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def create_endpoint(
        self,
        role: str,
        *,
        api_key: str,
        base_url: str,
        model: str,
        name: str,
        protocol: CreateEndpointRequestProtocol,
        adapter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SaveEndpointsResponse]:
        """
        Create a single role stanza without exposing YAML editing to the UI.

        Parameters
        ----------
        role : str

        api_key : str

        base_url : str

        model : str

        name : str

        protocol : CreateEndpointRequestProtocol

        adapter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SaveEndpointsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/providers/endpoints/{encode_path_param(role)}",
            method="POST",
            json={
                "adapter": adapter,
                "api_key": api_key,
                "base_url": base_url,
                "model": model,
                "name": name,
                "protocol": protocol,
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
                    SaveEndpointsResponse,
                    parse_obj_as(
                        type_=SaveEndpointsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_endpoint(
        self,
        role: str,
        *,
        base_url: str,
        model: str,
        name: str,
        protocol: UpdateEndpointRequestProtocol,
        adapter: typing.Optional[str] = OMIT,
        api_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SaveEndpointsResponse]:
        """
        Replace a single role's stanza.

        ``api_key`` semantics: ``None``, empty string, and whitespace-only all
        mean "preserve the existing env-var binding on disk".  Any other value
        is persisted to the secrets store and the YAML's ``api_key_env`` is
        rewritten to the derived env name.  To explicitly unbind, DELETE the
        role and re-POST.

        Parameters
        ----------
        role : str

        base_url : str

        model : str

        name : str

        protocol : UpdateEndpointRequestProtocol

        adapter : typing.Optional[str]

        api_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SaveEndpointsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/providers/endpoints/{encode_path_param(role)}",
            method="PUT",
            json={
                "adapter": adapter,
                "api_key": api_key,
                "base_url": base_url,
                "model": model,
                "name": name,
                "protocol": protocol,
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
                    SaveEndpointsResponse,
                    parse_obj_as(
                        type_=SaveEndpointsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def delete_endpoint(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SaveEndpointsResponse]:
        """
        Remove a role's stanza from config.yaml and re-boot the registry.

        Read-modify-write under the same lock+checksum protocol as POST.  Missing
        role → 404.  Required roles (``REQUIRED_ROLES``) → 409; deleting them
        would crash the next startup with ERR-PROV-001.  Use PUT to swap settings.

        Parameters
        ----------
        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SaveEndpointsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/providers/endpoints/{encode_path_param(role)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SaveEndpointsResponse,
                    parse_obj_as(
                        type_=SaveEndpointsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_endpoint_secret(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointSecretResponse]:
        """
        Return the locally saved secret for *role*.

        Only keys saved through ``data/secrets.json`` are revealable.  If the
        endpoint is backed by a shell/environment variable, the UI can still probe
        it via ``api_key_env`` but the plaintext value is not exposed here.

        Parameters
        ----------
        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointSecretResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/providers/endpoints/{encode_path_param(role)}/secret",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointSecretResponse,
                    parse_obj_as(
                        type_=EndpointSecretResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_provider_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ProviderHealthRow]]:
        """
        Per-role health snapshot derived from ``app.state.registry``.

        Latency probes are not yet implemented (status/latency_ms stubbed to
        None).  When a known role has no binding, the row carries the role
        name in ``unbound`` so the frontend can render the warning chip.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ProviderHealthRow]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/providers/health",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProviderHealthRow],
                    parse_obj_as(
                        type_=typing.List[ProviderHealthRow],
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

    async def list_provider_models(
        self, *, role: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProviderProbeResponse]:
        """
        Probe registry-bound adapter model catalogs.

        Each adapter hits its own ``/models`` endpoint (OpenAI: ``{base_url}/models``,
        Anthropic: ``{base_url}/v1/models``). Passing ``?role=llm`` probes just one
        role so the UI can test a row without waiting for every configured backend.

        Parameters
        ----------
        role : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderProbeResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/providers/models",
            method="GET",
            params={
                "role": role,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProviderProbeResponse,
                    parse_obj_as(
                        type_=ProviderProbeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def probe_candidate(
        self,
        *,
        base_url: str,
        protocol: ProbeCandidateRequestProtocol,
        adapter: typing.Optional[str] = OMIT,
        api_key: typing.Optional[str] = OMIT,
        api_key_env: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProbeCandidateResponse]:
        """
        Probe a candidate (un-registered) endpoint and return its model catalog.

        Accepts either an existing ``api_key_env`` name (looked up via
        ``os.environ``) or an inline ``api_key`` (used directly for the probe but
        never persisted).  The inline path lets the AddEndpointModal probe a
        freshly-pasted key before the operator commits to saving it.

        Adapter contract: ``probe()`` never raises — failures surface as
        ``ok=False`` with an ``error`` string.

        Parameters
        ----------
        base_url : str

        protocol : ProbeCandidateRequestProtocol

        adapter : typing.Optional[str]

        api_key : typing.Optional[str]

        api_key_env : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProbeCandidateResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/providers/probe",
            method="POST",
            json={
                "adapter": adapter,
                "api_key": api_key,
                "api_key_env": api_key_env,
                "base_url": base_url,
                "protocol": protocol,
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
                    ProbeCandidateResponse,
                    parse_obj_as(
                        type_=ProbeCandidateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def store_secret(
        self, *, api_key: str, name: str, role: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StoreSecretResponse]:
        """
        Persist an API key to the gitignored secrets store + inject into env.

        Derives a deterministic env-var name from ``role`` + ``name`` so the
        operator never has to invent one.  The plaintext key lives only in
        ``data/secrets.json`` (gitignored); ``config.yaml`` continues to store
        only the env-var name per ADR-011.

        Parameters
        ----------
        api_key : str

        name : str

        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StoreSecretResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/providers/secrets",
            method="POST",
            json={
                "api_key": api_key,
                "name": name,
                "role": role,
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
                    StoreSecretResponse,
                    parse_obj_as(
                        type_=StoreSecretResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_provider_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvidersSummaryResponse]:
        """
        Summary of the on-disk ``config.yaml``.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvidersSummaryResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/providers/summary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvidersSummaryResponse,
                    parse_obj_as(
                        type_=ProvidersSummaryResponse,
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
