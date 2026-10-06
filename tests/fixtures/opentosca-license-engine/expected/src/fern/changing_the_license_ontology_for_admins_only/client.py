

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.conditions import Conditions
from ..types.license_types import LicenseTypes
from ..types.limitations import Limitations
from ..types.permissions import Permissions
from .raw_client import (
    AsyncRawChangingTheLicenseOntologyForAdminsOnlyClient,
    RawChangingTheLicenseOntologyForAdminsOnlyClient,
)


OMIT = typing.cast(typing.Any, ...)


class ChangingTheLicenseOntologyForAdminsOnlyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawChangingTheLicenseOntologyForAdminsOnlyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawChangingTheLicenseOntologyForAdminsOnlyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawChangingTheLicenseOntologyForAdminsOnlyClient
        """
        return self._raw_client

    def add_license(
        self,
        *,
        id: str,
        name: str,
        url: typing.Optional[str] = OMIT,
        type: typing.Optional[LicenseTypes] = OMIT,
        conditions: typing.Optional[typing.Sequence[Conditions]] = OMIT,
        permissions: typing.Optional[typing.Sequence[Permissions]] = OMIT,
        limitations: typing.Optional[typing.Sequence[Limitations]] = OMIT,
        compatibility: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Adds a license to the ontology. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        id : str

        name : str

        url : typing.Optional[str]

        type : typing.Optional[LicenseTypes]

        conditions : typing.Optional[typing.Sequence[Conditions]]

        permissions : typing.Optional[typing.Sequence[Permissions]]

        limitations : typing.Optional[typing.Sequence[Limitations]]

        compatibility : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.changing_the_license_ontology_for_admins_only.add_license(
            id="id",
            name="name",
        )
        """
        _response = self._raw_client.add_license(
            id=id,
            name=name,
            url=url,
            type=type,
            conditions=conditions,
            permissions=permissions,
            limitations=limitations,
            compatibility=compatibility,
            request_options=request_options,
        )
        return _response.data

    def update_license(
        self,
        license_id: str,
        *,
        id: str,
        name: str,
        url: typing.Optional[str] = OMIT,
        type: typing.Optional[LicenseTypes] = OMIT,
        conditions: typing.Optional[typing.Sequence[Conditions]] = OMIT,
        permissions: typing.Optional[typing.Sequence[Permissions]] = OMIT,
        limitations: typing.Optional[typing.Sequence[Limitations]] = OMIT,
        compatibility: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Changes the properties of a certain license. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        license_id : str

        id : str

        name : str

        url : typing.Optional[str]

        type : typing.Optional[LicenseTypes]

        conditions : typing.Optional[typing.Sequence[Conditions]]

        permissions : typing.Optional[typing.Sequence[Permissions]]

        limitations : typing.Optional[typing.Sequence[Limitations]]

        compatibility : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.changing_the_license_ontology_for_admins_only.update_license(
            license_id="license_id",
            id="id",
            name="name",
        )
        """
        _response = self._raw_client.update_license(
            license_id,
            id=id,
            name=name,
            url=url,
            type=type,
            conditions=conditions,
            permissions=permissions,
            limitations=limitations,
            compatibility=compatibility,
            request_options=request_options,
        )
        return _response.data

    def delete_license(self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Deletes a certain license. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        license_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.changing_the_license_ontology_for_admins_only.delete_license(
            license_id="license_id",
        )
        """
        _response = self._raw_client.delete_license(license_id, request_options=request_options)
        return _response.data


class AsyncChangingTheLicenseOntologyForAdminsOnlyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawChangingTheLicenseOntologyForAdminsOnlyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawChangingTheLicenseOntologyForAdminsOnlyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawChangingTheLicenseOntologyForAdminsOnlyClient
        """
        return self._raw_client

    async def add_license(
        self,
        *,
        id: str,
        name: str,
        url: typing.Optional[str] = OMIT,
        type: typing.Optional[LicenseTypes] = OMIT,
        conditions: typing.Optional[typing.Sequence[Conditions]] = OMIT,
        permissions: typing.Optional[typing.Sequence[Permissions]] = OMIT,
        limitations: typing.Optional[typing.Sequence[Limitations]] = OMIT,
        compatibility: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Adds a license to the ontology. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        id : str

        name : str

        url : typing.Optional[str]

        type : typing.Optional[LicenseTypes]

        conditions : typing.Optional[typing.Sequence[Conditions]]

        permissions : typing.Optional[typing.Sequence[Permissions]]

        limitations : typing.Optional[typing.Sequence[Limitations]]

        compatibility : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.changing_the_license_ontology_for_admins_only.add_license(
                id="id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_license(
            id=id,
            name=name,
            url=url,
            type=type,
            conditions=conditions,
            permissions=permissions,
            limitations=limitations,
            compatibility=compatibility,
            request_options=request_options,
        )
        return _response.data

    async def update_license(
        self,
        license_id: str,
        *,
        id: str,
        name: str,
        url: typing.Optional[str] = OMIT,
        type: typing.Optional[LicenseTypes] = OMIT,
        conditions: typing.Optional[typing.Sequence[Conditions]] = OMIT,
        permissions: typing.Optional[typing.Sequence[Permissions]] = OMIT,
        limitations: typing.Optional[typing.Sequence[Limitations]] = OMIT,
        compatibility: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Changes the properties of a certain license. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        license_id : str

        id : str

        name : str

        url : typing.Optional[str]

        type : typing.Optional[LicenseTypes]

        conditions : typing.Optional[typing.Sequence[Conditions]]

        permissions : typing.Optional[typing.Sequence[Permissions]]

        limitations : typing.Optional[typing.Sequence[Limitations]]

        compatibility : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.changing_the_license_ontology_for_admins_only.update_license(
                license_id="license_id",
                id="id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_license(
            license_id,
            id=id,
            name=name,
            url=url,
            type=type,
            conditions=conditions,
            permissions=permissions,
            limitations=limitations,
            compatibility=compatibility,
            request_options=request_options,
        )
        return _response.data

    async def delete_license(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Deletes a certain license. Only for admins.

        **work in progress, not working yet**

        Parameters
        ----------
        license_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.changing_the_license_ontology_for_admins_only.delete_license(
                license_id="license_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_license(license_id, request_options=request_options)
        return _response.data
