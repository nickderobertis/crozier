

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok37 import Ok37
from ..types.ok86 import Ok86
from ..types.ok87 import Ok87
from ..types.ok89 import Ok89
from ..types.ok90 import Ok90
from .raw_client import AsyncRawProblemsClient, RawProblemsClient


OMIT = typing.cast(typing.Any, ...)


class ProblemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProblemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProblemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProblemsClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_problems(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok86:
        """
        Gets a list of patient problems after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the problems are being displayed

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok86
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.base_url_persons_person_id_chart_problems(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_problems(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def post_base_url_persons_person_id_chart_problems(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a new problem for the given person id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the problem is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.post_base_url_persons_person_id_chart_problems(
            person_id="personId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_problems(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_problems_problem_id1(
        self, person_id: str, problem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok87:
        """
        Gets the details of a patient problem.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose problem is being retrieved

        problem_id : str
            (Required) (Required) The id of the problem

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok87
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.base_url_persons_person_id_chart_problems_problem_id1(
            person_id="personId",
            problem_id="problemId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_problems_problem_id1(
            person_id, problem_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_problems_problem_id(
        self,
        person_id: str,
        problem_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient problem

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the problem is being modified

        problem_id : str
            (Required) (Required) The id of the problem being modified

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.put_base_url_persons_person_id_chart_problems_problem_id(
            person_id="personId",
            problem_id="problemId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_problems_problem_id(
            person_id, problem_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_problems_problem_id(
        self, person_id: str, problem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a patient problem

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the problem is being removed

        problem_id : str
            (Required) (Required) The id of the problem being removed

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.base_url_persons_person_id_chart_problems_problem_id(
            person_id="personId",
            problem_id="problemId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_problems_problem_id(
            person_id, problem_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_problems_problem_id_interactions(
        self, person_id: str, problem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Ok37]:
        """
        Gets patient interactions for an existing problems after adding the problem so that user will be aware of the contraindications while updating them.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose interactions are being retrieved

        problem_id : str
            (Required) (Required) The id of the problem for which interactions are being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Ok37]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.base_url_persons_person_id_chart_problems_problem_id_interactions(
            person_id="personId",
            problem_id="problemId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_problems_problem_id_interactions(
            person_id, problem_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_problems_problem_id_notes(
        self,
        person_id: str,
        problem_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok89:
        """
        Gets a list of notes attached to a patient problem after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the problem notes are being retrieved

        problem_id : str
            (Required) (Required) The id of the problem for which the notes are being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok89
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.base_url_persons_person_id_chart_problems_problem_id_notes(
            person_id="personId",
            problem_id="problemId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_problems_problem_id_notes(
            person_id,
            problem_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def post_base_url_persons_person_id_chart_problems_problem_id_notes(
        self,
        person_id: str,
        problem_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a note to a patient problem

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which we are adding the problem note

        problem_id : str
            (Required) (Required) The id of the problem that the note is being added to

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.post_base_url_persons_person_id_chart_problems_problem_id_notes(
            person_id="personId",
            problem_id="problemId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_problems_problem_id_notes(
            person_id, problem_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_problems_problem_id_notes_note_id1(
        self, person_id: str, problem_id: str, note_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok90:
        """
        Gets a problem note.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the note is being retrieved

        problem_id : str
            (Required) (Required) The id of the problem that the note is associated with

        note_id : str
            (Required) (Required) The id of the note

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok90
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.base_url_persons_person_id_chart_problems_problem_id_notes_note_id1(
            person_id="personId",
            problem_id="problemId",
            note_id="noteId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_problems_problem_id_notes_note_id1(
            person_id, problem_id, note_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
        self,
        person_id: str,
        problem_id: str,
        note_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a problem note

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the note is being updated

        problem_id : str
            (Required) (Required) The id of the problem that the note is associated with

        note_id : str
            (Required) (Required) The id of the note

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.put_base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
            person_id="personId",
            problem_id="problemId",
            note_id="noteId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
            person_id, problem_id, note_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
        self, person_id: str, problem_id: str, note_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a problem note

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the note is being deleted

        problem_id : str
            (Required) (Required) The id of the problem that the note is associated with

        note_id : str
            (Required) (Required) The id of the note

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
            person_id="personId",
            problem_id="problemId",
            note_id="noteId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
            person_id, problem_id, note_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_problems_interactions(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Ok37]:
        """
        This route is meant to be used in conjunction with the POST for Patient Problem. The results of this route will be required by the POST for verification that interactions were viewed.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose interactions are being retrieved.

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Ok37]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.problems.base_url_persons_person_id_chart_problems_interactions(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_problems_interactions(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data


class AsyncProblemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProblemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProblemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProblemsClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_problems(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok86:
        """
        Gets a list of patient problems after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the problems are being displayed

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok86
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.base_url_persons_person_id_chart_problems(
                person_id="personId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_problems(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_problems(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a new problem for the given person id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the problem is being added

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.post_base_url_persons_person_id_chart_problems(
                person_id="personId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_problems(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_problems_problem_id1(
        self, person_id: str, problem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok87:
        """
        Gets the details of a patient problem.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose problem is being retrieved

        problem_id : str
            (Required) (Required) The id of the problem

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok87
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.base_url_persons_person_id_chart_problems_problem_id1(
                person_id="personId",
                problem_id="problemId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_problems_problem_id1(
            person_id, problem_id, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_problems_problem_id(
        self,
        person_id: str,
        problem_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient problem

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the problem is being modified

        problem_id : str
            (Required) (Required) The id of the problem being modified

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.put_base_url_persons_person_id_chart_problems_problem_id(
                person_id="personId",
                problem_id="problemId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_problems_problem_id(
            person_id, problem_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_problems_problem_id(
        self, person_id: str, problem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a patient problem

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the problem is being removed

        problem_id : str
            (Required) (Required) The id of the problem being removed

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.base_url_persons_person_id_chart_problems_problem_id(
                person_id="personId",
                problem_id="problemId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_problems_problem_id(
            person_id, problem_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_problems_problem_id_interactions(
        self, person_id: str, problem_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Ok37]:
        """
        Gets patient interactions for an existing problems after adding the problem so that user will be aware of the contraindications while updating them.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose interactions are being retrieved

        problem_id : str
            (Required) (Required) The id of the problem for which interactions are being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Ok37]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.base_url_persons_person_id_chart_problems_problem_id_interactions(
                person_id="personId",
                problem_id="problemId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_problems_problem_id_interactions(
            person_id, problem_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_problems_problem_id_notes(
        self,
        person_id: str,
        problem_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok89:
        """
        Gets a list of notes attached to a patient problem after performing additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the problem notes are being retrieved

        problem_id : str
            (Required) (Required) The id of the problem for which the notes are being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok89
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.base_url_persons_person_id_chart_problems_problem_id_notes(
                person_id="personId",
                problem_id="problemId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_problems_problem_id_notes(
            person_id,
            problem_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_problems_problem_id_notes(
        self,
        person_id: str,
        problem_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a note to a patient problem

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which we are adding the problem note

        problem_id : str
            (Required) (Required) The id of the problem that the note is being added to

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.post_base_url_persons_person_id_chart_problems_problem_id_notes(
                person_id="personId",
                problem_id="problemId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_problems_problem_id_notes(
            person_id, problem_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_problems_problem_id_notes_note_id1(
        self, person_id: str, problem_id: str, note_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok90:
        """
        Gets a problem note.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the note is being retrieved

        problem_id : str
            (Required) (Required) The id of the problem that the note is associated with

        note_id : str
            (Required) (Required) The id of the note

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok90
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.base_url_persons_person_id_chart_problems_problem_id_notes_note_id1(
                person_id="personId",
                problem_id="problemId",
                note_id="noteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_problems_problem_id_notes_note_id1(
            person_id, problem_id, note_id, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
        self,
        person_id: str,
        problem_id: str,
        note_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a problem note

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the note is being updated

        problem_id : str
            (Required) (Required) The id of the problem that the note is associated with

        note_id : str
            (Required) (Required) The id of the note

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.put_base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
                person_id="personId",
                problem_id="problemId",
                note_id="noteId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
            person_id, problem_id, note_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
        self, person_id: str, problem_id: str, note_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a problem note

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the note is being deleted

        problem_id : str
            (Required) (Required) The id of the problem that the note is associated with

        note_id : str
            (Required) (Required) The id of the note

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
                person_id="personId",
                problem_id="problemId",
                note_id="noteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_problems_problem_id_notes_note_id(
            person_id, problem_id, note_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_problems_interactions(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Ok37]:
        """
        This route is meant to be used in conjunction with the POST for Patient Problem. The results of this route will be required by the POST for verification that interactions were viewed.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose interactions are being retrieved.

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Ok37]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.problems.base_url_persons_person_id_chart_problems_interactions(
                person_id="personId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_problems_interactions(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data
