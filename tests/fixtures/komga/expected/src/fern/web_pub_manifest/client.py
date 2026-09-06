

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.r2device import R2Device
from ..types.r2locator import R2Locator
from ..types.r2positions import R2Positions
from ..types.r2progression import R2Progression
from ..types.wp_publication_dto import WpPublicationDto
from .raw_client import AsyncRawWebPubManifestClient, RawWebPubManifestClient


OMIT = typing.cast(typing.Any, ...)


class WebPubManifestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebPubManifestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebPubManifestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebPubManifestClient
        """
        return self._raw_client

    def get_book_web_pub_manifest(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WpPublicationDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WpPublicationDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.web_pub_manifest.get_book_web_pub_manifest(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_web_pub_manifest(book_id, request_options=request_options)
        return _response.data

    def get_book_web_pub_manifest_divina(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WpPublicationDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WpPublicationDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.web_pub_manifest.get_book_web_pub_manifest_divina(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_web_pub_manifest_divina(book_id, request_options=request_options)
        return _response.data

    def get_book_web_pub_manifest_epub(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WpPublicationDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WpPublicationDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.web_pub_manifest.get_book_web_pub_manifest_epub(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_web_pub_manifest_epub(book_id, request_options=request_options)
        return _response.data

    def get_book_web_pub_manifest_pdf(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WpPublicationDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WpPublicationDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.web_pub_manifest.get_book_web_pub_manifest_pdf(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_web_pub_manifest_pdf(book_id, request_options=request_options)
        return _response.data

    def get_book_positions(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> R2Positions:
        """
        The Positions API is a proposed standard for OPDS 2 and Readium. It is used by the Epub Reader.

        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        R2Positions
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.web_pub_manifest.get_book_positions(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_positions(book_id, request_options=request_options)
        return _response.data

    def get_book_progression(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> R2Progression:
        """
        The Progression API is a proposed standard for OPDS 2 and Readium. It is used by the Epub Reader.

        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        R2Progression
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.web_pub_manifest.get_book_progression(
            book_id="bookId",
        )
        """
        _response = self._raw_client.get_book_progression(book_id, request_options=request_options)
        return _response.data

    def update_book_progression(
        self,
        book_id: str,
        *,
        device: R2Device,
        locator: R2Locator,
        modified: dt.datetime,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The Progression API is a proposed standard for OPDS 2 and Readium. It is used by the Epub Reader.

        Parameters
        ----------
        book_id : str

        device : R2Device

        locator : R2Locator

        modified : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi, R2Device, R2Locator

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.web_pub_manifest.update_book_progression(
            book_id="bookId",
            device=R2Device(
                id="id",
                name="name",
            ),
            locator=R2Locator(
                href="href",
                type="type",
            ),
            modified=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.update_book_progression(
            book_id, device=device, locator=locator, modified=modified, request_options=request_options
        )
        return _response.data

    def get_book_epub_resource(
        self, book_id: str, resource: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Return a resource from within an Epub book.

        Parameters
        ----------
        book_id : str

        resource : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.web_pub_manifest.get_book_epub_resource(
            book_id="bookId",
            resource="resource",
        )
        """
        _response = self._raw_client.get_book_epub_resource(book_id, resource, request_options=request_options)
        return _response.data


class AsyncWebPubManifestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebPubManifestClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebPubManifestClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebPubManifestClient
        """
        return self._raw_client

    async def get_book_web_pub_manifest(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WpPublicationDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WpPublicationDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.web_pub_manifest.get_book_web_pub_manifest(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_web_pub_manifest(book_id, request_options=request_options)
        return _response.data

    async def get_book_web_pub_manifest_divina(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WpPublicationDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WpPublicationDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.web_pub_manifest.get_book_web_pub_manifest_divina(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_web_pub_manifest_divina(book_id, request_options=request_options)
        return _response.data

    async def get_book_web_pub_manifest_epub(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WpPublicationDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WpPublicationDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.web_pub_manifest.get_book_web_pub_manifest_epub(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_web_pub_manifest_epub(book_id, request_options=request_options)
        return _response.data

    async def get_book_web_pub_manifest_pdf(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WpPublicationDto:
        """
        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WpPublicationDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.web_pub_manifest.get_book_web_pub_manifest_pdf(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_web_pub_manifest_pdf(book_id, request_options=request_options)
        return _response.data

    async def get_book_positions(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> R2Positions:
        """
        The Positions API is a proposed standard for OPDS 2 and Readium. It is used by the Epub Reader.

        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        R2Positions
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.web_pub_manifest.get_book_positions(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_positions(book_id, request_options=request_options)
        return _response.data

    async def get_book_progression(
        self, book_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> R2Progression:
        """
        The Progression API is a proposed standard for OPDS 2 and Readium. It is used by the Epub Reader.

        Parameters
        ----------
        book_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        R2Progression
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.web_pub_manifest.get_book_progression(
                book_id="bookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_progression(book_id, request_options=request_options)
        return _response.data

    async def update_book_progression(
        self,
        book_id: str,
        *,
        device: R2Device,
        locator: R2Locator,
        modified: dt.datetime,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The Progression API is a proposed standard for OPDS 2 and Readium. It is used by the Epub Reader.

        Parameters
        ----------
        book_id : str

        device : R2Device

        locator : R2Locator

        modified : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, R2Device, R2Locator

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.web_pub_manifest.update_book_progression(
                book_id="bookId",
                device=R2Device(
                    id="id",
                    name="name",
                ),
                locator=R2Locator(
                    href="href",
                    type="type",
                ),
                modified=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_book_progression(
            book_id, device=device, locator=locator, modified=modified, request_options=request_options
        )
        return _response.data

    async def get_book_epub_resource(
        self, book_id: str, resource: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Return a resource from within an Epub book.

        Parameters
        ----------
        book_id : str

        resource : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.web_pub_manifest.get_book_epub_resource(
                book_id="bookId",
                resource="resource",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_book_epub_resource(book_id, resource, request_options=request_options)
        return _response.data
