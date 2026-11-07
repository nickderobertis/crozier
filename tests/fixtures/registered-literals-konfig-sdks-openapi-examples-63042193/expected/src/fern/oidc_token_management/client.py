

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.claim_response import ClaimResponse
from ..types.json_duration import JsonDuration
from .raw_client import AsyncRawOidcTokenManagementClient, RawOidcTokenManagementClient


OMIT = typing.cast(typing.Any, ...)


class OidcTokenManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOidcTokenManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOidcTokenManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOidcTokenManagementClient
        """
        return self._raw_client

    def oidc_token_management_get_org_claims(
        self, org_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClaimResponse:
        """
        Fetches org-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully fetched.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.oidc_token_management.oidc_token_management_get_org_claims(
            org_id="orgID",
        )
        """
        _response = self._raw_client.oidc_token_management_get_org_claims(org_id, request_options=request_options)
        return _response.data

    def oidc_token_management_delete_org_claims(
        self, org_id: str, *, claims: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ClaimResponse:
        """
        Deletes org-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        claims : str
            comma separated list of claims to delete. Valid values are "audience" and "ttl".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully deleted.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.oidc_token_management.oidc_token_management_delete_org_claims(
            org_id="orgID",
            claims="claims",
        )
        """
        _response = self._raw_client.oidc_token_management_delete_org_claims(
            org_id, claims=claims, request_options=request_options
        )
        return _response.data

    def oidc_token_management_update_org_claims(
        self,
        org_id: str,
        *,
        audience: typing.Optional[typing.Sequence[str]] = OMIT,
        ttl: typing.Optional[JsonDuration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClaimResponse:
        """
        Creates/Updates org-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        audience : typing.Optional[typing.Sequence[str]]

        ttl : typing.Optional[JsonDuration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully patched.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.oidc_token_management.oidc_token_management_update_org_claims(
            org_id="orgID",
        )
        """
        _response = self._raw_client.oidc_token_management_update_org_claims(
            org_id, audience=audience, ttl=ttl, request_options=request_options
        )
        return _response.data

    def oidc_token_management_get_project_claims(
        self, org_id: str, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClaimResponse:
        """
        Fetches project-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully fetched.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.oidc_token_management.oidc_token_management_get_project_claims(
            org_id="orgID",
            project_id="projectID",
        )
        """
        _response = self._raw_client.oidc_token_management_get_project_claims(
            org_id, project_id, request_options=request_options
        )
        return _response.data

    def oidc_token_management_delete_project_claims(
        self, org_id: str, project_id: str, *, claims: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ClaimResponse:
        """
        Deletes project-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        project_id : str

        claims : str
            comma separated list of claims to delete. Valid values are "audience" and "ttl".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully deleted.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.oidc_token_management.oidc_token_management_delete_project_claims(
            org_id="orgID",
            project_id="projectID",
            claims="claims",
        )
        """
        _response = self._raw_client.oidc_token_management_delete_project_claims(
            org_id, project_id, claims=claims, request_options=request_options
        )
        return _response.data

    def oidc_token_management_update_project_claims(
        self,
        org_id: str,
        project_id: str,
        *,
        audience: typing.Optional[typing.Sequence[str]] = OMIT,
        ttl: typing.Optional[JsonDuration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClaimResponse:
        """
        Creates/Updates project-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        project_id : str

        audience : typing.Optional[typing.Sequence[str]]

        ttl : typing.Optional[JsonDuration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully patched.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.oidc_token_management.oidc_token_management_update_project_claims(
            org_id="orgID",
            project_id="projectID",
        )
        """
        _response = self._raw_client.oidc_token_management_update_project_claims(
            org_id, project_id, audience=audience, ttl=ttl, request_options=request_options
        )
        return _response.data


class AsyncOidcTokenManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOidcTokenManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOidcTokenManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOidcTokenManagementClient
        """
        return self._raw_client

    async def oidc_token_management_get_org_claims(
        self, org_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClaimResponse:
        """
        Fetches org-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully fetched.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.oidc_token_management.oidc_token_management_get_org_claims(
                org_id="orgID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.oidc_token_management_get_org_claims(org_id, request_options=request_options)
        return _response.data

    async def oidc_token_management_delete_org_claims(
        self, org_id: str, *, claims: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ClaimResponse:
        """
        Deletes org-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        claims : str
            comma separated list of claims to delete. Valid values are "audience" and "ttl".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully deleted.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.oidc_token_management.oidc_token_management_delete_org_claims(
                org_id="orgID",
                claims="claims",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.oidc_token_management_delete_org_claims(
            org_id, claims=claims, request_options=request_options
        )
        return _response.data

    async def oidc_token_management_update_org_claims(
        self,
        org_id: str,
        *,
        audience: typing.Optional[typing.Sequence[str]] = OMIT,
        ttl: typing.Optional[JsonDuration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClaimResponse:
        """
        Creates/Updates org-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        audience : typing.Optional[typing.Sequence[str]]

        ttl : typing.Optional[JsonDuration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully patched.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.oidc_token_management.oidc_token_management_update_org_claims(
                org_id="orgID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.oidc_token_management_update_org_claims(
            org_id, audience=audience, ttl=ttl, request_options=request_options
        )
        return _response.data

    async def oidc_token_management_get_project_claims(
        self, org_id: str, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClaimResponse:
        """
        Fetches project-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully fetched.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.oidc_token_management.oidc_token_management_get_project_claims(
                org_id="orgID",
                project_id="projectID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.oidc_token_management_get_project_claims(
            org_id, project_id, request_options=request_options
        )
        return _response.data

    async def oidc_token_management_delete_project_claims(
        self, org_id: str, project_id: str, *, claims: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ClaimResponse:
        """
        Deletes project-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        project_id : str

        claims : str
            comma separated list of claims to delete. Valid values are "audience" and "ttl".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully deleted.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.oidc_token_management.oidc_token_management_delete_project_claims(
                org_id="orgID",
                project_id="projectID",
                claims="claims",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.oidc_token_management_delete_project_claims(
            org_id, project_id, claims=claims, request_options=request_options
        )
        return _response.data

    async def oidc_token_management_update_project_claims(
        self,
        org_id: str,
        project_id: str,
        *,
        audience: typing.Optional[typing.Sequence[str]] = OMIT,
        ttl: typing.Optional[JsonDuration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClaimResponse:
        """
        Creates/Updates project-level custom claims of OIDC identity tokens

        Parameters
        ----------
        org_id : str

        project_id : str

        audience : typing.Optional[typing.Sequence[str]]

        ttl : typing.Optional[JsonDuration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClaimResponse
            Claims successfully patched.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.oidc_token_management.oidc_token_management_update_project_claims(
                org_id="orgID",
                project_id="projectID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.oidc_token_management_update_project_claims(
            org_id, project_id, audience=audience, ttl=ttl, request_options=request_options
        )
        return _response.data
