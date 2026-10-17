

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_project_addons_response_output import ListProjectAddonsResponseOutput
from .raw_client import AsyncRawBillingClient, RawBillingClient
from .types.apply_project_addon_body_addon_type import ApplyProjectAddonBodyAddonType
from .types.apply_project_addon_body_addon_variant import ApplyProjectAddonBodyAddonVariant
from .types.v1remove_project_addon_request_addon_variant import V1RemoveProjectAddonRequestAddonVariant


OMIT = typing.cast(typing.Any, ...)


class BillingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBillingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBillingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBillingClient
        """
        return self._raw_client

    def v1list_project_addons(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListProjectAddonsResponseOutput:
        """
        Returns the billing addons that are currently applied, including the active compute instance size, and lists every addon option that can be provisioned with pricing metadata.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProjectAddonsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.v1list_project_addons(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_project_addons(ref, request_options=request_options)
        return _response.data

    def v1apply_project_addon(
        self,
        ref: str,
        *,
        addon_variant: ApplyProjectAddonBodyAddonVariant,
        addon_type: ApplyProjectAddonBodyAddonType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Selects an addon variant, for example scaling the project’s compute instance up or down, and applies it to the project.

        Parameters
        ----------
        ref : str
            Project ref

        addon_variant : ApplyProjectAddonBodyAddonVariant

        addon_type : ApplyProjectAddonBodyAddonType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.billing import (
            ApplyProjectAddonBodyAddonType,
            ApplyProjectAddonBodyAddonVariantTwo,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.v1apply_project_addon(
            ref="abcdefghijklmnopqrst",
            addon_variant=ApplyProjectAddonBodyAddonVariantTwo.PITR7,
            addon_type=ApplyProjectAddonBodyAddonType.PITR,
        )
        """
        _response = self._raw_client.v1apply_project_addon(
            ref, addon_variant=addon_variant, addon_type=addon_type, request_options=request_options
        )
        return _response.data

    def v1remove_project_addon(
        self,
        ref: str,
        addon_variant: V1RemoveProjectAddonRequestAddonVariant,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Disables the selected addon variant, including rolling the compute instance back to its previous size.

        Parameters
        ----------
        ref : str
            Project ref

        addon_variant : V1RemoveProjectAddonRequestAddonVariant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.billing import V1RemoveProjectAddonRequestAddonVariantZero

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.billing.v1remove_project_addon(
            ref="abcdefghijklmnopqrst",
            addon_variant=V1RemoveProjectAddonRequestAddonVariantZero.CI_MICRO,
        )
        """
        _response = self._raw_client.v1remove_project_addon(ref, addon_variant, request_options=request_options)
        return _response.data


class AsyncBillingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBillingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBillingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBillingClient
        """
        return self._raw_client

    async def v1list_project_addons(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListProjectAddonsResponseOutput:
        """
        Returns the billing addons that are currently applied, including the active compute instance size, and lists every addon option that can be provisioned with pricing metadata.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProjectAddonsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.v1list_project_addons(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_project_addons(ref, request_options=request_options)
        return _response.data

    async def v1apply_project_addon(
        self,
        ref: str,
        *,
        addon_variant: ApplyProjectAddonBodyAddonVariant,
        addon_type: ApplyProjectAddonBodyAddonType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Selects an addon variant, for example scaling the project’s compute instance up or down, and applies it to the project.

        Parameters
        ----------
        ref : str
            Project ref

        addon_variant : ApplyProjectAddonBodyAddonVariant

        addon_type : ApplyProjectAddonBodyAddonType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.billing import (
            ApplyProjectAddonBodyAddonType,
            ApplyProjectAddonBodyAddonVariantTwo,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.v1apply_project_addon(
                ref="abcdefghijklmnopqrst",
                addon_variant=ApplyProjectAddonBodyAddonVariantTwo.PITR7,
                addon_type=ApplyProjectAddonBodyAddonType.PITR,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1apply_project_addon(
            ref, addon_variant=addon_variant, addon_type=addon_type, request_options=request_options
        )
        return _response.data

    async def v1remove_project_addon(
        self,
        ref: str,
        addon_variant: V1RemoveProjectAddonRequestAddonVariant,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Disables the selected addon variant, including rolling the compute instance back to its previous size.

        Parameters
        ----------
        ref : str
            Project ref

        addon_variant : V1RemoveProjectAddonRequestAddonVariant

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.billing import V1RemoveProjectAddonRequestAddonVariantZero

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.billing.v1remove_project_addon(
                ref="abcdefghijklmnopqrst",
                addon_variant=V1RemoveProjectAddonRequestAddonVariantZero.CI_MICRO,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1remove_project_addon(ref, addon_variant, request_options=request_options)
        return _response.data
