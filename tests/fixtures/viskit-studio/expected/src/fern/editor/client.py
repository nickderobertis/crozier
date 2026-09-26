

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.edit_accepted import EditAccepted
from ..types.edit_result_out import EditResultOut
from ..types.editor_project_response import EditorProjectResponse
from ..types.ocr_response import OcrResponse
from ..types.save_image_response import SaveImageResponse
from .raw_client import AsyncRawEditorClient, RawEditorClient
from .types.save_image_request_mode import SaveImageRequestMode


OMIT = typing.cast(typing.Any, ...)


class EditorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEditorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEditorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEditorClient
        """
        return self._raw_client

    def get_image_bytes(self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        image_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.get_image_bytes(
            image_id="image_id",
        )
        """
        _response = self._raw_client.get_image_bytes(image_id, request_options=request_options)
        return _response.data

    def start_edit(
        self,
        image_id: str,
        *,
        mask_box: typing.Dict[str, int],
        new_text: str,
        kit_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EditAccepted:
        """
        Parameters
        ----------
        image_id : str

        mask_box : typing.Dict[str, int]
            x,y,w,h

        new_text : str

        kit_id : typing.Optional[str]
            Optional kit id for local edit context; safe-character allowlist keeps sidecar references portable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditAccepted
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.start_edit(
            image_id="image_id",
            mask_box={"key": 1},
            new_text="new_text",
        )
        """
        _response = self._raw_client.start_edit(
            image_id, mask_box=mask_box, new_text=new_text, kit_id=kit_id, request_options=request_options
        )
        return _response.data

    def create_edit_result(
        self,
        image_id: str,
        *,
        result_data_url: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EditResultOut:
        """
        Parameters
        ----------
        image_id : str

        result_data_url : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        source_image_ref : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditResultOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.create_edit_result(
            image_id="image_id",
            result_data_url="result_data_url",
        )
        """
        _response = self._raw_client.create_edit_result(
            image_id,
            result_data_url=result_data_url,
            metadata=metadata,
            source_image_ref=source_image_ref,
            request_options=request_options,
        )
        return _response.data

    def get_edit_result_image(
        self, image_id: str, edit_result_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        image_id : str

        edit_result_ref : str

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.get_edit_result_image(
            image_id="image_id",
            edit_result_ref="edit_result_ref",
        )
        """
        _response = self._raw_client.get_edit_result_image(image_id, edit_result_ref, request_options=request_options)
        return _response.data

    def edit_events(
        self, image_id: str, *, job_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        image_id : str

        job_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.edit_events(
            image_id="image_id",
            job_id="job_id",
        )
        """
        _response = self._raw_client.edit_events(image_id, job_id=job_id, request_options=request_options)
        return _response.data

    def ocr_image(self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> OcrResponse:
        """
        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcrResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.ocr_image(
            image_id="image_id",
        )
        """
        _response = self._raw_client.ocr_image(image_id, request_options=request_options)
        return _response.data

    def get_editor_project(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EditorProjectResponse:
        """
        Return the saved Viskit editor project JSON for a canonical image id.

        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditorProjectResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.get_editor_project(
            image_id="image_id",
        )
        """
        _response = self._raw_client.get_editor_project(image_id, request_options=request_options)
        return _response.data

    def put_editor_project(
        self,
        image_id: str,
        *,
        document: typing.Dict[str, typing.Any],
        expected_revision: typing.Optional[int] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EditorProjectResponse:
        """
        Create or replace the persisted project JSON for a canonical image id.

        Parameters
        ----------
        image_id : str

        document : typing.Dict[str, typing.Any]
            Versioned ViskitEditorDocument JSON object

        expected_revision : typing.Optional[int]
            Optimistic concurrency guard; 409 when it differs from stored revision.

        source_image_ref : typing.Optional[str]
            Optional source_images.id backing this project import.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditorProjectResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.put_editor_project(
            image_id="image_id",
            document={"key": "value"},
        )
        """
        _response = self._raw_client.put_editor_project(
            image_id,
            document=document,
            expected_revision=expected_revision,
            source_image_ref=source_image_ref,
            request_options=request_options,
        )
        return _response.data

    def export_editor_project(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Download the saved editor project as project JSON.

        Parameters
        ----------
        image_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.export_editor_project(
            image_id="image_id",
        )
        """
        _response = self._raw_client.export_editor_project(image_id, request_options=request_options)
        return _response.data

    def import_editor_project(
        self,
        image_id: str,
        *,
        document: typing.Dict[str, typing.Any],
        expected_revision: typing.Optional[int] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EditorProjectResponse:
        """
        Import project JSON into the persisted editor state for this image.

        Parameters
        ----------
        image_id : str

        document : typing.Dict[str, typing.Any]
            Versioned ViskitEditorDocument JSON object

        expected_revision : typing.Optional[int]
            Optimistic concurrency guard; 409 when it differs from stored revision.

        source_image_ref : typing.Optional[str]
            Optional source_images.id backing this project import.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditorProjectResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.import_editor_project(
            image_id="image_id",
            document={"key": "value"},
        )
        """
        _response = self._raw_client.import_editor_project(
            image_id,
            document=document,
            expected_revision=expected_revision,
            source_image_ref=source_image_ref,
            request_options=request_options,
        )
        return _response.data

    def save_edited_image(
        self,
        image_id: str,
        *,
        edit_result_ref: str,
        mode: SaveImageRequestMode,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SaveImageResponse:
        """
        Persist an edit result via an explicit replace-or-copy choice.

        Parameters
        ----------
        image_id : str

        edit_result_ref : str

        mode : SaveImageRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SaveImageResponse
            Successful Response

        Examples
        --------
        from fern.editor import SaveImageRequestMode

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.editor.save_edited_image(
            image_id="image_id",
            edit_result_ref="edit_result_ref",
            mode=SaveImageRequestMode.REPLACE,
        )
        """
        _response = self._raw_client.save_edited_image(
            image_id, edit_result_ref=edit_result_ref, mode=mode, request_options=request_options
        )
        return _response.data


class AsyncEditorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEditorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEditorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEditorClient
        """
        return self._raw_client

    async def get_image_bytes(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        image_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.get_image_bytes(
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_image_bytes(image_id, request_options=request_options)
        return _response.data

    async def start_edit(
        self,
        image_id: str,
        *,
        mask_box: typing.Dict[str, int],
        new_text: str,
        kit_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EditAccepted:
        """
        Parameters
        ----------
        image_id : str

        mask_box : typing.Dict[str, int]
            x,y,w,h

        new_text : str

        kit_id : typing.Optional[str]
            Optional kit id for local edit context; safe-character allowlist keeps sidecar references portable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditAccepted
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.start_edit(
                image_id="image_id",
                mask_box={"key": 1},
                new_text="new_text",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_edit(
            image_id, mask_box=mask_box, new_text=new_text, kit_id=kit_id, request_options=request_options
        )
        return _response.data

    async def create_edit_result(
        self,
        image_id: str,
        *,
        result_data_url: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EditResultOut:
        """
        Parameters
        ----------
        image_id : str

        result_data_url : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        source_image_ref : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditResultOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.create_edit_result(
                image_id="image_id",
                result_data_url="result_data_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_edit_result(
            image_id,
            result_data_url=result_data_url,
            metadata=metadata,
            source_image_ref=source_image_ref,
            request_options=request_options,
        )
        return _response.data

    async def get_edit_result_image(
        self, image_id: str, edit_result_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        image_id : str

        edit_result_ref : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.get_edit_result_image(
                image_id="image_id",
                edit_result_ref="edit_result_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_edit_result_image(
            image_id, edit_result_ref, request_options=request_options
        )
        return _response.data

    async def edit_events(
        self, image_id: str, *, job_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        image_id : str

        job_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.edit_events(
                image_id="image_id",
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_events(image_id, job_id=job_id, request_options=request_options)
        return _response.data

    async def ocr_image(self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> OcrResponse:
        """
        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OcrResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.ocr_image(
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ocr_image(image_id, request_options=request_options)
        return _response.data

    async def get_editor_project(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EditorProjectResponse:
        """
        Return the saved Viskit editor project JSON for a canonical image id.

        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditorProjectResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.get_editor_project(
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_editor_project(image_id, request_options=request_options)
        return _response.data

    async def put_editor_project(
        self,
        image_id: str,
        *,
        document: typing.Dict[str, typing.Any],
        expected_revision: typing.Optional[int] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EditorProjectResponse:
        """
        Create or replace the persisted project JSON for a canonical image id.

        Parameters
        ----------
        image_id : str

        document : typing.Dict[str, typing.Any]
            Versioned ViskitEditorDocument JSON object

        expected_revision : typing.Optional[int]
            Optimistic concurrency guard; 409 when it differs from stored revision.

        source_image_ref : typing.Optional[str]
            Optional source_images.id backing this project import.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditorProjectResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.put_editor_project(
                image_id="image_id",
                document={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_editor_project(
            image_id,
            document=document,
            expected_revision=expected_revision,
            source_image_ref=source_image_ref,
            request_options=request_options,
        )
        return _response.data

    async def export_editor_project(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Download the saved editor project as project JSON.

        Parameters
        ----------
        image_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.export_editor_project(
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_editor_project(image_id, request_options=request_options)
        return _response.data

    async def import_editor_project(
        self,
        image_id: str,
        *,
        document: typing.Dict[str, typing.Any],
        expected_revision: typing.Optional[int] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EditorProjectResponse:
        """
        Import project JSON into the persisted editor state for this image.

        Parameters
        ----------
        image_id : str

        document : typing.Dict[str, typing.Any]
            Versioned ViskitEditorDocument JSON object

        expected_revision : typing.Optional[int]
            Optimistic concurrency guard; 409 when it differs from stored revision.

        source_image_ref : typing.Optional[str]
            Optional source_images.id backing this project import.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EditorProjectResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.import_editor_project(
                image_id="image_id",
                document={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_editor_project(
            image_id,
            document=document,
            expected_revision=expected_revision,
            source_image_ref=source_image_ref,
            request_options=request_options,
        )
        return _response.data

    async def save_edited_image(
        self,
        image_id: str,
        *,
        edit_result_ref: str,
        mode: SaveImageRequestMode,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SaveImageResponse:
        """
        Persist an edit result via an explicit replace-or-copy choice.

        Parameters
        ----------
        image_id : str

        edit_result_ref : str

        mode : SaveImageRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SaveImageResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.editor import SaveImageRequestMode

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.editor.save_edited_image(
                image_id="image_id",
                edit_result_ref="edit_result_ref",
                mode=SaveImageRequestMode.REPLACE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_edited_image(
            image_id, edit_result_ref=edit_result_ref, mode=mode, request_options=request_options
        )
        return _response.data
