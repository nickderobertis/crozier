

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.certificate import Certificate
from ..types.deleted import Deleted
from ..types.patch import Patch
from .raw_client import AsyncRawCertificatesClient, RawCertificatesClient


OMIT = typing.cast(typing.Any, ...)


class CertificatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCertificatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCertificatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCertificatesClient
        """
        return self._raw_client

    def all_certs(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Certificate]:
        """
        Get all certificates

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Certificate]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.all_certs()
        """
        _response = self._raw_client.all_certs(request_options=request_options)
        return _response.data

    def create_cert(
        self,
        *,
        auto_renew: str,
        ca: str,
        ca_ref: str,
        chain: str,
        domain: str,
        from_: str,
        id: str,
        private_key: str,
        self_signed: str,
        subject: str,
        to: str,
        valid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Certificate:
        """
        Create one certificate

        Parameters
        ----------
        auto_renew : str
            Allow Otoroshi to renew the certificate (if self signed)

        ca : str
            Certificate is a CA (read only)

        ca_ref : str
            Reference for a CA certificate in otoroshi

        chain : str
            Certificate chain of trust in PEM format

        domain : str
            Domain of the certificate (read only)

        from_ : str
            Start date of validity

        id : str
            Id of the certificate

        private_key : str
            PKCS8 private key in PEM format

        self_signed : str
            Certificate is self signed  read only)

        subject : str
            Subject of the certificate (read only)

        to : str
            End date of validity

        valid : str
            Certificate is valid (read only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Certificate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.create_cert(
            auto_renew="a string value",
            ca="a string value",
            ca_ref="a string value",
            chain="a string value",
            domain="a string value",
            from_="a string value",
            id="a string value",
            private_key="a string value",
            self_signed="a string value",
            subject="a string value",
            to="a string value",
            valid="a string value",
        )
        """
        _response = self._raw_client.create_cert(
            auto_renew=auto_renew,
            ca=ca,
            ca_ref=ca_ref,
            chain=chain,
            domain=domain,
            from_=from_,
            id=id,
            private_key=private_key,
            self_signed=self_signed,
            subject=subject,
            to=to,
            valid=valid,
            request_options=request_options,
        )
        return _response.data

    def one_cert(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Certificate:
        """
        Get one certificate by id

        Parameters
        ----------
        id : str
            The auth. config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Certificate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.one_cert(
            id="id",
        )
        """
        _response = self._raw_client.one_cert(id, request_options=request_options)
        return _response.data

    def put_cert(
        self,
        id_: str,
        *,
        auto_renew: str,
        ca: str,
        ca_ref: str,
        chain: str,
        domain: str,
        from_: str,
        id: str,
        private_key: str,
        self_signed: str,
        subject: str,
        to: str,
        valid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Certificate:
        """
        Update one certificate by id

        Parameters
        ----------
        id_ : str
            The certificate id

        auto_renew : str
            Allow Otoroshi to renew the certificate (if self signed)

        ca : str
            Certificate is a CA (read only)

        ca_ref : str
            Reference for a CA certificate in otoroshi

        chain : str
            Certificate chain of trust in PEM format

        domain : str
            Domain of the certificate (read only)

        from_ : str
            Start date of validity

        id : str
            Id of the certificate

        private_key : str
            PKCS8 private key in PEM format

        self_signed : str
            Certificate is self signed  read only)

        subject : str
            Subject of the certificate (read only)

        to : str
            End date of validity

        valid : str
            Certificate is valid (read only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Certificate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.put_cert(
            id_="id",
            auto_renew="a string value",
            ca="a string value",
            ca_ref="a string value",
            chain="a string value",
            domain="a string value",
            from_="a string value",
            id="a string value",
            private_key="a string value",
            self_signed="a string value",
            subject="a string value",
            to="a string value",
            valid="a string value",
        )
        """
        _response = self._raw_client.put_cert(
            id_,
            auto_renew=auto_renew,
            ca=ca,
            ca_ref=ca_ref,
            chain=chain,
            domain=domain,
            from_=from_,
            id=id,
            private_key=private_key,
            self_signed=self_signed,
            subject=subject,
            to=to,
            valid=valid,
            request_options=request_options,
        )
        return _response.data

    def delete_cert(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deleted:
        """
        Delete one certificate by id

        Parameters
        ----------
        id : str
            The certificate id

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
        client.certificates.delete_cert(
            id="id",
        )
        """
        _response = self._raw_client.delete_cert(id, request_options=request_options)
        return _response.data

    def patch_cert(
        self, id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> Certificate:
        """
        Update one certificate by id

        Parameters
        ----------
        id : str
            The certificate id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Certificate
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.certificates.patch_cert(
            id="id",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_cert(id, request=request, request_options=request_options)
        return _response.data


class AsyncCertificatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCertificatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCertificatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCertificatesClient
        """
        return self._raw_client

    async def all_certs(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Certificate]:
        """
        Get all certificates

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Certificate]
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
            await client.certificates.all_certs()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_certs(request_options=request_options)
        return _response.data

    async def create_cert(
        self,
        *,
        auto_renew: str,
        ca: str,
        ca_ref: str,
        chain: str,
        domain: str,
        from_: str,
        id: str,
        private_key: str,
        self_signed: str,
        subject: str,
        to: str,
        valid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Certificate:
        """
        Create one certificate

        Parameters
        ----------
        auto_renew : str
            Allow Otoroshi to renew the certificate (if self signed)

        ca : str
            Certificate is a CA (read only)

        ca_ref : str
            Reference for a CA certificate in otoroshi

        chain : str
            Certificate chain of trust in PEM format

        domain : str
            Domain of the certificate (read only)

        from_ : str
            Start date of validity

        id : str
            Id of the certificate

        private_key : str
            PKCS8 private key in PEM format

        self_signed : str
            Certificate is self signed  read only)

        subject : str
            Subject of the certificate (read only)

        to : str
            End date of validity

        valid : str
            Certificate is valid (read only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Certificate
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
            await client.certificates.create_cert(
                auto_renew="a string value",
                ca="a string value",
                ca_ref="a string value",
                chain="a string value",
                domain="a string value",
                from_="a string value",
                id="a string value",
                private_key="a string value",
                self_signed="a string value",
                subject="a string value",
                to="a string value",
                valid="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_cert(
            auto_renew=auto_renew,
            ca=ca,
            ca_ref=ca_ref,
            chain=chain,
            domain=domain,
            from_=from_,
            id=id,
            private_key=private_key,
            self_signed=self_signed,
            subject=subject,
            to=to,
            valid=valid,
            request_options=request_options,
        )
        return _response.data

    async def one_cert(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Certificate:
        """
        Get one certificate by id

        Parameters
        ----------
        id : str
            The auth. config id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Certificate
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
            await client.certificates.one_cert(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one_cert(id, request_options=request_options)
        return _response.data

    async def put_cert(
        self,
        id_: str,
        *,
        auto_renew: str,
        ca: str,
        ca_ref: str,
        chain: str,
        domain: str,
        from_: str,
        id: str,
        private_key: str,
        self_signed: str,
        subject: str,
        to: str,
        valid: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Certificate:
        """
        Update one certificate by id

        Parameters
        ----------
        id_ : str
            The certificate id

        auto_renew : str
            Allow Otoroshi to renew the certificate (if self signed)

        ca : str
            Certificate is a CA (read only)

        ca_ref : str
            Reference for a CA certificate in otoroshi

        chain : str
            Certificate chain of trust in PEM format

        domain : str
            Domain of the certificate (read only)

        from_ : str
            Start date of validity

        id : str
            Id of the certificate

        private_key : str
            PKCS8 private key in PEM format

        self_signed : str
            Certificate is self signed  read only)

        subject : str
            Subject of the certificate (read only)

        to : str
            End date of validity

        valid : str
            Certificate is valid (read only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Certificate
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
            await client.certificates.put_cert(
                id_="id",
                auto_renew="a string value",
                ca="a string value",
                ca_ref="a string value",
                chain="a string value",
                domain="a string value",
                from_="a string value",
                id="a string value",
                private_key="a string value",
                self_signed="a string value",
                subject="a string value",
                to="a string value",
                valid="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_cert(
            id_,
            auto_renew=auto_renew,
            ca=ca,
            ca_ref=ca_ref,
            chain=chain,
            domain=domain,
            from_=from_,
            id=id,
            private_key=private_key,
            self_signed=self_signed,
            subject=subject,
            to=to,
            valid=valid,
            request_options=request_options,
        )
        return _response.data

    async def delete_cert(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deleted:
        """
        Delete one certificate by id

        Parameters
        ----------
        id : str
            The certificate id

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
            await client.certificates.delete_cert(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_cert(id, request_options=request_options)
        return _response.data

    async def patch_cert(
        self, id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> Certificate:
        """
        Update one certificate by id

        Parameters
        ----------
        id : str
            The certificate id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Certificate
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
            await client.certificates.patch_cert(
                id="id",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_cert(id, request=request, request_options=request_options)
        return _response.data
