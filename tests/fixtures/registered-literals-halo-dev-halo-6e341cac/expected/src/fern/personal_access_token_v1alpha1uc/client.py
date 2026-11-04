

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.metadata import Metadata
from ..types.pat_spec import PatSpec
from ..types.personal_access_token import PersonalAccessToken
from .raw_client import AsyncRawPersonalAccessTokenV1Alpha1UcClient, RawPersonalAccessTokenV1Alpha1UcClient


OMIT = typing.cast(typing.Any, ...)


class PersonalAccessTokenV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPersonalAccessTokenV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPersonalAccessTokenV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPersonalAccessTokenV1Alpha1UcClient
        """
        return self._raw_client

    def obtain_pats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PersonalAccessToken]:
        """
        Obtain PAT list.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PersonalAccessToken]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.personal_access_token_v1alpha1uc.obtain_pats()
        """
        _response = self._raw_client.obtain_pats(request_options=request_options)
        return _response.data

    def generate_pat(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: typing.Optional[PatSpec] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PersonalAccessToken:
        """
        Generate a PAT.

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : typing.Optional[PatSpec]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonalAccessToken
            default response

        Examples
        --------
        from fern import FernApi, Metadata

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.personal_access_token_v1alpha1uc.generate_pat(
            api_version="apiVersion",
            kind="kind",
            metadata=Metadata(
                name="name",
            ),
        )
        """
        _response = self._raw_client.generate_pat(
            api_version=api_version, kind=kind, metadata=metadata, spec=spec, request_options=request_options
        )
        return _response.data

    def obtain_pat(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> PersonalAccessToken:
        """
        Obtain a PAT.

        Parameters
        ----------
        name : str
            metadata.name of the PAT to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonalAccessToken
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.personal_access_token_v1alpha1uc.obtain_pat(
            name="name",
        )
        """
        _response = self._raw_client.obtain_pat(name, request_options=request_options)
        return _response.data

    def delete_pat(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> PersonalAccessToken:
        """
        Delete a PAT

        Parameters
        ----------
        name : str
            metadata.name of the PAT to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonalAccessToken
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.personal_access_token_v1alpha1uc.delete_pat(
            name="name",
        )
        """
        _response = self._raw_client.delete_pat(name, request_options=request_options)
        return _response.data

    def restore_pat(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> PersonalAccessToken:
        """
        Restore a PAT.

        Parameters
        ----------
        name : str
            metadata.name of the PAT to restore.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonalAccessToken
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.personal_access_token_v1alpha1uc.restore_pat(
            name="name",
        )
        """
        _response = self._raw_client.restore_pat(name, request_options=request_options)
        return _response.data

    def revoke_pat(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> PersonalAccessToken:
        """
        Revoke a PAT

        Parameters
        ----------
        name : str
            metadata.name of the PAT to revoke.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonalAccessToken
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.personal_access_token_v1alpha1uc.revoke_pat(
            name="name",
        )
        """
        _response = self._raw_client.revoke_pat(name, request_options=request_options)
        return _response.data


class AsyncPersonalAccessTokenV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPersonalAccessTokenV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPersonalAccessTokenV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPersonalAccessTokenV1Alpha1UcClient
        """
        return self._raw_client

    async def obtain_pats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PersonalAccessToken]:
        """
        Obtain PAT list.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PersonalAccessToken]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.personal_access_token_v1alpha1uc.obtain_pats()


        asyncio.run(main())
        """
        _response = await self._raw_client.obtain_pats(request_options=request_options)
        return _response.data

    async def generate_pat(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: typing.Optional[PatSpec] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PersonalAccessToken:
        """
        Generate a PAT.

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : typing.Optional[PatSpec]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonalAccessToken
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Metadata

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.personal_access_token_v1alpha1uc.generate_pat(
                api_version="apiVersion",
                kind="kind",
                metadata=Metadata(
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_pat(
            api_version=api_version, kind=kind, metadata=metadata, spec=spec, request_options=request_options
        )
        return _response.data

    async def obtain_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PersonalAccessToken:
        """
        Obtain a PAT.

        Parameters
        ----------
        name : str
            metadata.name of the PAT to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonalAccessToken
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.personal_access_token_v1alpha1uc.obtain_pat(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.obtain_pat(name, request_options=request_options)
        return _response.data

    async def delete_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PersonalAccessToken:
        """
        Delete a PAT

        Parameters
        ----------
        name : str
            metadata.name of the PAT to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonalAccessToken
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.personal_access_token_v1alpha1uc.delete_pat(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_pat(name, request_options=request_options)
        return _response.data

    async def restore_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PersonalAccessToken:
        """
        Restore a PAT.

        Parameters
        ----------
        name : str
            metadata.name of the PAT to restore.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonalAccessToken
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.personal_access_token_v1alpha1uc.restore_pat(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_pat(name, request_options=request_options)
        return _response.data

    async def revoke_pat(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PersonalAccessToken:
        """
        Revoke a PAT

        Parameters
        ----------
        name : str
            metadata.name of the PAT to revoke.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PersonalAccessToken
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.personal_access_token_v1alpha1uc.revoke_pat(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_pat(name, request_options=request_options)
        return _response.data
