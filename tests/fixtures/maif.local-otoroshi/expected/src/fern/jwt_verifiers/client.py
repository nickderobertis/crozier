

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deleted import Deleted
from ..types.global_jwt_verifier import GlobalJwtVerifier
from ..types.global_jwt_verifier_algo_settings import GlobalJwtVerifierAlgoSettings
from ..types.global_jwt_verifier_source import GlobalJwtVerifierSource
from ..types.global_jwt_verifier_strategy import GlobalJwtVerifierStrategy
from ..types.patch import Patch
from .raw_client import AsyncRawJwtVerifiersClient, RawJwtVerifiersClient


OMIT = typing.cast(typing.Any, ...)


class JwtVerifiersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJwtVerifiersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJwtVerifiersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJwtVerifiersClient
        """
        return self._raw_client

    def find_all_global_jwt_verifiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GlobalJwtVerifier]:
        """
        Get all global JWT verifiers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GlobalJwtVerifier]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.find_all_global_jwt_verifiers()
        """
        _response = self._raw_client.find_all_global_jwt_verifiers(request_options=request_options)
        return _response.data

    def create_global_jwt_verifier(
        self,
        *,
        algo_settings: GlobalJwtVerifierAlgoSettings,
        desc: str,
        enabled: bool,
        id: str,
        name: str,
        source: GlobalJwtVerifierSource,
        strategy: GlobalJwtVerifierStrategy,
        strict: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlobalJwtVerifier:
        """
        Create one global JWT verifiers

        Parameters
        ----------
        algo_settings : GlobalJwtVerifierAlgoSettings

        desc : str
            Verifier description

        enabled : bool
            Is it enabled

        id : str
            Verifier id

        name : str
            Verifier name

        source : GlobalJwtVerifierSource

        strategy : GlobalJwtVerifierStrategy

        strict : bool
            Does it fail if JWT not found

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalJwtVerifier
            Successful operation

        Examples
        --------
        from fern import (
            FernApi,
            HsAlgoSettings,
            InQueryParam,
            PassThrough,
            VerificationSettings,
        )

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.create_global_jwt_verifier(
            algo_settings=HsAlgoSettings(
                secret="a string value",
                size=123123,
                type="a string value",
            ),
            desc="a string value",
            enabled=True,
            id="a string value",
            name="a string value",
            source=InQueryParam(
                name="a string value",
                type="a string value",
            ),
            strategy=PassThrough(
                type="a string value",
                verification_settings=VerificationSettings(
                    fields={"key": "value"},
                ),
            ),
            strict=True,
        )
        """
        _response = self._raw_client.create_global_jwt_verifier(
            algo_settings=algo_settings,
            desc=desc,
            enabled=enabled,
            id=id,
            name=name,
            source=source,
            strategy=strategy,
            strict=strict,
            request_options=request_options,
        )
        return _response.data

    def find_global_jwt_verifiers_by_id(
        self, verifier_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalJwtVerifier:
        """
        Get one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalJwtVerifier
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.find_global_jwt_verifiers_by_id(
            verifier_id="verifierId",
        )
        """
        _response = self._raw_client.find_global_jwt_verifiers_by_id(verifier_id, request_options=request_options)
        return _response.data

    def update_global_jwt_verifier(
        self,
        verifier_id: str,
        *,
        algo_settings: GlobalJwtVerifierAlgoSettings,
        desc: str,
        enabled: bool,
        id: str,
        name: str,
        source: GlobalJwtVerifierSource,
        strategy: GlobalJwtVerifierStrategy,
        strict: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlobalJwtVerifier:
        """
        Update one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        algo_settings : GlobalJwtVerifierAlgoSettings

        desc : str
            Verifier description

        enabled : bool
            Is it enabled

        id : str
            Verifier id

        name : str
            Verifier name

        source : GlobalJwtVerifierSource

        strategy : GlobalJwtVerifierStrategy

        strict : bool
            Does it fail if JWT not found

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalJwtVerifier
            Successful operation

        Examples
        --------
        from fern import (
            FernApi,
            HsAlgoSettings,
            InQueryParam,
            PassThrough,
            VerificationSettings,
        )

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.update_global_jwt_verifier(
            verifier_id="verifierId",
            algo_settings=HsAlgoSettings(
                secret="a string value",
                size=123123,
                type="a string value",
            ),
            desc="a string value",
            enabled=True,
            id="a string value",
            name="a string value",
            source=InQueryParam(
                name="a string value",
                type="a string value",
            ),
            strategy=PassThrough(
                type="a string value",
                verification_settings=VerificationSettings(
                    fields={"key": "value"},
                ),
            ),
            strict=True,
        )
        """
        _response = self._raw_client.update_global_jwt_verifier(
            verifier_id,
            algo_settings=algo_settings,
            desc=desc,
            enabled=enabled,
            id=id,
            name=name,
            source=source,
            strategy=strategy,
            strict=strict,
            request_options=request_options,
        )
        return _response.data

    def delete_global_jwt_verifier(
        self, verifier_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.delete_global_jwt_verifier(
            verifier_id="verifierId",
        )
        """
        _response = self._raw_client.delete_global_jwt_verifier(verifier_id, request_options=request_options)
        return _response.data

    def patch_global_jwt_verifier(
        self, verifier_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalJwtVerifier:
        """
        Update one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalJwtVerifier
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.jwt_verifiers.patch_global_jwt_verifier(
            verifier_id="verifierId",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_global_jwt_verifier(
            verifier_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncJwtVerifiersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJwtVerifiersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJwtVerifiersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJwtVerifiersClient
        """
        return self._raw_client

    async def find_all_global_jwt_verifiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GlobalJwtVerifier]:
        """
        Get all global JWT verifiers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GlobalJwtVerifier]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.jwt_verifiers.find_all_global_jwt_verifiers()


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all_global_jwt_verifiers(request_options=request_options)
        return _response.data

    async def create_global_jwt_verifier(
        self,
        *,
        algo_settings: GlobalJwtVerifierAlgoSettings,
        desc: str,
        enabled: bool,
        id: str,
        name: str,
        source: GlobalJwtVerifierSource,
        strategy: GlobalJwtVerifierStrategy,
        strict: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlobalJwtVerifier:
        """
        Create one global JWT verifiers

        Parameters
        ----------
        algo_settings : GlobalJwtVerifierAlgoSettings

        desc : str
            Verifier description

        enabled : bool
            Is it enabled

        id : str
            Verifier id

        name : str
            Verifier name

        source : GlobalJwtVerifierSource

        strategy : GlobalJwtVerifierStrategy

        strict : bool
            Does it fail if JWT not found

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalJwtVerifier
            Successful operation

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            HsAlgoSettings,
            InQueryParam,
            PassThrough,
            VerificationSettings,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.jwt_verifiers.create_global_jwt_verifier(
                algo_settings=HsAlgoSettings(
                    secret="a string value",
                    size=123123,
                    type="a string value",
                ),
                desc="a string value",
                enabled=True,
                id="a string value",
                name="a string value",
                source=InQueryParam(
                    name="a string value",
                    type="a string value",
                ),
                strategy=PassThrough(
                    type="a string value",
                    verification_settings=VerificationSettings(
                        fields={"key": "value"},
                    ),
                ),
                strict=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_global_jwt_verifier(
            algo_settings=algo_settings,
            desc=desc,
            enabled=enabled,
            id=id,
            name=name,
            source=source,
            strategy=strategy,
            strict=strict,
            request_options=request_options,
        )
        return _response.data

    async def find_global_jwt_verifiers_by_id(
        self, verifier_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalJwtVerifier:
        """
        Get one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalJwtVerifier
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.jwt_verifiers.find_global_jwt_verifiers_by_id(
                verifier_id="verifierId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_global_jwt_verifiers_by_id(verifier_id, request_options=request_options)
        return _response.data

    async def update_global_jwt_verifier(
        self,
        verifier_id: str,
        *,
        algo_settings: GlobalJwtVerifierAlgoSettings,
        desc: str,
        enabled: bool,
        id: str,
        name: str,
        source: GlobalJwtVerifierSource,
        strategy: GlobalJwtVerifierStrategy,
        strict: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GlobalJwtVerifier:
        """
        Update one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        algo_settings : GlobalJwtVerifierAlgoSettings

        desc : str
            Verifier description

        enabled : bool
            Is it enabled

        id : str
            Verifier id

        name : str
            Verifier name

        source : GlobalJwtVerifierSource

        strategy : GlobalJwtVerifierStrategy

        strict : bool
            Does it fail if JWT not found

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalJwtVerifier
            Successful operation

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            HsAlgoSettings,
            InQueryParam,
            PassThrough,
            VerificationSettings,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.jwt_verifiers.update_global_jwt_verifier(
                verifier_id="verifierId",
                algo_settings=HsAlgoSettings(
                    secret="a string value",
                    size=123123,
                    type="a string value",
                ),
                desc="a string value",
                enabled=True,
                id="a string value",
                name="a string value",
                source=InQueryParam(
                    name="a string value",
                    type="a string value",
                ),
                strategy=PassThrough(
                    type="a string value",
                    verification_settings=VerificationSettings(
                        fields={"key": "value"},
                    ),
                ),
                strict=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_global_jwt_verifier(
            verifier_id,
            algo_settings=algo_settings,
            desc=desc,
            enabled=enabled,
            id=id,
            name=name,
            source=source,
            strategy=strategy,
            strict=strict,
            request_options=request_options,
        )
        return _response.data

    async def delete_global_jwt_verifier(
        self, verifier_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.jwt_verifiers.delete_global_jwt_verifier(
                verifier_id="verifierId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_global_jwt_verifier(verifier_id, request_options=request_options)
        return _response.data

    async def patch_global_jwt_verifier(
        self, verifier_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalJwtVerifier:
        """
        Update one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalJwtVerifier
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchItem, PatchItemOp

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.jwt_verifiers.patch_global_jwt_verifier(
                verifier_id="verifierId",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_global_jwt_verifier(
            verifier_id, request=request, request_options=request_options
        )
        return _response.data
