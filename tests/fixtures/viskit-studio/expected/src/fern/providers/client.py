

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_state_response import ConfigStateResponse
from ..types.endpoint_secret_response import EndpointSecretResponse
from ..types.endpoint_stanza import EndpointStanza
from ..types.probe_candidate_response import ProbeCandidateResponse
from ..types.provider_health_row import ProviderHealthRow
from ..types.provider_probe_response import ProviderProbeResponse
from ..types.providers_summary_response import ProvidersSummaryResponse
from ..types.save_endpoints_response import SaveEndpointsResponse
from ..types.store_secret_response import StoreSecretResponse
from .raw_client import AsyncRawProvidersClient, RawProvidersClient
from .types.create_endpoint_request_protocol import CreateEndpointRequestProtocol
from .types.probe_candidate_request_protocol import ProbeCandidateRequestProtocol
from .types.update_endpoint_request_protocol import UpdateEndpointRequestProtocol


OMIT = typing.cast(typing.Any, ...)


class ProvidersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProvidersClient
        """
        return self._raw_client

    def get_config_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConfigStateResponse:
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
        ConfigStateResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.get_config_state()
        """
        _response = self._raw_client.get_config_state(request_options=request_options)
        return _response.data

    def save_endpoints(
        self, *, expected_sha256: str, new_yaml: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SaveEndpointsResponse:
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
        SaveEndpointsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.save_endpoints(
            expected_sha256="expected_sha256",
            new_yaml="new_yaml",
        )
        """
        _response = self._raw_client.save_endpoints(
            expected_sha256=expected_sha256, new_yaml=new_yaml, request_options=request_options
        )
        return _response.data

    def get_endpoint(self, role: str, *, request_options: typing.Optional[RequestOptions] = None) -> EndpointStanza:
        """
        Return the structured stanza for *role* so the UI can prefill the edit modal.

        Parameters
        ----------
        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointStanza
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.get_endpoint(
            role="role",
        )
        """
        _response = self._raw_client.get_endpoint(role, request_options=request_options)
        return _response.data

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
    ) -> SaveEndpointsResponse:
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
        SaveEndpointsResponse
            Successful Response

        Examples
        --------
        from fern.providers import CreateEndpointRequestProtocol

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.create_endpoint(
            role="role",
            api_key="api_key",
            base_url="base_url",
            model="model",
            name="name",
            protocol=CreateEndpointRequestProtocol.OPENAI_COMPATIBLE,
        )
        """
        _response = self._raw_client.create_endpoint(
            role,
            api_key=api_key,
            base_url=base_url,
            model=model,
            name=name,
            protocol=protocol,
            adapter=adapter,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SaveEndpointsResponse:
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
        SaveEndpointsResponse
            Successful Response

        Examples
        --------
        from fern.providers import UpdateEndpointRequestProtocol

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.update_endpoint(
            role="role",
            base_url="base_url",
            model="model",
            name="name",
            protocol=UpdateEndpointRequestProtocol.OPENAI_COMPATIBLE,
        )
        """
        _response = self._raw_client.update_endpoint(
            role,
            base_url=base_url,
            model=model,
            name=name,
            protocol=protocol,
            adapter=adapter,
            api_key=api_key,
            request_options=request_options,
        )
        return _response.data

    def delete_endpoint(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SaveEndpointsResponse:
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
        SaveEndpointsResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.delete_endpoint(
            role="role",
        )
        """
        _response = self._raw_client.delete_endpoint(role, request_options=request_options)
        return _response.data

    def get_endpoint_secret(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointSecretResponse:
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
        EndpointSecretResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.get_endpoint_secret(
            role="role",
        )
        """
        _response = self._raw_client.get_endpoint_secret(role, request_options=request_options)
        return _response.data

    def get_provider_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProviderHealthRow]:
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
        typing.List[ProviderHealthRow]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.get_provider_health()
        """
        _response = self._raw_client.get_provider_health(request_options=request_options)
        return _response.data

    def list_provider_models(
        self, *, role: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderProbeResponse:
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
        ProviderProbeResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.list_provider_models()
        """
        _response = self._raw_client.list_provider_models(role=role, request_options=request_options)
        return _response.data

    def probe_candidate(
        self,
        *,
        base_url: str,
        protocol: ProbeCandidateRequestProtocol,
        adapter: typing.Optional[str] = OMIT,
        api_key: typing.Optional[str] = OMIT,
        api_key_env: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProbeCandidateResponse:
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
        ProbeCandidateResponse
            Successful Response

        Examples
        --------
        from fern.providers import ProbeCandidateRequestProtocol

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.probe_candidate(
            base_url="base_url",
            protocol=ProbeCandidateRequestProtocol.OPENAI_COMPATIBLE,
        )
        """
        _response = self._raw_client.probe_candidate(
            base_url=base_url,
            protocol=protocol,
            adapter=adapter,
            api_key=api_key,
            api_key_env=api_key_env,
            request_options=request_options,
        )
        return _response.data

    def store_secret(
        self, *, api_key: str, name: str, role: str, request_options: typing.Optional[RequestOptions] = None
    ) -> StoreSecretResponse:
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
        StoreSecretResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.store_secret(
            api_key="api_key",
            name="name",
            role="role",
        )
        """
        _response = self._raw_client.store_secret(
            api_key=api_key, name=name, role=role, request_options=request_options
        )
        return _response.data

    def get_provider_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvidersSummaryResponse:
        """
        Summary of the on-disk ``config.yaml``.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvidersSummaryResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.providers.get_provider_summary()
        """
        _response = self._raw_client.get_provider_summary(request_options=request_options)
        return _response.data


class AsyncProvidersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProvidersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProvidersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProvidersClient
        """
        return self._raw_client

    async def get_config_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConfigStateResponse:
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
        ConfigStateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.get_config_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_config_state(request_options=request_options)
        return _response.data

    async def save_endpoints(
        self, *, expected_sha256: str, new_yaml: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SaveEndpointsResponse:
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
        SaveEndpointsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.save_endpoints(
                expected_sha256="expected_sha256",
                new_yaml="new_yaml",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_endpoints(
            expected_sha256=expected_sha256, new_yaml=new_yaml, request_options=request_options
        )
        return _response.data

    async def get_endpoint(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointStanza:
        """
        Return the structured stanza for *role* so the UI can prefill the edit modal.

        Parameters
        ----------
        role : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointStanza
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.get_endpoint(
                role="role",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_endpoint(role, request_options=request_options)
        return _response.data

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
    ) -> SaveEndpointsResponse:
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
        SaveEndpointsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.providers import CreateEndpointRequestProtocol

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.create_endpoint(
                role="role",
                api_key="api_key",
                base_url="base_url",
                model="model",
                name="name",
                protocol=CreateEndpointRequestProtocol.OPENAI_COMPATIBLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_endpoint(
            role,
            api_key=api_key,
            base_url=base_url,
            model=model,
            name=name,
            protocol=protocol,
            adapter=adapter,
            request_options=request_options,
        )
        return _response.data

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
    ) -> SaveEndpointsResponse:
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
        SaveEndpointsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.providers import UpdateEndpointRequestProtocol

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.update_endpoint(
                role="role",
                base_url="base_url",
                model="model",
                name="name",
                protocol=UpdateEndpointRequestProtocol.OPENAI_COMPATIBLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_endpoint(
            role,
            base_url=base_url,
            model=model,
            name=name,
            protocol=protocol,
            adapter=adapter,
            api_key=api_key,
            request_options=request_options,
        )
        return _response.data

    async def delete_endpoint(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SaveEndpointsResponse:
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
        SaveEndpointsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.delete_endpoint(
                role="role",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_endpoint(role, request_options=request_options)
        return _response.data

    async def get_endpoint_secret(
        self, role: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointSecretResponse:
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
        EndpointSecretResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.get_endpoint_secret(
                role="role",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_endpoint_secret(role, request_options=request_options)
        return _response.data

    async def get_provider_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ProviderHealthRow]:
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
        typing.List[ProviderHealthRow]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.get_provider_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_provider_health(request_options=request_options)
        return _response.data

    async def list_provider_models(
        self, *, role: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderProbeResponse:
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
        ProviderProbeResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.list_provider_models()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_provider_models(role=role, request_options=request_options)
        return _response.data

    async def probe_candidate(
        self,
        *,
        base_url: str,
        protocol: ProbeCandidateRequestProtocol,
        adapter: typing.Optional[str] = OMIT,
        api_key: typing.Optional[str] = OMIT,
        api_key_env: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProbeCandidateResponse:
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
        ProbeCandidateResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.providers import ProbeCandidateRequestProtocol

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.probe_candidate(
                base_url="base_url",
                protocol=ProbeCandidateRequestProtocol.OPENAI_COMPATIBLE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.probe_candidate(
            base_url=base_url,
            protocol=protocol,
            adapter=adapter,
            api_key=api_key,
            api_key_env=api_key_env,
            request_options=request_options,
        )
        return _response.data

    async def store_secret(
        self, *, api_key: str, name: str, role: str, request_options: typing.Optional[RequestOptions] = None
    ) -> StoreSecretResponse:
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
        StoreSecretResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.store_secret(
                api_key="api_key",
                name="name",
                role="role",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_secret(
            api_key=api_key, name=name, role=role, request_options=request_options
        )
        return _response.data

    async def get_provider_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvidersSummaryResponse:
        """
        Summary of the on-disk ``config.yaml``.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvidersSummaryResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.providers.get_provider_summary()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_provider_summary(request_options=request_options)
        return _response.data
