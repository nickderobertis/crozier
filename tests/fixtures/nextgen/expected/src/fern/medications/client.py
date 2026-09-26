

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok67 import Ok67
from ..types.ok68 import Ok68
from ..types.ok70 import Ok70
from ..types.ok73 import Ok73
from ..types.ok74 import Ok74
from ..types.ok75 import Ok75
from ..types.ok76 import Ok76
from .raw_client import AsyncRawMedicationsClient, RawMedicationsClient


OMIT = typing.cast(typing.Any, ...)


class MedicationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMedicationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMedicationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMedicationsClient
        """
        return self._raw_client

    def base_url_persons_charts_medications(
        self,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok67:
        """
        GETs medications created or modified within a given interval. If an oData filter of createTimestamp or modifyTimestamp is not specified, medications which are created or modified within the last 7 days are retrieved.

        Parameters
        ----------
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
        Ok67
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_charts_medications(
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_charts_medications(
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_medication_history(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok68:
        """
        Gets a list of medication history records for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose medication history is being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok68
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_person_id_medication_history(
            person_id="personId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_medication_history(
            person_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_medication_history_create_consent(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Creates medication history consent for a given person id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which medication history consent is being created

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
        client.medications.base_url_persons_person_id_medication_history_create_consent(
            person_id="personId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_medication_history_create_consent(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_medication_history_create_request(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Creates an medication history request for the given person id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which medication history is being requested

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
        client.medications.base_url_persons_person_id_medication_history_create_request(
            person_id="personId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_medication_history_create_request(
            person_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_medications(
        self,
        person_id: str,
        encounter_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok67:
        """
        Gets a list of patient medication for the specified person id and encounter id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose medications are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter for which the medications are retrieved

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
        Ok67
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications(
            person_id="personId",
            encounter_id="encounterId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_medications(
            person_id,
            encounter_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def post_base_url_persons_person_id_chart_encounters_encounter_id_medications(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a new medication for the given person id and encounter id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being added

        encounter_id : str
            (Required) (Required) The id of the encounter in which the medication is being added

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
        client.medications.post_base_url_persons_person_id_chart_encounters_encounter_id_medications(
            person_id="personId",
            encounter_id="encounterId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_medications(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data

    def get_base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
        self,
        person_id: str,
        encounter_id: str,
        medication_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok70:
        """
        Gets the patient medication details for the given person id, encounter id and patient medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient of whose medication is being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter for which the medication is being retrieved

        medication_id : str
            (Required) (Required) The id of the patient medication being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok70
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.get_base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
            person_id="personId",
            encounter_id="encounterId",
            medication_id="medicationId",
        )
        """
        _response = (
            self._raw_client.get_base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
                person_id, encounter_id, medication_id, request_options=request_options
            )
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id1(
        self,
        person_id: str,
        encounter_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient medication record for the given person id , encounter id and medication id Note: AcknowledgedProblems in prescription request object will be ignored because DUR check is not done while updating a medication. This field should not be set.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter in which the medication is being updated

        medication_id : str
            (Required) (Required) The unique id of the patient medication being updated

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
        client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id1(
            person_id="personId",
            encounter_id="encounterId",
            medication_id="medicationId",
            request={"key": "value"},
        )
        """
        _response = (
            self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id1(
                person_id, encounter_id, medication_id, request=request, request_options=request_options
            )
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
        self,
        person_id: str,
        encounter_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        deletes a medication for a given person id, encounter id and medication id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being deleted

        encounter_id : str
            (Required) (Required) The id of the encounter in which the medication is being deleted

        medication_id : str
            (Required) (Required) The id of the patient medication that is being deleted

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
        client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
            person_id="personId",
            encounter_id="encounterId",
            medication_id="medicationId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
            person_id, encounter_id, medication_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_renew(
        self,
        person_id: str,
        encounter_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Renews a medication for the given person id, encounter id and medication id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being added

        encounter_id : str
            (Required) (Required) The id of the encounter in which the medication is being added

        medication_id : str
            (Required) (Required) The id of the patient medication to be renewed

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
        client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_renew(
            person_id="personId",
            encounter_id="encounterId",
            medication_id="medicationId",
            request={"key": "value"},
        )
        """
        _response = (
            self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_renew(
                person_id, encounter_id, medication_id, request=request, request_options=request_options
            )
        )
        return _response.data

    def base_url_persons_person_id_chart_medications(
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
    ) -> Ok67:
        """
        Gets a list of patient medications for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose medications are being retrieved

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
        Ok67
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_person_id_chart_medications(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications(
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

    def base_url_persons_person_id_chart_medications_medication_id(
        self, person_id: str, medication_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok70:
        """
        Gets the patient medication details for the given person id and patient medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose medication is being retrieved

        medication_id : str
            (Required) (Required) The id of the patient medication being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok70
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_person_id_chart_medications_medication_id(
            person_id="personId",
            medication_id="medicationId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_medication_id(
            person_id, medication_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_medications_medication_id_cancel(
        self, person_id: str, medication_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Cancels a medication for the given person id and medication id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being cancelled

        medication_id : str
            (Required) (Required) The id of the patient medication that is being cancelled

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
        client.medications.base_url_persons_person_id_chart_medications_medication_id_cancel(
            person_id="personId",
            medication_id="medicationId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_medication_id_cancel(
            person_id, medication_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_medications_medication_id_notes(
        self,
        person_id: str,
        medication_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok73:
        """
        Returns a list of prescription notes for the specified person id and medication id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose prescription notes is being retrieved.

        medication_id : str
            (Required) (Required) The id of the patient medication whose prescription notes is being retrieved.

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
        Ok73
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_person_id_chart_medications_medication_id_notes(
            person_id="personId",
            medication_id="medicationId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_medication_id_notes(
            person_id,
            medication_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def post_base_url_persons_person_id_chart_medications_medication_id_notes(
        self,
        person_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a prescription note for the given person id and medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which a prescription note is being added.

        medication_id : str
            (Required) (Required) The id of the patient medication for which a prescription note is being added.

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
        client.medications.post_base_url_persons_person_id_chart_medications_medication_id_notes(
            person_id="personId",
            medication_id="medicationId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_medications_medication_id_notes(
            person_id, medication_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_medications_medication_id_notes_note_id1(
        self,
        person_id: str,
        medication_id: str,
        note_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok74:
        """
        Gets the prescription note for the given person id, patient medication id and note id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose prescription note is being retrieved

        medication_id : str
            (Required) (Required) The id of the patient medication whose prescription note is being retrieved

        note_id : str
            (Required) (Required) The id of the prescription note being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok74
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_person_id_chart_medications_medication_id_notes_note_id1(
            person_id="personId",
            medication_id="medicationId",
            note_id="noteId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_medication_id_notes_note_id1(
            person_id, medication_id, note_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
        self,
        person_id: str,
        medication_id: str,
        note_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update the specified prescription note for the person id and medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose prescription note is to be updated.

        medication_id : str
            (Required) (Required) The id of the medication whose prescription note is to be updated.

        note_id : str
            (Required) (Required) The id of the prescription note to be updated.

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
        client.medications.put_base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
            person_id="personId",
            medication_id="medicationId",
            note_id="noteId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
            person_id, medication_id, note_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
        self,
        person_id: str,
        medication_id: str,
        note_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified prescription note for the person id and medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose prescription note is to be deleted.

        medication_id : str
            (Required) (Required) The id of the medication whose prescription note is to be deleted.

        note_id : str
            (Required) (Required) The id of the prescription note to be deleted.

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
        client.medications.base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
            person_id="personId",
            medication_id="medicationId",
            note_id="noteId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
            person_id, medication_id, note_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_medications_medication_id_send_erx(
        self,
        person_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Submits an electronic prescription for the given person id, medication id, and additional details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient for which the medication is being electronically prescribed

        medication_id : str
            (Required) (Required) The id of the patient medication that is being electronically prescribed

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
        client.medications.base_url_persons_person_id_chart_medications_medication_id_send_erx(
            person_id="personId",
            medication_id="medicationId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_medication_id_send_erx(
            person_id, medication_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_medications_medication_id_stop(
        self,
        person_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Stops a medication for the given person id and medication id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being stopped

        medication_id : str
            (Required) (Required) The id of the patient medication that is being stopped

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
        client.medications.base_url_persons_person_id_chart_medications_medication_id_stop(
            person_id="personId",
            medication_id="medicationId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_medication_id_stop(
            person_id, medication_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_medications_medid_dur_check(
        self,
        person_id: str,
        medid: str,
        *,
        is_representative_ndc: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Performs a drug utilization review and returns any problems for the given person id and medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which a drug utilization review is being performed

        medid : str
            (Required) (Required) The id of the medication for which a drug utilization review is being performed

        is_representative_ndc : str
            A true or false value that represents whether the medication was prescribed elsewhere and the strength, route, and form were unknown at the time the medication was added

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_person_id_chart_medications_medid_dur_check(
            person_id="personId",
            medid="medid",
            is_representative_ndc="isRepresentativeNdc",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_medid_dur_check(
            person_id, medid, is_representative_ndc=is_representative_ndc, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_medications_medid_monograph_data(
        self, person_id: str, medid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok75:
        """
        Get the monograph data for a medication.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for monograph data

        medid : str
            (Required) (Required) The id of the medication for monograph data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok75
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_person_id_chart_medications_medid_monograph_data(
            person_id="personId",
            medid="medid",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_medid_monograph_data(
            person_id, medid, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_medications_medid_patient_education(
        self,
        person_id: str,
        medid: str,
        *,
        resource_type: str,
        encounter_date: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok76:
        """
        Get the external resources URL and type for patient education.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom patient education url is being retreived

        medid : str
            (Required) (Required) The id of the medication for patient education

        resource_type : str
            (Required) Patient education Resource Type - resourceType - 1 (ExternalPatientEducation) or 2 - (ClinicalDecisionSupport) or 3 - (ExternalProviderReferences)

        encounter_date : str
            Encounter Date on which patient education data is being retreived

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok76
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_person_id_chart_medications_medid_patient_education(
            person_id="personId",
            medid="medid",
            resource_type="resourceType",
            encounter_date="encounterDate",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_medid_patient_education(
            person_id,
            medid,
            resource_type=resource_type,
            encounter_date=encounter_date,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_medications_pdmp_report(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok67:
        """
        Get PDMP report for a person.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose medications are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok67
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.medications.base_url_persons_person_id_chart_medications_pdmp_report(
            person_id="personId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_medications_pdmp_report(
            person_id, request_options=request_options
        )
        return _response.data


class AsyncMedicationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMedicationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMedicationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMedicationsClient
        """
        return self._raw_client

    async def base_url_persons_charts_medications(
        self,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok67:
        """
        GETs medications created or modified within a given interval. If an oData filter of createTimestamp or modifyTimestamp is not specified, medications which are created or modified within the last 7 days are retrieved.

        Parameters
        ----------
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
        Ok67
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_charts_medications(
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_charts_medications(
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_medication_history(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok68:
        """
        Gets a list of medication history records for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose medication history is being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok68
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_person_id_medication_history(
                person_id="personId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_medication_history(
            person_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_medication_history_create_consent(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Creates medication history consent for a given person id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which medication history consent is being created

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
            await client.medications.base_url_persons_person_id_medication_history_create_consent(
                person_id="personId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_medication_history_create_consent(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_medication_history_create_request(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Creates an medication history request for the given person id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which medication history is being requested

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
            await client.medications.base_url_persons_person_id_medication_history_create_request(
                person_id="personId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_medication_history_create_request(
            person_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_medications(
        self,
        person_id: str,
        encounter_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok67:
        """
        Gets a list of patient medication for the specified person id and encounter id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose medications are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter for which the medications are retrieved

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
        Ok67
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications(
                person_id="personId",
                encounter_id="encounterId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_medications(
            person_id,
            encounter_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_encounters_encounter_id_medications(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a new medication for the given person id and encounter id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being added

        encounter_id : str
            (Required) (Required) The id of the encounter in which the medication is being added

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
            await client.medications.post_base_url_persons_person_id_chart_encounters_encounter_id_medications(
                person_id="personId",
                encounter_id="encounterId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_medications(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
        self,
        person_id: str,
        encounter_id: str,
        medication_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok70:
        """
        Gets the patient medication details for the given person id, encounter id and patient medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient of whose medication is being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter for which the medication is being retrieved

        medication_id : str
            (Required) (Required) The id of the patient medication being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok70
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.get_base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
                person_id="personId",
                encounter_id="encounterId",
                medication_id="medicationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
            person_id, encounter_id, medication_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id1(
        self,
        person_id: str,
        encounter_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient medication record for the given person id , encounter id and medication id Note: AcknowledgedProblems in prescription request object will be ignored because DUR check is not done while updating a medication. This field should not be set.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter in which the medication is being updated

        medication_id : str
            (Required) (Required) The unique id of the patient medication being updated

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
            await client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id1(
                person_id="personId",
                encounter_id="encounterId",
                medication_id="medicationId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id1(
                person_id, encounter_id, medication_id, request=request, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
        self,
        person_id: str,
        encounter_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        deletes a medication for a given person id, encounter id and medication id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being deleted

        encounter_id : str
            (Required) (Required) The id of the encounter in which the medication is being deleted

        medication_id : str
            (Required) (Required) The id of the patient medication that is being deleted

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
            await client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
                person_id="personId",
                encounter_id="encounterId",
                medication_id="medicationId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id(
                person_id, encounter_id, medication_id, request=request, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_renew(
        self,
        person_id: str,
        encounter_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Renews a medication for the given person id, encounter id and medication id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being added

        encounter_id : str
            (Required) (Required) The id of the encounter in which the medication is being added

        medication_id : str
            (Required) (Required) The id of the patient medication to be renewed

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
            await client.medications.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_renew(
                person_id="personId",
                encounter_id="encounterId",
                medication_id="medicationId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_renew(
            person_id, encounter_id, medication_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications(
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
    ) -> Ok67:
        """
        Gets a list of patient medications for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose medications are being retrieved

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
        Ok67
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_person_id_chart_medications(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_medications(
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

    async def base_url_persons_person_id_chart_medications_medication_id(
        self, person_id: str, medication_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok70:
        """
        Gets the patient medication details for the given person id and patient medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose medication is being retrieved

        medication_id : str
            (Required) (Required) The id of the patient medication being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok70
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_person_id_chart_medications_medication_id(
                person_id="personId",
                medication_id="medicationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_medication_id(
            person_id, medication_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications_medication_id_cancel(
        self, person_id: str, medication_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Cancels a medication for the given person id and medication id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being cancelled

        medication_id : str
            (Required) (Required) The id of the patient medication that is being cancelled

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
            await client.medications.base_url_persons_person_id_chart_medications_medication_id_cancel(
                person_id="personId",
                medication_id="medicationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_medication_id_cancel(
            person_id, medication_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications_medication_id_notes(
        self,
        person_id: str,
        medication_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok73:
        """
        Returns a list of prescription notes for the specified person id and medication id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose prescription notes is being retrieved.

        medication_id : str
            (Required) (Required) The id of the patient medication whose prescription notes is being retrieved.

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
        Ok73
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_person_id_chart_medications_medication_id_notes(
                person_id="personId",
                medication_id="medicationId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_medication_id_notes(
            person_id,
            medication_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_medications_medication_id_notes(
        self,
        person_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a prescription note for the given person id and medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which a prescription note is being added.

        medication_id : str
            (Required) (Required) The id of the patient medication for which a prescription note is being added.

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
            await client.medications.post_base_url_persons_person_id_chart_medications_medication_id_notes(
                person_id="personId",
                medication_id="medicationId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_medications_medication_id_notes(
            person_id, medication_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications_medication_id_notes_note_id1(
        self,
        person_id: str,
        medication_id: str,
        note_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok74:
        """
        Gets the prescription note for the given person id, patient medication id and note id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose prescription note is being retrieved

        medication_id : str
            (Required) (Required) The id of the patient medication whose prescription note is being retrieved

        note_id : str
            (Required) (Required) The id of the prescription note being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok74
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_person_id_chart_medications_medication_id_notes_note_id1(
                person_id="personId",
                medication_id="medicationId",
                note_id="noteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_medication_id_notes_note_id1(
            person_id, medication_id, note_id, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
        self,
        person_id: str,
        medication_id: str,
        note_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update the specified prescription note for the person id and medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose prescription note is to be updated.

        medication_id : str
            (Required) (Required) The id of the medication whose prescription note is to be updated.

        note_id : str
            (Required) (Required) The id of the prescription note to be updated.

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
            await client.medications.put_base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
                person_id="personId",
                medication_id="medicationId",
                note_id="noteId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
            person_id, medication_id, note_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
        self,
        person_id: str,
        medication_id: str,
        note_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete the specified prescription note for the person id and medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose prescription note is to be deleted.

        medication_id : str
            (Required) (Required) The id of the medication whose prescription note is to be deleted.

        note_id : str
            (Required) (Required) The id of the prescription note to be deleted.

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
            await client.medications.base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
                person_id="personId",
                medication_id="medicationId",
                note_id="noteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_medication_id_notes_note_id(
            person_id, medication_id, note_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications_medication_id_send_erx(
        self,
        person_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Submits an electronic prescription for the given person id, medication id, and additional details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient for which the medication is being electronically prescribed

        medication_id : str
            (Required) (Required) The id of the patient medication that is being electronically prescribed

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
            await client.medications.base_url_persons_person_id_chart_medications_medication_id_send_erx(
                person_id="personId",
                medication_id="medicationId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_medication_id_send_erx(
            person_id, medication_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications_medication_id_stop(
        self,
        person_id: str,
        medication_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Stops a medication for the given person id and medication id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which the medication is being stopped

        medication_id : str
            (Required) (Required) The id of the patient medication that is being stopped

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
            await client.medications.base_url_persons_person_id_chart_medications_medication_id_stop(
                person_id="personId",
                medication_id="medicationId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_medication_id_stop(
            person_id, medication_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications_medid_dur_check(
        self,
        person_id: str,
        medid: str,
        *,
        is_representative_ndc: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Performs a drug utilization review and returns any problems for the given person id and medication id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for which a drug utilization review is being performed

        medid : str
            (Required) (Required) The id of the medication for which a drug utilization review is being performed

        is_representative_ndc : str
            A true or false value that represents whether the medication was prescribed elsewhere and the strength, route, and form were unknown at the time the medication was added

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
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_person_id_chart_medications_medid_dur_check(
                person_id="personId",
                medid="medid",
                is_representative_ndc="isRepresentativeNdc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_medid_dur_check(
            person_id, medid, is_representative_ndc=is_representative_ndc, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications_medid_monograph_data(
        self, person_id: str, medid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok75:
        """
        Get the monograph data for a medication.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for monograph data

        medid : str
            (Required) (Required) The id of the medication for monograph data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok75
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_person_id_chart_medications_medid_monograph_data(
                person_id="personId",
                medid="medid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_medid_monograph_data(
            person_id, medid, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications_medid_patient_education(
        self,
        person_id: str,
        medid: str,
        *,
        resource_type: str,
        encounter_date: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok76:
        """
        Get the external resources URL and type for patient education.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person for whom patient education url is being retreived

        medid : str
            (Required) (Required) The id of the medication for patient education

        resource_type : str
            (Required) Patient education Resource Type - resourceType - 1 (ExternalPatientEducation) or 2 - (ClinicalDecisionSupport) or 3 - (ExternalProviderReferences)

        encounter_date : str
            Encounter Date on which patient education data is being retreived

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok76
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_person_id_chart_medications_medid_patient_education(
                person_id="personId",
                medid="medid",
                resource_type="resourceType",
                encounter_date="encounterDate",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_medid_patient_education(
            person_id,
            medid,
            resource_type=resource_type,
            encounter_date=encounter_date,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_medications_pdmp_report(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok67:
        """
        Get PDMP report for a person.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose medications are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok67
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.medications.base_url_persons_person_id_chart_medications_pdmp_report(
                person_id="personId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_medications_pdmp_report(
            person_id, request_options=request_options
        )
        return _response.data
