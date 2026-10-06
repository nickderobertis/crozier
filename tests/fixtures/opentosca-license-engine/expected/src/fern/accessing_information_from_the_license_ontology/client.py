

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.license import License
from .raw_client import (
    AsyncRawAccessingInformationFromTheLicenseOntologyClient,
    RawAccessingInformationFromTheLicenseOntologyClient,
)


OMIT = typing.cast(typing.Any, ...)


class AccessingInformationFromTheLicenseOntologyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccessingInformationFromTheLicenseOntologyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccessingInformationFromTheLicenseOntologyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccessingInformationFromTheLicenseOntologyClient
        """
        return self._raw_client

    def get_all_licenses(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[License]:
        """
        Returns all available software licenses as License-Objects

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[License]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.accessing_information_from_the_license_ontology.get_all_licenses()
        """
        _response = self._raw_client.get_all_licenses(request_options=request_options)
        return _response.data

    def get_license(self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Returns a certain license as a License-Object

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
        client.accessing_information_from_the_license_ontology.get_license(
            license_id="license_id",
        )
        """
        _response = self._raw_client.get_license(license_id, request_options=request_options)
        return _response.data

    def get_license_conditions(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns the conditions of a certain license.

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
        client.accessing_information_from_the_license_ontology.get_license_conditions(
            license_id="license_id",
        )
        """
        _response = self._raw_client.get_license_conditions(license_id, request_options=request_options)
        return _response.data

    def get_license_limitations(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns the limitations of a certain license.

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
        client.accessing_information_from_the_license_ontology.get_license_limitations(
            license_id="license_id",
        )
        """
        _response = self._raw_client.get_license_limitations(license_id, request_options=request_options)
        return _response.data

    def get_license_permissions(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns the permissions of a certain license.

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
        client.accessing_information_from_the_license_ontology.get_license_permissions(
            license_id="license_id",
        )
        """
        _response = self._raw_client.get_license_permissions(license_id, request_options=request_options)
        return _response.data

    def get_license_type(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns the type of a certain license.

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
        client.accessing_information_from_the_license_ontology.get_license_type(
            license_id="license_id",
        )
        """
        _response = self._raw_client.get_license_type(license_id, request_options=request_options)
        return _response.data

    def check_osi_popularity(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns TRUE if the license is among the popular licenses according to the Open Software Initiative.

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
        client.accessing_information_from_the_license_ontology.check_osi_popularity(
            license_id="license_id",
        )
        """
        _response = self._raw_client.check_osi_popularity(license_id, request_options=request_options)
        return _response.data

    def return_osi_popular_licenses(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Returns all popular licenses according to the Open Software Initiative.

        Parameters
        ----------
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
        client.accessing_information_from_the_license_ontology.return_osi_popular_licenses()
        """
        _response = self._raw_client.return_osi_popular_licenses(request_options=request_options)
        return _response.data

    def return_licenses_for_type(
        self, license_type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns a list of licenses of a certain type.

        Parameters
        ----------
        license_type : str

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
        client.accessing_information_from_the_license_ontology.return_licenses_for_type(
            license_type="license_type",
        )
        """
        _response = self._raw_client.return_licenses_for_type(license_type, request_options=request_options)
        return _response.data

    def check_license(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns which licenses are compatible with a certain license.

        **work in progress, not working yet**

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.accessing_information_from_the_license_ontology.check_license(
            request=["string"],
        )
        """
        _response = self._raw_client.check_license(request=request, request_options=request_options)
        return _response.data


class AsyncAccessingInformationFromTheLicenseOntologyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccessingInformationFromTheLicenseOntologyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccessingInformationFromTheLicenseOntologyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccessingInformationFromTheLicenseOntologyClient
        """
        return self._raw_client

    async def get_all_licenses(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[License]:
        """
        Returns all available software licenses as License-Objects

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[License]
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
            await client.accessing_information_from_the_license_ontology.get_all_licenses()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_licenses(request_options=request_options)
        return _response.data

    async def get_license(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns a certain license as a License-Object

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
            await client.accessing_information_from_the_license_ontology.get_license(
                license_id="license_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_license(license_id, request_options=request_options)
        return _response.data

    async def get_license_conditions(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns the conditions of a certain license.

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
            await client.accessing_information_from_the_license_ontology.get_license_conditions(
                license_id="license_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_license_conditions(license_id, request_options=request_options)
        return _response.data

    async def get_license_limitations(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns the limitations of a certain license.

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
            await client.accessing_information_from_the_license_ontology.get_license_limitations(
                license_id="license_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_license_limitations(license_id, request_options=request_options)
        return _response.data

    async def get_license_permissions(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns the permissions of a certain license.

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
            await client.accessing_information_from_the_license_ontology.get_license_permissions(
                license_id="license_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_license_permissions(license_id, request_options=request_options)
        return _response.data

    async def get_license_type(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns the type of a certain license.

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
            await client.accessing_information_from_the_license_ontology.get_license_type(
                license_id="license_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_license_type(license_id, request_options=request_options)
        return _response.data

    async def check_osi_popularity(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns TRUE if the license is among the popular licenses according to the Open Software Initiative.

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
            await client.accessing_information_from_the_license_ontology.check_osi_popularity(
                license_id="license_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_osi_popularity(license_id, request_options=request_options)
        return _response.data

    async def return_osi_popular_licenses(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns all popular licenses according to the Open Software Initiative.

        Parameters
        ----------
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
            await client.accessing_information_from_the_license_ontology.return_osi_popular_licenses()


        asyncio.run(main())
        """
        _response = await self._raw_client.return_osi_popular_licenses(request_options=request_options)
        return _response.data

    async def return_licenses_for_type(
        self, license_type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Returns a list of licenses of a certain type.

        Parameters
        ----------
        license_type : str

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
            await client.accessing_information_from_the_license_ontology.return_licenses_for_type(
                license_type="license_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_licenses_for_type(license_type, request_options=request_options)
        return _response.data

    async def check_license(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns which licenses are compatible with a certain license.

        **work in progress, not working yet**

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
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
            await client.accessing_information_from_the_license_ontology.check_license(
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_license(request=request, request_options=request_options)
        return _response.data
