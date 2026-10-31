

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPropertiesClient, RawPropertiesClient
from .types.properties_archive_response import PropertiesArchiveResponse
from .types.properties_by_id_response import PropertiesByIdResponse
from .types.properties_complete_image_upload_response import PropertiesCompleteImageUploadResponse
from .types.properties_create_image_upload_url_request_content_type import (
    PropertiesCreateImageUploadUrlRequestContentType,
)
from .types.properties_create_image_upload_url_response import PropertiesCreateImageUploadUrlResponse
from .types.properties_create_request_address import PropertiesCreateRequestAddress
from .types.properties_create_request_property_type import PropertiesCreateRequestPropertyType
from .types.properties_create_request_units_item import PropertiesCreateRequestUnitsItem
from .types.properties_create_response import PropertiesCreateResponse
from .types.properties_delete_image_response import PropertiesDeleteImageResponse
from .types.properties_delete_response import PropertiesDeleteResponse
from .types.properties_inactivate_response import PropertiesInactivateResponse
from .types.properties_list_response import PropertiesListResponse
from .types.properties_reactivate_response import PropertiesReactivateResponse
from .types.properties_update_notes_response import PropertiesUpdateNotesResponse
from .types.properties_update_request_address import PropertiesUpdateRequestAddress
from .types.properties_update_request_property_type import PropertiesUpdateRequestPropertyType
from .types.properties_update_request_units_item import PropertiesUpdateRequestUnitsItem
from .types.properties_update_response import PropertiesUpdateResponse


OMIT = typing.cast(typing.Any, ...)


class PropertiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPropertiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPropertiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPropertiesClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> PropertiesListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        name: str,
        property_type: PropertiesCreateRequestPropertyType,
        address: PropertiesCreateRequestAddress,
        unit_count: int,
        tag_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        contact_name: typing.Optional[str] = OMIT,
        contact_email: typing.Optional[str] = OMIT,
        contact_phone: typing.Optional[str] = OMIT,
        contact_address: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        units: typing.Optional[typing.Sequence[PropertiesCreateRequestUnitsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PropertiesCreateResponse:
        """
        Parameters
        ----------
        name : str

        property_type : PropertiesCreateRequestPropertyType

        address : PropertiesCreateRequestAddress

        unit_count : int

        tag_ids : typing.Optional[typing.Sequence[int]]

        contact_name : typing.Optional[str]

        contact_email : typing.Optional[str]

        contact_phone : typing.Optional[str]

        contact_address : typing.Optional[str]

        notes : typing.Optional[str]

        units : typing.Optional[typing.Sequence[PropertiesCreateRequestUnitsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesCreateResponse
            Successful response

        Examples
        --------
        from fern.properties import PropertiesCreateRequestAddress

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.create(
            name="name",
            property_type="Apartment",
            address=PropertiesCreateRequestAddress(
                line1="line1",
                city="city",
                region="region",
                postal_code="postalCode",
            ),
            unit_count=1,
        )
        """
        _response = self._raw_client.create(
            name=name,
            property_type=property_type,
            address=address,
            unit_count=unit_count,
            tag_ids=tag_ids,
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            contact_address=contact_address,
            notes=notes,
            units=units,
            request_options=request_options,
        )
        return _response.data

    def byid(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> PropertiesByIdResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesByIdResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.byid(
            id=1,
        )
        """
        _response = self._raw_client.byid(id, request_options=request_options)
        return _response.data

    def update(
        self,
        id: int,
        *,
        name: str,
        property_type: PropertiesUpdateRequestPropertyType,
        address: PropertiesUpdateRequestAddress,
        unit_count: int,
        tag_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        contact_name: typing.Optional[str] = OMIT,
        contact_email: typing.Optional[str] = OMIT,
        contact_phone: typing.Optional[str] = OMIT,
        contact_address: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        units: typing.Optional[typing.Sequence[PropertiesUpdateRequestUnitsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PropertiesUpdateResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        property_type : PropertiesUpdateRequestPropertyType

        address : PropertiesUpdateRequestAddress

        unit_count : int

        tag_ids : typing.Optional[typing.Sequence[int]]

        contact_name : typing.Optional[str]

        contact_email : typing.Optional[str]

        contact_phone : typing.Optional[str]

        contact_address : typing.Optional[str]

        notes : typing.Optional[str]

        units : typing.Optional[typing.Sequence[PropertiesUpdateRequestUnitsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesUpdateResponse
            Successful response

        Examples
        --------
        from fern.properties import PropertiesUpdateRequestAddress

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.update(
            id=1,
            name="name",
            property_type="Apartment",
            address=PropertiesUpdateRequestAddress(
                line1="line1",
                city="city",
                region="region",
                postal_code="postalCode",
            ),
            unit_count=1,
        )
        """
        _response = self._raw_client.update(
            id,
            name=name,
            property_type=property_type,
            address=address,
            unit_count=unit_count,
            tag_ids=tag_ids,
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            contact_address=contact_address,
            notes=notes,
            units=units,
            request_options=request_options,
        )
        return _response.data

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> PropertiesDeleteResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.delete(
            id=1,
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def createimageuploadurl(
        self,
        id: int,
        *,
        content_type: PropertiesCreateImageUploadUrlRequestContentType,
        file_size: int,
        file_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PropertiesCreateImageUploadUrlResponse:
        """
        Parameters
        ----------
        id : int

        content_type : PropertiesCreateImageUploadUrlRequestContentType

        file_size : int

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesCreateImageUploadUrlResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.createimageuploadurl(
            id=1,
            content_type="image/jpeg",
            file_size=1,
            file_name="fileName",
        )
        """
        _response = self._raw_client.createimageuploadurl(
            id, content_type=content_type, file_size=file_size, file_name=file_name, request_options=request_options
        )
        return _response.data

    def completeimageupload(
        self, id: int, *, object_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesCompleteImageUploadResponse:
        """
        Parameters
        ----------
        id : int

        object_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesCompleteImageUploadResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.completeimageupload(
            id=1,
            object_key="objectKey",
        )
        """
        _response = self._raw_client.completeimageupload(id, object_key=object_key, request_options=request_options)
        return _response.data

    def deleteimage(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesDeleteImageResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesDeleteImageResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.deleteimage(
            id=1,
        )
        """
        _response = self._raw_client.deleteimage(id, request_options=request_options)
        return _response.data

    def archive(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> PropertiesArchiveResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesArchiveResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.archive(
            id=1,
        )
        """
        _response = self._raw_client.archive(id, request_options=request_options)
        return _response.data

    def inactivate(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesInactivateResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesInactivateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.inactivate(
            id=1,
        )
        """
        _response = self._raw_client.inactivate(id, request_options=request_options)
        return _response.data

    def reactivate(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesReactivateResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesReactivateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.reactivate(
            id=1,
        )
        """
        _response = self._raw_client.reactivate(id, request_options=request_options)
        return _response.data

    def updatenotes(
        self, id: int, *, notes: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesUpdateNotesResponse:
        """
        Parameters
        ----------
        id : int

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesUpdateNotesResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.properties.updatenotes(
            id=1,
        )
        """
        _response = self._raw_client.updatenotes(id, notes=notes, request_options=request_options)
        return _response.data


class AsyncPropertiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPropertiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPropertiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPropertiesClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> PropertiesListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        name: str,
        property_type: PropertiesCreateRequestPropertyType,
        address: PropertiesCreateRequestAddress,
        unit_count: int,
        tag_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        contact_name: typing.Optional[str] = OMIT,
        contact_email: typing.Optional[str] = OMIT,
        contact_phone: typing.Optional[str] = OMIT,
        contact_address: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        units: typing.Optional[typing.Sequence[PropertiesCreateRequestUnitsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PropertiesCreateResponse:
        """
        Parameters
        ----------
        name : str

        property_type : PropertiesCreateRequestPropertyType

        address : PropertiesCreateRequestAddress

        unit_count : int

        tag_ids : typing.Optional[typing.Sequence[int]]

        contact_name : typing.Optional[str]

        contact_email : typing.Optional[str]

        contact_phone : typing.Optional[str]

        contact_address : typing.Optional[str]

        notes : typing.Optional[str]

        units : typing.Optional[typing.Sequence[PropertiesCreateRequestUnitsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesCreateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.properties import PropertiesCreateRequestAddress

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.create(
                name="name",
                property_type="Apartment",
                address=PropertiesCreateRequestAddress(
                    line1="line1",
                    city="city",
                    region="region",
                    postal_code="postalCode",
                ),
                unit_count=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            name=name,
            property_type=property_type,
            address=address,
            unit_count=unit_count,
            tag_ids=tag_ids,
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            contact_address=contact_address,
            notes=notes,
            units=units,
            request_options=request_options,
        )
        return _response.data

    async def byid(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> PropertiesByIdResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesByIdResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.byid(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.byid(id, request_options=request_options)
        return _response.data

    async def update(
        self,
        id: int,
        *,
        name: str,
        property_type: PropertiesUpdateRequestPropertyType,
        address: PropertiesUpdateRequestAddress,
        unit_count: int,
        tag_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        contact_name: typing.Optional[str] = OMIT,
        contact_email: typing.Optional[str] = OMIT,
        contact_phone: typing.Optional[str] = OMIT,
        contact_address: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        units: typing.Optional[typing.Sequence[PropertiesUpdateRequestUnitsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PropertiesUpdateResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        property_type : PropertiesUpdateRequestPropertyType

        address : PropertiesUpdateRequestAddress

        unit_count : int

        tag_ids : typing.Optional[typing.Sequence[int]]

        contact_name : typing.Optional[str]

        contact_email : typing.Optional[str]

        contact_phone : typing.Optional[str]

        contact_address : typing.Optional[str]

        notes : typing.Optional[str]

        units : typing.Optional[typing.Sequence[PropertiesUpdateRequestUnitsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesUpdateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.properties import PropertiesUpdateRequestAddress

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.update(
                id=1,
                name="name",
                property_type="Apartment",
                address=PropertiesUpdateRequestAddress(
                    line1="line1",
                    city="city",
                    region="region",
                    postal_code="postalCode",
                ),
                unit_count=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id,
            name=name,
            property_type=property_type,
            address=address,
            unit_count=unit_count,
            tag_ids=tag_ids,
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            contact_address=contact_address,
            notes=notes,
            units=units,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesDeleteResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def createimageuploadurl(
        self,
        id: int,
        *,
        content_type: PropertiesCreateImageUploadUrlRequestContentType,
        file_size: int,
        file_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PropertiesCreateImageUploadUrlResponse:
        """
        Parameters
        ----------
        id : int

        content_type : PropertiesCreateImageUploadUrlRequestContentType

        file_size : int

        file_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesCreateImageUploadUrlResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.createimageuploadurl(
                id=1,
                content_type="image/jpeg",
                file_size=1,
                file_name="fileName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createimageuploadurl(
            id, content_type=content_type, file_size=file_size, file_name=file_name, request_options=request_options
        )
        return _response.data

    async def completeimageupload(
        self, id: int, *, object_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesCompleteImageUploadResponse:
        """
        Parameters
        ----------
        id : int

        object_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesCompleteImageUploadResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.completeimageupload(
                id=1,
                object_key="objectKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.completeimageupload(
            id, object_key=object_key, request_options=request_options
        )
        return _response.data

    async def deleteimage(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesDeleteImageResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesDeleteImageResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.deleteimage(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteimage(id, request_options=request_options)
        return _response.data

    async def archive(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesArchiveResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesArchiveResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.archive(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.archive(id, request_options=request_options)
        return _response.data

    async def inactivate(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesInactivateResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesInactivateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.inactivate(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inactivate(id, request_options=request_options)
        return _response.data

    async def reactivate(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesReactivateResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesReactivateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.reactivate(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reactivate(id, request_options=request_options)
        return _response.data

    async def updatenotes(
        self, id: int, *, notes: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> PropertiesUpdateNotesResponse:
        """
        Parameters
        ----------
        id : int

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PropertiesUpdateNotesResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.properties.updatenotes(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatenotes(id, notes=notes, request_options=request_options)
        return _response.data
