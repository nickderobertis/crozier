

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCommentsClient, RawCommentsClient
from .types.comments_read_response import CommentsReadResponse


OMIT = typing.cast(typing.Any, ...)


class CommentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCommentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCommentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCommentsClient
        """
        return self._raw_client

    def read(self, comment_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> CommentsReadResponse:
        """
        Retrieves the details of a comment
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested comment, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        comment_id : str
            The unique identifier of the comment you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommentsReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.comments.read(
            comment_id="comment_id",
        )
        """
        _response = self._raw_client.read(comment_id, request_options=request_options)
        return _response.data

    def put(
        self,
        comment_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the specified comment by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        #### Returns
        Returns JSON with a `data` key containing the new representation of the updated comment, if the request is successful.

        If the request is unsuccessful, JSON with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        comment_id : str
            The unique identifier of the comment you wish to update.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.comments.put(
            comment_id="comment_id",
            request={
                "data": {
                    "attributes": {"content": "changed comment content"},
                    "id": "{comment_id}",
                    "type": "comments",
                }
            },
        )
        """
        _response = self._raw_client.put(comment_id, request=request, request_options=request_options)
        return _response.data

    def delete(self, comment_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a comment. This action can be undone by setting deleted to False in a comment update request.
        #### Returns
        If the request is successful, no content is returned.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        comment_id : str
            The unique identifier of the comment you wish to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.comments.delete(
            comment_id="comment_id",
        )
        """
        _response = self._raw_client.delete(comment_id, request_options=request_options)
        return _response.data


class AsyncCommentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCommentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCommentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCommentsClient
        """
        return self._raw_client

    async def read(
        self, comment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommentsReadResponse:
        """
        Retrieves the details of a comment
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested comment, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        comment_id : str
            The unique identifier of the comment you wish to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommentsReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.comments.read(
                comment_id="comment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read(comment_id, request_options=request_options)
        return _response.data

    async def put(
        self,
        comment_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the specified comment by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        #### Returns
        Returns JSON with a `data` key containing the new representation of the updated comment, if the request is successful.

        If the request is unsuccessful, JSON with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        comment_id : str
            The unique identifier of the comment you wish to update.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.comments.put(
                comment_id="comment_id",
                request={
                    "data": {
                        "attributes": {"content": "changed comment content"},
                        "id": "{comment_id}",
                        "type": "comments",
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(comment_id, request=request, request_options=request_options)
        return _response.data

    async def delete(self, comment_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a comment. This action can be undone by setting deleted to False in a comment update request.
        #### Returns
        If the request is successful, no content is returned.

        If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        comment_id : str
            The unique identifier of the comment you wish to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.comments.delete(
                comment_id="comment_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(comment_id, request_options=request_options)
        return _response.data
