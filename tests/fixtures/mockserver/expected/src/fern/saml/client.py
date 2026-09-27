

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.expectation import Expectation
from .raw_client import AsyncRawSamlClient, RawSamlClient


OMIT = typing.cast(typing.Any, ...)


class SamlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSamlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSamlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSamlClient
        """
        return self._raw_client

    def mock_saml_provider(
        self,
        *,
        idp_entity_id: typing.Optional[str] = OMIT,
        sp_entity_id: typing.Optional[str] = OMIT,
        signing_certificate_pem: typing.Optional[str] = OMIT,
        signing_private_key_pem: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Expectation]:
        """
        Generates a set of expectations that emulate a SAML 2.0 identity provider (metadata, single sign-on and single logout endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        idp_entity_id : typing.Optional[str]
            identity provider entity ID advertised in metadata

        sp_entity_id : typing.Optional[str]
            service provider entity ID the assertions are issued for

        signing_certificate_pem : typing.Optional[str]
            PEM-encoded X.509 certificate used to verify signed assertions

        signing_private_key_pem : typing.Optional[str]
            PEM-encoded private key used to sign assertions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            SAML provider expectations created

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.saml.mock_saml_provider(
            idp_entity_id="http://localhost:1080/saml/idp",
            sp_entity_id="urn:my-app:sp",
        )
        """
        _response = self._raw_client.mock_saml_provider(
            idp_entity_id=idp_entity_id,
            sp_entity_id=sp_entity_id,
            signing_certificate_pem=signing_certificate_pem,
            signing_private_key_pem=signing_private_key_pem,
            request_options=request_options,
        )
        return _response.data


class AsyncSamlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSamlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSamlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSamlClient
        """
        return self._raw_client

    async def mock_saml_provider(
        self,
        *,
        idp_entity_id: typing.Optional[str] = OMIT,
        sp_entity_id: typing.Optional[str] = OMIT,
        signing_certificate_pem: typing.Optional[str] = OMIT,
        signing_private_key_pem: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Expectation]:
        """
        Generates a set of expectations that emulate a SAML 2.0 identity provider (metadata, single sign-on and single logout endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        idp_entity_id : typing.Optional[str]
            identity provider entity ID advertised in metadata

        sp_entity_id : typing.Optional[str]
            service provider entity ID the assertions are issued for

        signing_certificate_pem : typing.Optional[str]
            PEM-encoded X.509 certificate used to verify signed assertions

        signing_private_key_pem : typing.Optional[str]
            PEM-encoded private key used to sign assertions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            SAML provider expectations created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.saml.mock_saml_provider(
                idp_entity_id="http://localhost:1080/saml/idp",
                sp_entity_id="urn:my-app:sp",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mock_saml_provider(
            idp_entity_id=idp_entity_id,
            sp_entity_id=sp_entity_id,
            signing_certificate_pem=signing_certificate_pem,
            signing_private_key_pem=signing_private_key_pem,
            request_options=request_options,
        )
        return _response.data
