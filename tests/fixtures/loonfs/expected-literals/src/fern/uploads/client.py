

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.complete_upload_body import CompleteUploadBody
from ..types.create_upload_body import CreateUploadBody
from ..types.sign_upload_parts_response import SignUploadPartsResponse
from ..types.upload_part_checksum_claim import UploadPartChecksumClaim
from ..types.upload_session import UploadSession
from .raw_client import AsyncRawUploadsClient, RawUploadsClient


OMIT = typing.cast(typing.Any, ...)


class UploadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUploadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUploadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUploadsClient
        """
        return self._raw_client

    def create(
        self, namespace_id: str, *, request: CreateUploadBody, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadSession:
        """
        Starts an upload session for content that a later commit can reference. A service-proxied upload sends the bytes through the server, and a direct PUT upload returns a presigned upload capability.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request : CreateUploadBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            Upload session started

        Examples
        --------
        from fern import CreateUploadBody_DirectMultipart, FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.uploads.create(
            namespace_id="namespace_id",
            request=CreateUploadBody_DirectMultipart(),
        )
        """
        _response = self._raw_client.create(namespace_id, request=request, request_options=request_options)
        return _response.data

    def retrieve(
        self, namespace_id: str, upload_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadSession:
        """
        Returns an upload session. An open `direct_put` session includes a newly signed upload capability. A completed session includes a new content token, so the client can retry the commit without uploading the content again.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            Upload session state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.uploads.retrieve(
            namespace_id="namespace_id",
            upload_id="upload_id",
        )
        """
        _response = self._raw_client.retrieve(namespace_id, upload_id, request_options=request_options)
        return _response.data

    def abort(
        self, namespace_id: str, upload_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadSession:
        """
        Aborts an open upload session and deletes the object that the session was writing. Repeating the request succeeds, but a completed session can't be aborted.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            Upload aborted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.uploads.abort(
            namespace_id="namespace_id",
            upload_id="upload_id",
        )
        """
        _response = self._raw_client.abort(namespace_id, upload_id, request_options=request_options)
        return _response.data

    def complete(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        request: CompleteUploadBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadSession:
        """
        Completes an upload. The request mode must match the mode that started the session. A direct upload includes a content claim, and a multipart upload also includes the completed parts.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request : CompleteUploadBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            Upload completed

        Examples
        --------
        from fern import (
            Checksum,
            CompletedUploadPart,
            CompleteUploadBody_DirectMultipart,
            FernApi,
            UploadContentClaim,
        )

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.uploads.complete(
            namespace_id="namespace_id",
            upload_id="upload_id",
            request=CompleteUploadBody_DirectMultipart(
                content=UploadContentClaim(
                    checksum=Checksum(
                        algorithm="crc64nvme",
                        value="value",
                    ),
                    size_bytes=1000000,
                ),
                parts=[
                    CompletedUploadPart(
                        checksum=Checksum(
                            algorithm="crc64nvme",
                            value="value",
                        ),
                        etag="etag",
                        part_number=1,
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.complete(namespace_id, upload_id, request=request, request_options=request_options)
        return _response.data

    def put_content(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadSession:
        """
        Uploads bytes into a service-proxied upload session and returns the open session with the staged content reference.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            Open session with the staged content reference
        """
        _response = self._raw_client.put_content(
            namespace_id, upload_id, request=request, request_options=request_options
        )
        return _response.data

    def sign_parts(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        parts: typing.Sequence[UploadPartChecksumClaim],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignUploadPartsResponse:
        """
        Returns one short-lived upload capability for each requested part of an open `direct_multipart` session. Each capability is bound to the part's checksum. To retry a part, a client asks for its capability again.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        parts : typing.Sequence[UploadPartChecksumClaim]
            The parts to authorize. A repeated part number replaces the earlier upload of that part.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignUploadPartsResponse
            Part capabilities issued

        Examples
        --------
        from fern import Checksum, FernApi, UploadPartChecksumClaim

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.uploads.sign_parts(
            namespace_id="namespace_id",
            upload_id="upload_id",
            parts=[
                UploadPartChecksumClaim(
                    checksum=Checksum(
                        algorithm="crc64nvme",
                        value="value",
                    ),
                    part_number=1,
                )
            ],
        )
        """
        _response = self._raw_client.sign_parts(namespace_id, upload_id, parts=parts, request_options=request_options)
        return _response.data


class AsyncUploadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUploadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUploadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUploadsClient
        """
        return self._raw_client

    async def create(
        self, namespace_id: str, *, request: CreateUploadBody, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadSession:
        """
        Starts an upload session for content that a later commit can reference. A service-proxied upload sends the bytes through the server, and a direct PUT upload returns a presigned upload capability.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request : CreateUploadBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            Upload session started

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreateUploadBody_DirectMultipart

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.uploads.create(
                namespace_id="namespace_id",
                request=CreateUploadBody_DirectMultipart(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(namespace_id, request=request, request_options=request_options)
        return _response.data

    async def retrieve(
        self, namespace_id: str, upload_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadSession:
        """
        Returns an upload session. An open `direct_put` session includes a newly signed upload capability. A completed session includes a new content token, so the client can retry the commit without uploading the content again.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            Upload session state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.uploads.retrieve(
                namespace_id="namespace_id",
                upload_id="upload_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(namespace_id, upload_id, request_options=request_options)
        return _response.data

    async def abort(
        self, namespace_id: str, upload_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadSession:
        """
        Aborts an open upload session and deletes the object that the session was writing. Repeating the request succeeds, but a completed session can't be aborted.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            Upload aborted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.uploads.abort(
                namespace_id="namespace_id",
                upload_id="upload_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.abort(namespace_id, upload_id, request_options=request_options)
        return _response.data

    async def complete(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        request: CompleteUploadBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadSession:
        """
        Completes an upload. The request mode must match the mode that started the session. A direct upload includes a content claim, and a multipart upload also includes the completed parts.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request : CompleteUploadBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            Upload completed

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Checksum,
            CompletedUploadPart,
            CompleteUploadBody_DirectMultipart,
            UploadContentClaim,
        )

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.uploads.complete(
                namespace_id="namespace_id",
                upload_id="upload_id",
                request=CompleteUploadBody_DirectMultipart(
                    content=UploadContentClaim(
                        checksum=Checksum(
                            algorithm="crc64nvme",
                            value="value",
                        ),
                        size_bytes=1000000,
                    ),
                    parts=[
                        CompletedUploadPart(
                            checksum=Checksum(
                                algorithm="crc64nvme",
                                value="value",
                            ),
                            etag="etag",
                            part_number=1,
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete(
            namespace_id, upload_id, request=request, request_options=request_options
        )
        return _response.data

    async def put_content(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UploadSession:
        """
        Uploads bytes into a service-proxied upload session and returns the open session with the staged content reference.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UploadSession
            Open session with the staged content reference
        """
        _response = await self._raw_client.put_content(
            namespace_id, upload_id, request=request, request_options=request_options
        )
        return _response.data

    async def sign_parts(
        self,
        namespace_id: str,
        upload_id: str,
        *,
        parts: typing.Sequence[UploadPartChecksumClaim],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SignUploadPartsResponse:
        """
        Returns one short-lived upload capability for each requested part of an open `direct_multipart` session. Each capability is bound to the part's checksum. To retry a part, a client asks for its capability again.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        upload_id : str
            The upload session ID.

        parts : typing.Sequence[UploadPartChecksumClaim]
            The parts to authorize. A repeated part number replaces the earlier upload of that part.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignUploadPartsResponse
            Part capabilities issued

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Checksum, UploadPartChecksumClaim

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.uploads.sign_parts(
                namespace_id="namespace_id",
                upload_id="upload_id",
                parts=[
                    UploadPartChecksumClaim(
                        checksum=Checksum(
                            algorithm="crc64nvme",
                            value="value",
                        ),
                        part_number=1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sign_parts(
            namespace_id, upload_id, parts=parts, request_options=request_options
        )
        return _response.data
