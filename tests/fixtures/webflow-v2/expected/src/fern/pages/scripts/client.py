

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawScriptsClient, RawScriptsClient
from .types.get_custom_code_scripts_response import GetCustomCodeScriptsResponse
from .types.upsert_custom_code_scripts_request_scripts_item import UpsertCustomCodeScriptsRequestScriptsItem
from .types.upsert_custom_code_scripts_response import UpsertCustomCodeScriptsResponse


OMIT = typing.cast(typing.Any, ...)


class ScriptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScriptsClient
        """
        return self._raw_client

    def get_custom_code(
        self, page_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomCodeScriptsResponse:
        """
        Get all scripts applied to a page.

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:read`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomCodeScriptsResponse
            Request was successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.scripts.get_custom_code(
            page_id="63c720f9347c2139b248e552",
        )
        """
        _response = self._raw_client.get_custom_code(page_id, request_options=request_options)
        return _response.data

    def upsert_custom_code(
        self,
        page_id: str,
        *,
        scripts: typing.Optional[typing.Sequence[UpsertCustomCodeScriptsRequestScriptsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpsertCustomCodeScriptsResponse:
        """
        Apply registered scripts to a page. If you have multiple scripts your App needs to apply or maintain on a page, ensure they are always included in the request body for this endpoint. To remove individual scripts, simply call this endpoint without the script in the request body.

        <Note title="Script Registration">
          To apply a script to a page, the script must first be registered to a Site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        scripts : typing.Optional[typing.Sequence[UpsertCustomCodeScriptsRequestScriptsItem]]
            A list of scripts applied to a Site or a Page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertCustomCodeScriptsResponse
            Request was successful

        Examples
        --------
        from fern.pages.scripts import (
            UpsertCustomCodeScriptsRequestScriptsItem,
            UpsertCustomCodeScriptsRequestScriptsItemLocation,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pages.scripts.upsert_custom_code(
            page_id="63c720f9347c2139b248e552",
            scripts=[
                UpsertCustomCodeScriptsRequestScriptsItem(
                    id="cms_slider",
                    location=UpsertCustomCodeScriptsRequestScriptsItemLocation.HEADER,
                    version="1.0.0",
                    attributes={"my-attribute": "some-value"},
                ),
                UpsertCustomCodeScriptsRequestScriptsItem(
                    id="alert",
                    location=UpsertCustomCodeScriptsRequestScriptsItemLocation.HEADER,
                    version="0.0.1",
                ),
            ],
        )
        """
        _response = self._raw_client.upsert_custom_code(page_id, scripts=scripts, request_options=request_options)
        return _response.data

    def delete_custom_code(self, page_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove all scripts from a page applied by the App. This endpoint will not remove scripts from the site's registered scripts.

        To remove individual scripts applied by the App, use the [Add/Update Custom Code](/data/reference/custom-code/custom-code-pages/upsert-custom-code) endpoint.

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

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
        client.pages.scripts.delete_custom_code(
            page_id="63c720f9347c2139b248e552",
        )
        """
        _response = self._raw_client.delete_custom_code(page_id, request_options=request_options)
        return _response.data


class AsyncScriptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScriptsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScriptsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScriptsClient
        """
        return self._raw_client

    async def get_custom_code(
        self, page_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCustomCodeScriptsResponse:
        """
        Get all scripts applied to a page.

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:read`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCustomCodeScriptsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.scripts.get_custom_code(
                page_id="63c720f9347c2139b248e552",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_custom_code(page_id, request_options=request_options)
        return _response.data

    async def upsert_custom_code(
        self,
        page_id: str,
        *,
        scripts: typing.Optional[typing.Sequence[UpsertCustomCodeScriptsRequestScriptsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpsertCustomCodeScriptsResponse:
        """
        Apply registered scripts to a page. If you have multiple scripts your App needs to apply or maintain on a page, ensure they are always included in the request body for this endpoint. To remove individual scripts, simply call this endpoint without the script in the request body.

        <Note title="Script Registration">
          To apply a script to a page, the script must first be registered to a Site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

        scripts : typing.Optional[typing.Sequence[UpsertCustomCodeScriptsRequestScriptsItem]]
            A list of scripts applied to a Site or a Page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertCustomCodeScriptsResponse
            Request was successful

        Examples
        --------
        import asyncio

        from fern.pages.scripts import (
            UpsertCustomCodeScriptsRequestScriptsItem,
            UpsertCustomCodeScriptsRequestScriptsItemLocation,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pages.scripts.upsert_custom_code(
                page_id="63c720f9347c2139b248e552",
                scripts=[
                    UpsertCustomCodeScriptsRequestScriptsItem(
                        id="cms_slider",
                        location=UpsertCustomCodeScriptsRequestScriptsItemLocation.HEADER,
                        version="1.0.0",
                        attributes={"my-attribute": "some-value"},
                    ),
                    UpsertCustomCodeScriptsRequestScriptsItem(
                        id="alert",
                        location=UpsertCustomCodeScriptsRequestScriptsItemLocation.HEADER,
                        version="0.0.1",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_custom_code(page_id, scripts=scripts, request_options=request_options)
        return _response.data

    async def delete_custom_code(
        self, page_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove all scripts from a page applied by the App. This endpoint will not remove scripts from the site's registered scripts.

        To remove individual scripts applied by the App, use the [Add/Update Custom Code](/data/reference/custom-code/custom-code-pages/upsert-custom-code) endpoint.

        <Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        page_id : str
            Unique identifier for a Page

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
            await client.pages.scripts.delete_custom_code(
                page_id="63c720f9347c2139b248e552",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_custom_code(page_id, request_options=request_options)
        return _response.data
