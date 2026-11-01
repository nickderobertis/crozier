

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.segment_envelope import SegmentEnvelope
from ..types.segment_list import SegmentList
from .raw_client import AsyncRawSegmentsClient, RawSegmentsClient


OMIT = typing.cast(typing.Any, ...)


class SegmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSegmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSegmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSegmentsClient
        """
        return self._raw_client

    def alle_segmenten_opvragen(
        self, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SegmentList:
        """
        All segments of a list in an array of segment objects. The segment objects are included in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentList
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.segments.alle_segmenten_opvragen(
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.alle_segmenten_opvragen(list_id=list_id, request_options=request_options)
        return _response.data

    def segment_toevoegen(
        self, *, list_id: str, name: str, definition: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SegmentEnvelope:
        """
        If there is something wrong with the provided parameters, an error code and message will be displayed. See above under Error Messages for what the codes mean.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : str
            The name of the segment

        definition : str
            The segment definition as JSON text. Note that a field name that does not exist is accepted and produces a segment that matches nobody.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.segments.segment_toevoegen(
            list_id="BaImMu3JZA",
            name="Nieuwsbrief",
            definition='{"blocks":[{"rules":[{"input":{"subject":"woonplaats","comparator":"equal","multi":"","text":"Utrecht"},"type":"members"}]}]}',
        )
        """
        _response = self._raw_client.segment_toevoegen(
            list_id=list_id, name=name, definition=definition, request_options=request_options
        )
        return _response.data

    def segment_opvragen(
        self, segment_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SegmentEnvelope:
        """
        All information about a segment.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.segments.segment_opvragen(
            segment_id="pDrp5KOD0z",
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.segment_opvragen(segment_id, list_id=list_id, request_options=request_options)
        return _response.data

    def segment_wijzigen(
        self,
        segment_id: str,
        *,
        list_id: str,
        name: typing.Optional[str] = OMIT,
        definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SegmentEnvelope:
        """
        You only need to include the fields that need to be changed in the request. Fields that are not mentioned retain their current value. Once a field is mentioned, it is checked and can therefore cause an error message. This error message will include a code and a message. See above under Error Messages for what the codes mean.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : typing.Optional[str]
            The name of the segment

        definition : typing.Optional[str]
            The definition of the segment (string in JSON format)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.segments.segment_wijzigen(
            segment_id="pDrp5KOD0z",
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.segment_wijzigen(
            segment_id, list_id=list_id, name=name, definition=definition, request_options=request_options
        )
        return _response.data

    def segment_verwijderen(
        self, segment_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SegmentEnvelope:
        """
        This permanently deletes a segment. After this, the segment cannot be retrieved again.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.segments.segment_verwijderen(
            segment_id="pDrp5KOD0z",
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.segment_verwijderen(segment_id, list_id=list_id, request_options=request_options)
        return _response.data


class AsyncSegmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSegmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSegmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSegmentsClient
        """
        return self._raw_client

    async def alle_segmenten_opvragen(
        self, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SegmentList:
        """
        All segments of a list in an array of segment objects. The segment objects are included in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentList
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.segments.alle_segmenten_opvragen(
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.alle_segmenten_opvragen(list_id=list_id, request_options=request_options)
        return _response.data

    async def segment_toevoegen(
        self, *, list_id: str, name: str, definition: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SegmentEnvelope:
        """
        If there is something wrong with the provided parameters, an error code and message will be displayed. See above under Error Messages for what the codes mean.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : str
            The name of the segment

        definition : str
            The segment definition as JSON text. Note that a field name that does not exist is accepted and produces a segment that matches nobody.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.segments.segment_toevoegen(
                list_id="BaImMu3JZA",
                name="Nieuwsbrief",
                definition='{"blocks":[{"rules":[{"input":{"subject":"woonplaats","comparator":"equal","multi":"","text":"Utrecht"},"type":"members"}]}]}',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.segment_toevoegen(
            list_id=list_id, name=name, definition=definition, request_options=request_options
        )
        return _response.data

    async def segment_opvragen(
        self, segment_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SegmentEnvelope:
        """
        All information about a segment.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.segments.segment_opvragen(
                segment_id="pDrp5KOD0z",
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.segment_opvragen(
            segment_id, list_id=list_id, request_options=request_options
        )
        return _response.data

    async def segment_wijzigen(
        self,
        segment_id: str,
        *,
        list_id: str,
        name: typing.Optional[str] = OMIT,
        definition: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SegmentEnvelope:
        """
        You only need to include the fields that need to be changed in the request. Fields that are not mentioned retain their current value. Once a field is mentioned, it is checked and can therefore cause an error message. This error message will include a code and a message. See above under Error Messages for what the codes mean.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : typing.Optional[str]
            The name of the segment

        definition : typing.Optional[str]
            The definition of the segment (string in JSON format)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.segments.segment_wijzigen(
                segment_id="pDrp5KOD0z",
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.segment_wijzigen(
            segment_id, list_id=list_id, name=name, definition=definition, request_options=request_options
        )
        return _response.data

    async def segment_verwijderen(
        self, segment_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SegmentEnvelope:
        """
        This permanently deletes a segment. After this, the segment cannot be retrieved again.

        Parameters
        ----------
        segment_id : str
            The id of the segment. You find it in the response of [Get all segments](/segmenten/alle-segmenten-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SegmentEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.segments.segment_verwijderen(
                segment_id="pDrp5KOD0z",
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.segment_verwijderen(
            segment_id, list_id=list_id, request_options=request_options
        )
        return _response.data
