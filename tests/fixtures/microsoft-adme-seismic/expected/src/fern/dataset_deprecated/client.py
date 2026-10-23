

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDatasetDeprecatedClient, RawDatasetDeprecatedClient


OMIT = typing.cast(typing.Any, ...)


class DatasetDeprecatedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatasetDeprecatedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatasetDeprecatedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatasetDeprecatedClient
        """
        return self._raw_client

    def dataset_sizes(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        datasets: typing.Sequence[str],
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[float]:
        """
        <ul>
        <li>Return a list with the sizes of the requested datasets.</li>
        <li>The correctness is not guarantee since this API returns sizes stored by the user in the dataset manifest.</li>
        <li>This API is deprecated, please using /size endpoint to compute and retrieve the size information</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant

        subprojectid : str
            Name of the subproject.

        datasets : typing.Sequence[str]
            Array of datasets inside the subproject.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[float]
            The list of sizes of all the datasets. If the dataset does not exist, the size returns -1.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.dataset_deprecated.dataset_sizes(
            tenantid="tenantid",
            subprojectid="subprojectid",
            datasets=["a/b/c/dsx01", "a/b/c/dsx02"],
        )
        """
        _response = self._raw_client.dataset_sizes(
            tenantid,
            subprojectid,
            datasets=datasets,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data


class AsyncDatasetDeprecatedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatasetDeprecatedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatasetDeprecatedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatasetDeprecatedClient
        """
        return self._raw_client

    async def dataset_sizes(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        datasets: typing.Sequence[str],
        impersonation_token_context: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[float]:
        """
        <ul>
        <li>Return a list with the sizes of the requested datasets.</li>
        <li>The correctness is not guarantee since this API returns sizes stored by the user in the dataset manifest.</li>
        <li>This API is deprecated, please using /size endpoint to compute and retrieve the size information</li>
        <li>Required roles: subproject.admin, subproject.viewer</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant

        subprojectid : str
            Name of the subproject.

        datasets : typing.Sequence[str]
            Array of datasets inside the subproject.

        impersonation_token_context : typing.Optional[str]
            The impersonation token context (required only with impersonation token credentials)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[float]
            The list of sizes of all the datasets. If the dataset does not exist, the size returns -1.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.dataset_deprecated.dataset_sizes(
                tenantid="tenantid",
                subprojectid="subprojectid",
                datasets=["a/b/c/dsx01", "a/b/c/dsx02"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.dataset_sizes(
            tenantid,
            subprojectid,
            datasets=datasets,
            impersonation_token_context=impersonation_token_context,
            request_options=request_options,
        )
        return _response.data
