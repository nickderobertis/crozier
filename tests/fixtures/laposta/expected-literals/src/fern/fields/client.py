

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.field_envelope import FieldEnvelope
from ..types.field_list import FieldList
from .raw_client import AsyncRawFieldsClient, RawFieldsClient
from .types.veld_toevoegen_request_datatype import VeldToevoegenRequestDatatype
from .types.veld_toevoegen_request_datatype_display import VeldToevoegenRequestDatatypeDisplay
from .types.veld_wijzigen_request_datatype import VeldWijzigenRequestDatatype
from .types.veld_wijzigen_request_datatype_display import VeldWijzigenRequestDatatypeDisplay


OMIT = typing.cast(typing.Any, ...)


class FieldsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFieldsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFieldsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFieldsClient
        """
        return self._raw_client

    def alle_velden_opvragen(
        self, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FieldList:
        """
        All fields of a list in an array of field objects. The field objects are formatted in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldList
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.fields.alle_velden_opvragen(
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.alle_velden_opvragen(list_id=list_id, request_options=request_options)
        return _response.data

    def veld_toevoegen(
        self,
        *,
        list_id: str,
        name: str,
        datatype: VeldToevoegenRequestDatatype,
        required: bool,
        in_form: bool,
        in_list: bool,
        defaultvalue: typing.Optional[str] = OMIT,
        datatype_display: typing.Optional[VeldToevoegenRequestDatatypeDisplay] = OMIT,
        options: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FieldEnvelope:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : str
            A name for this field

        datatype : VeldToevoegenRequestDatatype
            The data type: text, numeric, date, select_single or select_multiple

        required : bool
            Is this a mandatory field?

        in_form : bool
            Does this field occur in the subscription form? (boolean)

        in_list : bool
            Is this field visible in Laposta's overview? (boolean)

        defaultvalue : typing.Optional[str]
            A potential default value

        datatype_display : typing.Optional[VeldToevoegenRequestDatatypeDisplay]
            Only applicable for select_single: the desired display (select, radio)

        options : typing.Optional[typing.Sequence[typing.Any]]
            What selection options are available? (mandatory for the data types select_single of select_multiple). The options can be given as an array. In the answer the options are repeated, but there is also an extra field options_full. Also listed are the option IDs, which may eventually be used to change the options later.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.fields.veld_toevoegen(
            list_id="BaImMu3JZA",
            name="Nieuwsbrief",
            datatype="text",
            required=True,
            in_form=True,
            in_list=True,
        )
        """
        _response = self._raw_client.veld_toevoegen(
            list_id=list_id,
            name=name,
            datatype=datatype,
            required=required,
            in_form=in_form,
            in_list=in_list,
            defaultvalue=defaultvalue,
            datatype_display=datatype_display,
            options=options,
            request_options=request_options,
        )
        return _response.data

    def veld_opvragen(
        self, field_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FieldEnvelope:
        """
        All information about a field.

        Parameters
        ----------
        field_id : str
            The id of the field. You find it in the response of [Get all fields](/velden/alle-velden-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.fields.veld_opvragen(
            field_id="Z87ysHha9A",
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.veld_opvragen(field_id, list_id=list_id, request_options=request_options)
        return _response.data

    def veld_wijzigen(
        self,
        field_id: str,
        *,
        list_id: str,
        required: bool,
        name: typing.Optional[str] = OMIT,
        datatype: typing.Optional[VeldWijzigenRequestDatatype] = OMIT,
        datatype_display: typing.Optional[VeldWijzigenRequestDatatypeDisplay] = OMIT,
        options_full: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        defaultvalue: typing.Optional[str] = OMIT,
        in_form: typing.Optional[bool] = OMIT,
        in_list: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FieldEnvelope:
        """
        You will only have to include the parts that need to be modified. Parts that are not mentioned will keep their current values. As soon as a part is mentioned it does get checked, and thus can cause an error message. This error message contains a code with a message. See above under 'Error messages' what these codes stand for. Pass options_full as a complete replacement for the option list. The key of each entry determines the operation: You may also pass options_full as an array of {"id", "value"} objects — the same shape as the response. The API will handle both formats.

        Parameters
        ----------
        field_id : str

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        required : bool
            Is this a mandatory field?

        name : typing.Optional[str]
            A name for this field

        datatype : typing.Optional[VeldWijzigenRequestDatatype]
            The data type of this field (text, numeric, date, select_single, select_multiple)

        datatype_display : typing.Optional[VeldWijzigenRequestDatatypeDisplay]
            Only applicable for select_single: the desired display (select, radio)

        options_full : typing.Optional[typing.Sequence[typing.Any]]
            The full set of options for a select_single or select_multiple field, as a key/value map of id → label. The key controls what happens to each option: Existing numeric ID (e.g. "2") — keeps or modifies the option. Changing the label updates it in-place; the ID stays the same, so existing member data is preserved. Non-numeric key (e.g. "new-0") — adds a new option; a fresh ID is assigned automatically. Omitting an existing ID — deletes that option. Always include every option you want to keep. Must be sent as JSON. Alternative format: instead of a key/value map you may also pass an array of objects in the same shape as the response: [{"id": "1", "value": "Red"}, {"id": "new-0", "value": "Orange"}]. The API will normalise this automatically.

        defaultvalue : typing.Optional[str]
            The default value (will be used in the absence of this field)

        in_form : typing.Optional[bool]
            Does this field occur in the subscription form? (boolean)

        in_list : typing.Optional[bool]
            Is this field visible in Laposta's overview? (boolean)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.fields.veld_wijzigen(
            field_id="field_id",
            list_id="BaImMu3JZA",
            required=True,
        )
        """
        _response = self._raw_client.veld_wijzigen(
            field_id,
            list_id=list_id,
            required=required,
            name=name,
            datatype=datatype,
            datatype_display=datatype_display,
            options_full=options_full,
            defaultvalue=defaultvalue,
            in_form=in_form,
            in_list=in_list,
            request_options=request_options,
        )
        return _response.data

    def veld_verwijderen(
        self, field_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FieldEnvelope:
        """
        This permanently deletes a field. If the field does not exist, an error message is displayed. In response you are shown another field object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the field.

        Parameters
        ----------
        field_id : str
            The id of the field. You find it in the response of [Get all fields](/velden/alle-velden-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.fields.veld_verwijderen(
            field_id="Z87ysHha9A",
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.veld_verwijderen(field_id, list_id=list_id, request_options=request_options)
        return _response.data


class AsyncFieldsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFieldsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFieldsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFieldsClient
        """
        return self._raw_client

    async def alle_velden_opvragen(
        self, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FieldList:
        """
        All fields of a list in an array of field objects. The field objects are formatted in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldList
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
            await client.fields.alle_velden_opvragen(
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.alle_velden_opvragen(list_id=list_id, request_options=request_options)
        return _response.data

    async def veld_toevoegen(
        self,
        *,
        list_id: str,
        name: str,
        datatype: VeldToevoegenRequestDatatype,
        required: bool,
        in_form: bool,
        in_list: bool,
        defaultvalue: typing.Optional[str] = OMIT,
        datatype_display: typing.Optional[VeldToevoegenRequestDatatypeDisplay] = OMIT,
        options: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FieldEnvelope:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        name : str
            A name for this field

        datatype : VeldToevoegenRequestDatatype
            The data type: text, numeric, date, select_single or select_multiple

        required : bool
            Is this a mandatory field?

        in_form : bool
            Does this field occur in the subscription form? (boolean)

        in_list : bool
            Is this field visible in Laposta's overview? (boolean)

        defaultvalue : typing.Optional[str]
            A potential default value

        datatype_display : typing.Optional[VeldToevoegenRequestDatatypeDisplay]
            Only applicable for select_single: the desired display (select, radio)

        options : typing.Optional[typing.Sequence[typing.Any]]
            What selection options are available? (mandatory for the data types select_single of select_multiple). The options can be given as an array. In the answer the options are repeated, but there is also an extra field options_full. Also listed are the option IDs, which may eventually be used to change the options later.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldEnvelope
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
            await client.fields.veld_toevoegen(
                list_id="BaImMu3JZA",
                name="Nieuwsbrief",
                datatype="text",
                required=True,
                in_form=True,
                in_list=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.veld_toevoegen(
            list_id=list_id,
            name=name,
            datatype=datatype,
            required=required,
            in_form=in_form,
            in_list=in_list,
            defaultvalue=defaultvalue,
            datatype_display=datatype_display,
            options=options,
            request_options=request_options,
        )
        return _response.data

    async def veld_opvragen(
        self, field_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FieldEnvelope:
        """
        All information about a field.

        Parameters
        ----------
        field_id : str
            The id of the field. You find it in the response of [Get all fields](/velden/alle-velden-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldEnvelope
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
            await client.fields.veld_opvragen(
                field_id="Z87ysHha9A",
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.veld_opvragen(field_id, list_id=list_id, request_options=request_options)
        return _response.data

    async def veld_wijzigen(
        self,
        field_id: str,
        *,
        list_id: str,
        required: bool,
        name: typing.Optional[str] = OMIT,
        datatype: typing.Optional[VeldWijzigenRequestDatatype] = OMIT,
        datatype_display: typing.Optional[VeldWijzigenRequestDatatypeDisplay] = OMIT,
        options_full: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        defaultvalue: typing.Optional[str] = OMIT,
        in_form: typing.Optional[bool] = OMIT,
        in_list: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FieldEnvelope:
        """
        You will only have to include the parts that need to be modified. Parts that are not mentioned will keep their current values. As soon as a part is mentioned it does get checked, and thus can cause an error message. This error message contains a code with a message. See above under 'Error messages' what these codes stand for. Pass options_full as a complete replacement for the option list. The key of each entry determines the operation: You may also pass options_full as an array of {"id", "value"} objects — the same shape as the response. The API will handle both formats.

        Parameters
        ----------
        field_id : str

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        required : bool
            Is this a mandatory field?

        name : typing.Optional[str]
            A name for this field

        datatype : typing.Optional[VeldWijzigenRequestDatatype]
            The data type of this field (text, numeric, date, select_single, select_multiple)

        datatype_display : typing.Optional[VeldWijzigenRequestDatatypeDisplay]
            Only applicable for select_single: the desired display (select, radio)

        options_full : typing.Optional[typing.Sequence[typing.Any]]
            The full set of options for a select_single or select_multiple field, as a key/value map of id → label. The key controls what happens to each option: Existing numeric ID (e.g. "2") — keeps or modifies the option. Changing the label updates it in-place; the ID stays the same, so existing member data is preserved. Non-numeric key (e.g. "new-0") — adds a new option; a fresh ID is assigned automatically. Omitting an existing ID — deletes that option. Always include every option you want to keep. Must be sent as JSON. Alternative format: instead of a key/value map you may also pass an array of objects in the same shape as the response: [{"id": "1", "value": "Red"}, {"id": "new-0", "value": "Orange"}]. The API will normalise this automatically.

        defaultvalue : typing.Optional[str]
            The default value (will be used in the absence of this field)

        in_form : typing.Optional[bool]
            Does this field occur in the subscription form? (boolean)

        in_list : typing.Optional[bool]
            Is this field visible in Laposta's overview? (boolean)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldEnvelope
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
            await client.fields.veld_wijzigen(
                field_id="field_id",
                list_id="BaImMu3JZA",
                required=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.veld_wijzigen(
            field_id,
            list_id=list_id,
            required=required,
            name=name,
            datatype=datatype,
            datatype_display=datatype_display,
            options_full=options_full,
            defaultvalue=defaultvalue,
            in_form=in_form,
            in_list=in_list,
            request_options=request_options,
        )
        return _response.data

    async def veld_verwijderen(
        self, field_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FieldEnvelope:
        """
        This permanently deletes a field. If the field does not exist, an error message is displayed. In response you are shown another field object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the field.

        Parameters
        ----------
        field_id : str
            The id of the field. You find it in the response of [Get all fields](/velden/alle-velden-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FieldEnvelope
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
            await client.fields.veld_verwijderen(
                field_id="Z87ysHha9A",
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.veld_verwijderen(field_id, list_id=list_id, request_options=request_options)
        return _response.data
