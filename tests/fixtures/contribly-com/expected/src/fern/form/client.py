

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.form import Form
from ..types.form_field import FormField
from ..types.form_response import FormResponse
from ..types.tag import Tag
from .raw_client import AsyncRawFormClient, RawFormClient


OMIT = typing.cast(typing.Any, ...)


class FormClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFormClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFormClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFormClient
        """
        return self._raw_client

    def list_form_responses(
        self,
        *,
        user: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        contribution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FormResponse]:
        """
        Parameters
        ----------
        user : typing.Optional[str]
            Restrict results to responses submitted by this user.

        form : typing.Optional[str]
            Restrict results to responses submitted to this form.

        contribution : typing.Optional[str]
            Restrict results to responses relating to this contribution.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FormResponse]
            A list of form responses

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.form.list_form_responses()
        """
        _response = self._raw_client.list_form_responses(
            user=user, form=form, contribution=contribution, request_options=request_options
        )
        return _response.data

    def submit_a_response_to_a_form(
        self,
        *,
        contribution: typing.Optional[str] = OMIT,
        form: typing.Optional[str] = OMIT,
        responses: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FormResponse:
        """
        Parameters
        ----------
        contribution : typing.Optional[str]

        form : typing.Optional[str]

        responses : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormResponse
            Form response saved

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.form.submit_a_response_to_a_form()
        """
        _response = self._raw_client.submit_a_response_to_a_form(
            contribution=contribution, form=form, responses=responses, request_options=request_options
        )
        return _response.data

    def get_a_single_form_response_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FormResponse:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormResponse
            Form response found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.form.get_a_single_form_response_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_a_single_form_response_by_id(id, request_options=request_options)
        return _response.data

    def list_forms(
        self, *, owned_by: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Form]:
        """
        Parameters
        ----------
        owned_by : str
            Restrict results to forms owned by this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Form]
            A list of forms

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.form.list_forms(
            owned_by="ownedBy",
        )
        """
        _response = self._raw_client.list_forms(owned_by=owned_by, request_options=request_options)
        return _response.data

    def create_a_form(
        self,
        *,
        call_to_action: typing.Optional[str] = OMIT,
        css_url: typing.Optional[str] = OMIT,
        fields: typing.Optional[typing.Sequence[FormField]] = OMIT,
        heading: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        no_css: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Form:
        """
        Parameters
        ----------
        call_to_action : typing.Optional[str]

        css_url : typing.Optional[str]

        fields : typing.Optional[typing.Sequence[FormField]]

        heading : typing.Optional[str]

        name : typing.Optional[str]

        no_css : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[Tag]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Form
            Form created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.form.create_a_form()
        """
        _response = self._raw_client.create_a_form(
            call_to_action=call_to_action,
            css_url=css_url,
            fields=fields,
            heading=heading,
            name=name,
            no_css=no_css,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def get_a_single_form_by_id(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Form:
        """
        Parameters
        ----------
        id : str
            Id of the form to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Form
            Form found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.form.get_a_single_form_by_id(
            id="id",
        )
        """
        _response = self._raw_client.get_a_single_form_by_id(id, request_options=request_options)
        return _response.data

    def delete_this_form_and_all_of_its_responses(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Id of the form to delete

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
        client.form.delete_this_form_and_all_of_its_responses(
            id="id",
        )
        """
        _response = self._raw_client.delete_this_form_and_all_of_its_responses(id, request_options=request_options)
        return _response.data


class AsyncFormClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFormClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFormClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFormClient
        """
        return self._raw_client

    async def list_form_responses(
        self,
        *,
        user: typing.Optional[str] = None,
        form: typing.Optional[str] = None,
        contribution: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FormResponse]:
        """
        Parameters
        ----------
        user : typing.Optional[str]
            Restrict results to responses submitted by this user.

        form : typing.Optional[str]
            Restrict results to responses submitted to this form.

        contribution : typing.Optional[str]
            Restrict results to responses relating to this contribution.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FormResponse]
            A list of form responses

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.form.list_form_responses()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_form_responses(
            user=user, form=form, contribution=contribution, request_options=request_options
        )
        return _response.data

    async def submit_a_response_to_a_form(
        self,
        *,
        contribution: typing.Optional[str] = OMIT,
        form: typing.Optional[str] = OMIT,
        responses: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FormResponse:
        """
        Parameters
        ----------
        contribution : typing.Optional[str]

        form : typing.Optional[str]

        responses : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormResponse
            Form response saved

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.form.submit_a_response_to_a_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_response_to_a_form(
            contribution=contribution, form=form, responses=responses, request_options=request_options
        )
        return _response.data

    async def get_a_single_form_response_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FormResponse:
        """
        Parameters
        ----------
        id : str
            Id of the assignment to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FormResponse
            Form response found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.form.get_a_single_form_response_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_single_form_response_by_id(id, request_options=request_options)
        return _response.data

    async def list_forms(
        self, *, owned_by: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Form]:
        """
        Parameters
        ----------
        owned_by : str
            Restrict results to forms owned by this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Form]
            A list of forms

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.form.list_forms(
                owned_by="ownedBy",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_forms(owned_by=owned_by, request_options=request_options)
        return _response.data

    async def create_a_form(
        self,
        *,
        call_to_action: typing.Optional[str] = OMIT,
        css_url: typing.Optional[str] = OMIT,
        fields: typing.Optional[typing.Sequence[FormField]] = OMIT,
        heading: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        no_css: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[Tag]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Form:
        """
        Parameters
        ----------
        call_to_action : typing.Optional[str]

        css_url : typing.Optional[str]

        fields : typing.Optional[typing.Sequence[FormField]]

        heading : typing.Optional[str]

        name : typing.Optional[str]

        no_css : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[Tag]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Form
            Form created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.form.create_a_form()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_form(
            call_to_action=call_to_action,
            css_url=css_url,
            fields=fields,
            heading=heading,
            name=name,
            no_css=no_css,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def get_a_single_form_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Form:
        """
        Parameters
        ----------
        id : str
            Id of the form to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Form
            Form found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.form.get_a_single_form_by_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_single_form_by_id(id, request_options=request_options)
        return _response.data

    async def delete_this_form_and_all_of_its_responses(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Id of the form to delete

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
            await client.form.delete_this_form_and_all_of_its_responses(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_this_form_and_all_of_its_responses(
            id, request_options=request_options
        )
        return _response.data
