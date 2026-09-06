

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCustomFontsClient, RawCustomFontsClient
from .types.batch_create_custom_fonts_request_items_item import BatchCreateCustomFontsRequestItemsItem
from .types.batch_create_custom_fonts_response import BatchCreateCustomFontsResponse
from .types.batch_delete_custom_fonts_request_items_item import BatchDeleteCustomFontsRequestItemsItem
from .types.batch_delete_custom_fonts_response import BatchDeleteCustomFontsResponse
from .types.create_custom_fonts_request_axes_item import CreateCustomFontsRequestAxesItem
from .types.create_custom_fonts_request_font_display import CreateCustomFontsRequestFontDisplay
from .types.create_custom_fonts_response import CreateCustomFontsResponse
from .types.get_custom_fonts_response import GetCustomFontsResponse
from .types.list_custom_fonts_response import ListCustomFontsResponse
from .types.replace_file_custom_fonts_request_axes_item import ReplaceFileCustomFontsRequestAxesItem
from .types.replace_file_custom_fonts_response import ReplaceFileCustomFontsResponse
from .types.update_custom_fonts_request_font_display import UpdateCustomFontsRequestFontDisplay
from .types.update_custom_fonts_response import UpdateCustomFontsResponse


OMIT = typing.cast(typing.Any, ...)


class CustomFontsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCustomFontsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCustomFontsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCustomFontsClient
        """
        return self._raw_client

    def list(
        self,
        site_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomFontsResponse:
        """
        List the custom fonts uploaded to a site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomFontsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_fonts.list(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._raw_client.list(site_id, offset=offset, limit=limit, request_options=request_options)
        return _response.data

    def create(
        self,
        site_id: str,
        *,
        file_name: str,
        file_hash: str,
        font_family: str,
        weight: int,
        italic: bool,
        font_display: CreateCustomFontsRequestFontDisplay,
        axes: typing.Optional[typing.Sequence[CreateCustomFontsRequestAxesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomFontsResponse:
        """
        Register a custom font on a site and get a presigned S3 URL to upload the font binary.

        The response includes a `customFont` object and an `upload` object. Use the `upload.url` and `upload.fields`
        to POST the font binary directly to S3 as `multipart/form-data`. The binary must go in a field named `file`
        and must be the last field in the form (an AWS S3 requirement). S3 returns `201 Created` on a successful upload.

        To learn more, see [Custom fonts](/data/docs/custom-fonts).

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        file_name : str
            File name including extension. Accepted extensions are `.woff2`, `.woff`, `.ttf`, `.otf`, and `.eot`. Maximum 256 characters.

        file_hash : str
            Lowercase hex MD5 hash of the font binary (exactly 32 characters)

        font_family : str
            The CSS font-family name (1-256 characters). Commas are stripped server-side.

        weight : int
            CSS font-weight value (1-1000)

        italic : bool
            Whether the font is italic

        font_display : CreateCustomFontsRequestFontDisplay
            CSS font-display value

        axes : typing.Optional[typing.Sequence[CreateCustomFontsRequestAxesItem]]
            Variable font axes. Omit or pass an empty array for static fonts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomFontsResponse
            Font registered. Upload the binary to the presigned S3 URL in `upload` to complete the process.

        Examples
        --------
        from fern.custom_fonts import CreateCustomFontsRequestFontDisplay

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_fonts.create(
            site_id="580e63e98c9a982ac9b8b741",
            file_name="AcmeSans-Regular.woff2",
            file_hash="3c7d87c9575702bc3b1e991f4d3c638e",
            font_family="Acme Sans",
            weight=400,
            italic=False,
            font_display=CreateCustomFontsRequestFontDisplay.AUTO,
        )
        """
        _response = self._raw_client.create(
            site_id,
            file_name=file_name,
            file_hash=file_hash,
            font_family=font_family,
            weight=weight,
            italic=italic,
            font_display=font_display,
            axes=axes,
            request_options=request_options,
        )
        return _response.data

    def get(
        self, site_id: str, font_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomFontsResponse:
        """
        Get details about a custom font on a site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomFontsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_fonts.get(
            site_id="580e63e98c9a982ac9b8b741",
            font_id="66f3a1b2c4d5e6f7a8b9c0d1",
        )
        """
        _response = self._raw_client.get(site_id, font_id, request_options=request_options)
        return _response.data

    def delete(self, site_id: str, font_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a custom font from a site.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_fonts.delete(
            site_id="580e63e98c9a982ac9b8b741",
            font_id="66f3a1b2c4d5e6f7a8b9c0d1",
        )
        """
        _response = self._raw_client.delete(site_id, font_id, request_options=request_options)
        return _response.data

    def update(
        self,
        site_id: str,
        font_id: str,
        *,
        font_family: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        italic: typing.Optional[bool] = OMIT,
        font_display: typing.Optional[UpdateCustomFontsRequestFontDisplay] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCustomFontsResponse:
        """
        Update the metadata of a custom font. The font binary is not changed by this endpoint.
        To replace the binary, use [Replace custom font file](#operation/replace-custom-font-file).

        The request body must include at least one of `fontFamily`, `weight`, `italic`, or `fontDisplay`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        font_family : typing.Optional[str]
            The CSS font-family name (1-256 characters)

        weight : typing.Optional[int]
            CSS font-weight value (1-1000)

        italic : typing.Optional[bool]
            Whether the font is italic

        font_display : typing.Optional[UpdateCustomFontsRequestFontDisplay]
            CSS font-display value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomFontsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_fonts.update(
            site_id="580e63e98c9a982ac9b8b741",
            font_id="66f3a1b2c4d5e6f7a8b9c0d1",
        )
        """
        _response = self._raw_client.update(
            site_id,
            font_id,
            font_family=font_family,
            weight=weight,
            italic=italic,
            font_display=font_display,
            request_options=request_options,
        )
        return _response.data

    def replace_file(
        self,
        site_id: str,
        font_id: str,
        *,
        file_name: str,
        file_hash: str,
        axes: typing.Optional[typing.Sequence[ReplaceFileCustomFontsRequestAxesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceFileCustomFontsResponse:
        """
        Replace the binary of an existing custom font while preserving its ID and any references to it.
        The upload handshake is identical to [Create custom font](#operation/create-custom-font).

        If the existing font has a non-empty `axes` array (a variable font), you must include an `axes` field
        in the request. Send `axes: []` to declare that the new binary is a static font, or send the new variable
        axes to declare it is still variable. Omitting `axes` when the existing font is variable returns `400`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        file_name : str
            File name including extension. Accepted extensions are `.woff2`, `.woff`, `.ttf`, `.otf`, and `.eot`. Maximum 256 characters.

        file_hash : str
            Lowercase hex MD5 hash of the font binary (exactly 32 characters)

        axes : typing.Optional[typing.Sequence[ReplaceFileCustomFontsRequestAxesItem]]
            Variable font axes for the replacement binary. Required when the existing font has a non-empty `axes` array.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceFileCustomFontsResponse
            File replacement initiated. Upload the binary to the presigned S3 URL in `upload` to complete the process.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_fonts.replace_file(
            site_id="580e63e98c9a982ac9b8b741",
            font_id="66f3a1b2c4d5e6f7a8b9c0d1",
            file_name="AcmeSans-Regular-v2.woff2",
            file_hash="3c7d87c9575702bc3b1e991f4d3c638e",
        )
        """
        _response = self._raw_client.replace_file(
            site_id, font_id, file_name=file_name, file_hash=file_hash, axes=axes, request_options=request_options
        )
        return _response.data

    def batch_create(
        self,
        site_id: str,
        *,
        items: typing.Sequence[BatchCreateCustomFontsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchCreateCustomFontsResponse:
        """
        Register 1–25 custom fonts in a single request and get a presigned S3 URL for each one.
        This collapses the registration step for a whole font family (for example, Regular, Bold,
        Italic, and Bold Italic) into one rate-limited request.

        Registration is batched, but the binary uploads are not: the response contains one `upload`
        object per registered font, and you must POST each font binary to its own presigned S3 URL
        exactly as you would for [Create custom font](#operation/create-custom-font). The Webflow API
        server never receives the raw font bytes.

        The response is `200 OK` for a valid request body. Per-font results are reported in the
        `created` and `failed` arrays. If the site's font limit is reached partway through the batch,
        the fonts that still fit are registered and returned in `created`, while the rest appear in
        `failed` with `name: "FontLimitReached"` — valid fonts are never discarded because a later
        font in the same batch could not be registered. Each presigned URL expires approximately
        15 minutes after issuance, so upload the binaries promptly.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        items : typing.Sequence[BatchCreateCustomFontsRequestItemsItem]
            The custom fonts to register. Each item uses the same shape as the single-font create request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchCreateCustomFontsResponse
            Request was successful. Check the `created` and `failed` arrays for per-item results.

        Examples
        --------
        from fern.custom_fonts import (
            BatchCreateCustomFontsRequestItemsItem,
            BatchCreateCustomFontsRequestItemsItemFontDisplay,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_fonts.batch_create(
            site_id="580e63e98c9a982ac9b8b741",
            items=[
                BatchCreateCustomFontsRequestItemsItem(
                    file_name="AcmeSans-Regular.woff2",
                    file_hash="3c7d87c9575702bc3b1e991f4d3c638e",
                    font_family="Acme Sans",
                    weight=400,
                    italic=False,
                    font_display=BatchCreateCustomFontsRequestItemsItemFontDisplay.AUTO,
                )
            ],
        )
        """
        _response = self._raw_client.batch_create(site_id, items=items, request_options=request_options)
        return _response.data

    def batch_delete(
        self,
        site_id: str,
        *,
        items: typing.Sequence[BatchDeleteCustomFontsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchDeleteCustomFontsResponse:
        """
        Delete 1-100 custom fonts in a single request. The response is always `200 OK` for a valid request body.
        Per-font results are reported in the `deleted` and `failed` arrays.

        The endpoint is idempotent: fonts that do not exist appear in `failed` with `name: "NotFound"` rather than
        failing the entire request. You can safely retry a partial failure by re-sending only the IDs that did not
        appear in `deleted`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        items : typing.Sequence[BatchDeleteCustomFontsRequestItemsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchDeleteCustomFontsResponse
            Request was successful. Check `deleted` and `failed` arrays for per-item results.

        Examples
        --------
        from fern.custom_fonts import BatchDeleteCustomFontsRequestItemsItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.custom_fonts.batch_delete(
            site_id="580e63e98c9a982ac9b8b741",
            items=[
                BatchDeleteCustomFontsRequestItemsItem(
                    id="66f3a1b2c4d5e6f7a8b9c0d1",
                )
            ],
        )
        """
        _response = self._raw_client.batch_delete(site_id, items=items, request_options=request_options)
        return _response.data


class AsyncCustomFontsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCustomFontsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCustomFontsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCustomFontsClient
        """
        return self._raw_client

    async def list(
        self,
        site_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCustomFontsResponse:
        """
        List the custom fonts uploaded to a site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCustomFontsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_fonts.list(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(site_id, offset=offset, limit=limit, request_options=request_options)
        return _response.data

    async def create(
        self,
        site_id: str,
        *,
        file_name: str,
        file_hash: str,
        font_family: str,
        weight: int,
        italic: bool,
        font_display: CreateCustomFontsRequestFontDisplay,
        axes: typing.Optional[typing.Sequence[CreateCustomFontsRequestAxesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCustomFontsResponse:
        """
        Register a custom font on a site and get a presigned S3 URL to upload the font binary.

        The response includes a `customFont` object and an `upload` object. Use the `upload.url` and `upload.fields`
        to POST the font binary directly to S3 as `multipart/form-data`. The binary must go in a field named `file`
        and must be the last field in the form (an AWS S3 requirement). S3 returns `201 Created` on a successful upload.

        To learn more, see [Custom fonts](/data/docs/custom-fonts).

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        file_name : str
            File name including extension. Accepted extensions are `.woff2`, `.woff`, `.ttf`, `.otf`, and `.eot`. Maximum 256 characters.

        file_hash : str
            Lowercase hex MD5 hash of the font binary (exactly 32 characters)

        font_family : str
            The CSS font-family name (1-256 characters). Commas are stripped server-side.

        weight : int
            CSS font-weight value (1-1000)

        italic : bool
            Whether the font is italic

        font_display : CreateCustomFontsRequestFontDisplay
            CSS font-display value

        axes : typing.Optional[typing.Sequence[CreateCustomFontsRequestAxesItem]]
            Variable font axes. Omit or pass an empty array for static fonts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCustomFontsResponse
            Font registered. Upload the binary to the presigned S3 URL in `upload` to complete the process.

        Examples
        --------
        import asyncio

        from fern.custom_fonts import CreateCustomFontsRequestFontDisplay

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_fonts.create(
                site_id="580e63e98c9a982ac9b8b741",
                file_name="AcmeSans-Regular.woff2",
                file_hash="3c7d87c9575702bc3b1e991f4d3c638e",
                font_family="Acme Sans",
                weight=400,
                italic=False,
                font_display=CreateCustomFontsRequestFontDisplay.AUTO,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            site_id,
            file_name=file_name,
            file_hash=file_hash,
            font_family=font_family,
            weight=weight,
            italic=italic,
            font_display=font_display,
            axes=axes,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self, site_id: str, font_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomFontsResponse:
        """
        Get details about a custom font on a site.

        Required scope | `sites:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomFontsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_fonts.get(
                site_id="580e63e98c9a982ac9b8b741",
                font_id="66f3a1b2c4d5e6f7a8b9c0d1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(site_id, font_id, request_options=request_options)
        return _response.data

    async def delete(
        self, site_id: str, font_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a custom font from a site.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_fonts.delete(
                site_id="580e63e98c9a982ac9b8b741",
                font_id="66f3a1b2c4d5e6f7a8b9c0d1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(site_id, font_id, request_options=request_options)
        return _response.data

    async def update(
        self,
        site_id: str,
        font_id: str,
        *,
        font_family: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        italic: typing.Optional[bool] = OMIT,
        font_display: typing.Optional[UpdateCustomFontsRequestFontDisplay] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCustomFontsResponse:
        """
        Update the metadata of a custom font. The font binary is not changed by this endpoint.
        To replace the binary, use [Replace custom font file](#operation/replace-custom-font-file).

        The request body must include at least one of `fontFamily`, `weight`, `italic`, or `fontDisplay`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        font_family : typing.Optional[str]
            The CSS font-family name (1-256 characters)

        weight : typing.Optional[int]
            CSS font-weight value (1-1000)

        italic : typing.Optional[bool]
            Whether the font is italic

        font_display : typing.Optional[UpdateCustomFontsRequestFontDisplay]
            CSS font-display value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCustomFontsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_fonts.update(
                site_id="580e63e98c9a982ac9b8b741",
                font_id="66f3a1b2c4d5e6f7a8b9c0d1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            site_id,
            font_id,
            font_family=font_family,
            weight=weight,
            italic=italic,
            font_display=font_display,
            request_options=request_options,
        )
        return _response.data

    async def replace_file(
        self,
        site_id: str,
        font_id: str,
        *,
        file_name: str,
        file_hash: str,
        axes: typing.Optional[typing.Sequence[ReplaceFileCustomFontsRequestAxesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceFileCustomFontsResponse:
        """
        Replace the binary of an existing custom font while preserving its ID and any references to it.
        The upload handshake is identical to [Create custom font](#operation/create-custom-font).

        If the existing font has a non-empty `axes` array (a variable font), you must include an `axes` field
        in the request. Send `axes: []` to declare that the new binary is a static font, or send the new variable
        axes to declare it is still variable. Omitting `axes` when the existing font is variable returns `400`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        font_id : str
            Unique identifier for a custom font on a site

        file_name : str
            File name including extension. Accepted extensions are `.woff2`, `.woff`, `.ttf`, `.otf`, and `.eot`. Maximum 256 characters.

        file_hash : str
            Lowercase hex MD5 hash of the font binary (exactly 32 characters)

        axes : typing.Optional[typing.Sequence[ReplaceFileCustomFontsRequestAxesItem]]
            Variable font axes for the replacement binary. Required when the existing font has a non-empty `axes` array.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceFileCustomFontsResponse
            File replacement initiated. Upload the binary to the presigned S3 URL in `upload` to complete the process.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_fonts.replace_file(
                site_id="580e63e98c9a982ac9b8b741",
                font_id="66f3a1b2c4d5e6f7a8b9c0d1",
                file_name="AcmeSans-Regular-v2.woff2",
                file_hash="3c7d87c9575702bc3b1e991f4d3c638e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_file(
            site_id, font_id, file_name=file_name, file_hash=file_hash, axes=axes, request_options=request_options
        )
        return _response.data

    async def batch_create(
        self,
        site_id: str,
        *,
        items: typing.Sequence[BatchCreateCustomFontsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchCreateCustomFontsResponse:
        """
        Register 1–25 custom fonts in a single request and get a presigned S3 URL for each one.
        This collapses the registration step for a whole font family (for example, Regular, Bold,
        Italic, and Bold Italic) into one rate-limited request.

        Registration is batched, but the binary uploads are not: the response contains one `upload`
        object per registered font, and you must POST each font binary to its own presigned S3 URL
        exactly as you would for [Create custom font](#operation/create-custom-font). The Webflow API
        server never receives the raw font bytes.

        The response is `200 OK` for a valid request body. Per-font results are reported in the
        `created` and `failed` arrays. If the site's font limit is reached partway through the batch,
        the fonts that still fit are registered and returned in `created`, while the rest appear in
        `failed` with `name: "FontLimitReached"` — valid fonts are never discarded because a later
        font in the same batch could not be registered. Each presigned URL expires approximately
        15 minutes after issuance, so upload the binaries promptly.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        items : typing.Sequence[BatchCreateCustomFontsRequestItemsItem]
            The custom fonts to register. Each item uses the same shape as the single-font create request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchCreateCustomFontsResponse
            Request was successful. Check the `created` and `failed` arrays for per-item results.

        Examples
        --------
        import asyncio

        from fern.custom_fonts import (
            BatchCreateCustomFontsRequestItemsItem,
            BatchCreateCustomFontsRequestItemsItemFontDisplay,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_fonts.batch_create(
                site_id="580e63e98c9a982ac9b8b741",
                items=[
                    BatchCreateCustomFontsRequestItemsItem(
                        file_name="AcmeSans-Regular.woff2",
                        file_hash="3c7d87c9575702bc3b1e991f4d3c638e",
                        font_family="Acme Sans",
                        weight=400,
                        italic=False,
                        font_display=BatchCreateCustomFontsRequestItemsItemFontDisplay.AUTO,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_create(site_id, items=items, request_options=request_options)
        return _response.data

    async def batch_delete(
        self,
        site_id: str,
        *,
        items: typing.Sequence[BatchDeleteCustomFontsRequestItemsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchDeleteCustomFontsResponse:
        """
        Delete 1-100 custom fonts in a single request. The response is always `200 OK` for a valid request body.
        Per-font results are reported in the `deleted` and `failed` arrays.

        The endpoint is idempotent: fonts that do not exist appear in `failed` with `name: "NotFound"` rather than
        failing the entire request. You can safely retry a partial failure by re-sending only the IDs that did not
        appear in `deleted`.

        Required scope | `sites:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        items : typing.Sequence[BatchDeleteCustomFontsRequestItemsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchDeleteCustomFontsResponse
            Request was successful. Check `deleted` and `failed` arrays for per-item results.

        Examples
        --------
        import asyncio

        from fern.custom_fonts import BatchDeleteCustomFontsRequestItemsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.custom_fonts.batch_delete(
                site_id="580e63e98c9a982ac9b8b741",
                items=[
                    BatchDeleteCustomFontsRequestItemsItem(
                        id="66f3a1b2c4d5e6f7a8b9c0d1",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_delete(site_id, items=items, request_options=request_options)
        return _response.data
