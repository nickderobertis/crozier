

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok17 import Ok17
from ..types.ok19 import Ok19
from ..types.ok20 import Ok20
from ..types.ok21 import Ok21
from ..types.ok22 import Ok22
from ..types.ok23 import Ok23
from .raw_client import AsyncRawGoalsClient, RawGoalsClient


OMIT = typing.cast(typing.Any, ...)


class GoalsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGoalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGoalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGoalsClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_care_plan_goals(
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
    ) -> Ok17:
        """
        Gets a patient's care plan goals.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose goals are being fetched

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
        Ok17
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.goals.base_url_persons_person_id_chart_care_plan_goals(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_care_plan_goals(
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

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok17:
        """
        Gets a patient's care plan goals for a specified encounter and health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose goals are being fetched

        encounter_id : str
            (Required) (Required) The id of the patient encounter whose goals are being fetched

        health_concern_id : str
            (Required) (Required) The id of the health concern whose goals are being fetched

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
        Ok17
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
            person_id,
            encounter_id,
            health_concern_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Creates a new care plan goal for a patient for specified encounter and health concern

        Parameters
        ----------
        person_id : str
            (Required) (Required) id of the Patient

        encounter_id : str
            (Required) (Required) id of the encounter

        health_concern_id : str
            (Required) (Required) id of Health Concern

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
        client.goals.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
            person_id, encounter_id, health_concern_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id1(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok19:
        """
        Gets a patient's care plan goal details.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) The id of the goal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok19
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id1(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id1(
            person_id, encounter_id, health_concern_id, goal_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update patient's careplan goal.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) Encounter id of the patient

        health_concern_id : str
            (Required) (Required) Care plan health concern id of the patient

        goal_id : str
            (Required) (Required) Care plan goal id of the patient

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
        client.goals.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
            person_id, encounter_id, health_concern_id, goal_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a Care Plan Goal

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

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
        client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
            person_id, encounter_id, health_concern_id, goal_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok20:
        """
        Returns a list of interventions for the specified person id, encounter id, health concern id and goal id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose interventions are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter whose interventions are being retrieved

        health_concern_id : str
            (Required) (Required) The id of the health concern whose interventions are being retrieved

        goal_id : str
            (Required) (Required) The id of the goal whose interventions are being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok20
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Add new intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

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
        client.goals.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
            person_id, encounter_id, health_concern_id, goal_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id1(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok21:
        """
        Gets intervention details based on person id, encounter id, health concern id , goal id and intervention id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose intervention is being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter whose intervention is being retrieved

        health_concern_id : str
            (Required) (Required) The id of the health concern whose intervention is being retrieved

        goal_id : str
            (Required) (Required) The id of the goal whose intervention is being retrieved

        intervention_id : str
            (Required) (Required) The id of the intervention to be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok21
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id1(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            intervention_id="interventionId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id1(
            person_id, encounter_id, health_concern_id, goal_id, intervention_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) The id of the patient encounter.

        health_concern_id : str
            (Required) (Required) The id of the health concern.

        goal_id : str
            (Required) (Required) Care plan goal id of patient.

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient.

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
        client.goals.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            intervention_id="interventionId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete Patient intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) The id of the goal

        intervention_id : str
            (Required) (Required) The id of the intervention

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
        client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            intervention_id="interventionId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
            person_id, encounter_id, health_concern_id, goal_id, intervention_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok22:
        """
        Returns a list of care plan outcomes for the specified person, encounter, concern, and goal after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care plan outcomes are being retrieved

        encounter_id : str
            (Required) (Required) Encounter id for outcome

        health_concern_id : str
            (Required) (Required) Care plan health concern id of patient

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok22
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            intervention_id="interventionId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Add new outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

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
        client.goals.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            intervention_id="interventionId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        expand: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok23:
        """
        Gets the care plan outcome details for the given outcome id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care plan outcomes are being retrieved

        encounter_id : str
            (Required) (Required) Encounter id for outcome

        health_concern_id : str
            (Required) (Required) Care plan health concern id of patient

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

        outcome_id : str
            (Required) (Required) Care plan outcome id for patient

        expand : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok23
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.goals.get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            intervention_id="interventionId",
            outcome_id="outcomeId",
            expand="$expand",
        )
        """
        _response = self._raw_client.get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            outcome_id,
            expand=expand,
            request_options=request_options,
        )
        return _response.data

    def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) The id of the patient encounter.

        health_concern_id : str
            (Required) (Required) The id of the health concern.

        goal_id : str
            (Required) (Required) Care plan goal id of patient.

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient.

        outcome_id : str
            (Required) (Required) Care plan outcome id for patient.

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
        client.goals.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            intervention_id="interventionId",
            outcome_id="outcomeId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            outcome_id,
            request=request,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id of the patient

        outcome_id : str
            (Required) (Required) Care plan outcome of the patient

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
        client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            goal_id="goalId",
            intervention_id="interventionId",
            outcome_id="outcomeId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            outcome_id,
            request_options=request_options,
        )
        return _response.data


class AsyncGoalsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGoalsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGoalsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGoalsClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_care_plan_goals(
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
    ) -> Ok17:
        """
        Gets a patient's care plan goals.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose goals are being fetched

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
        Ok17
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.goals.base_url_persons_person_id_chart_care_plan_goals(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_care_plan_goals(
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

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok17:
        """
        Gets a patient's care plan goals for a specified encounter and health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose goals are being fetched

        encounter_id : str
            (Required) (Required) The id of the patient encounter whose goals are being fetched

        health_concern_id : str
            (Required) (Required) The id of the health concern whose goals are being fetched

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
        Ok17
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
            person_id,
            encounter_id,
            health_concern_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Creates a new care plan goal for a patient for specified encounter and health concern

        Parameters
        ----------
        person_id : str
            (Required) (Required) id of the Patient

        encounter_id : str
            (Required) (Required) id of the encounter

        health_concern_id : str
            (Required) (Required) id of Health Concern

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
            await client.goals.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals(
            person_id, encounter_id, health_concern_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id1(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok19:
        """
        Gets a patient's care plan goal details.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) The id of the goal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok19
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id1(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id1(
            person_id, encounter_id, health_concern_id, goal_id, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update patient's careplan goal.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) Encounter id of the patient

        health_concern_id : str
            (Required) (Required) Care plan health concern id of the patient

        goal_id : str
            (Required) (Required) Care plan goal id of the patient

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
            await client.goals.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
            person_id, encounter_id, health_concern_id, goal_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a Care Plan Goal

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

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
            await client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id(
            person_id, encounter_id, health_concern_id, goal_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok20:
        """
        Returns a list of interventions for the specified person id, encounter id, health concern id and goal id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose interventions are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter whose interventions are being retrieved

        health_concern_id : str
            (Required) (Required) The id of the health concern whose interventions are being retrieved

        goal_id : str
            (Required) (Required) The id of the goal whose interventions are being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok20
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Add new intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

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
            await client.goals.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions(
            person_id, encounter_id, health_concern_id, goal_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id1(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok21:
        """
        Gets intervention details based on person id, encounter id, health concern id , goal id and intervention id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose intervention is being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter whose intervention is being retrieved

        health_concern_id : str
            (Required) (Required) The id of the health concern whose intervention is being retrieved

        goal_id : str
            (Required) (Required) The id of the goal whose intervention is being retrieved

        intervention_id : str
            (Required) (Required) The id of the intervention to be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok21
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id1(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                intervention_id="interventionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id1(
            person_id, encounter_id, health_concern_id, goal_id, intervention_id, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) The id of the patient encounter.

        health_concern_id : str
            (Required) (Required) The id of the health concern.

        goal_id : str
            (Required) (Required) Care plan goal id of patient.

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient.

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
            await client.goals.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                intervention_id="interventionId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete Patient intervention details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) The id of the goal

        intervention_id : str
            (Required) (Required) The id of the intervention

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
            await client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                intervention_id="interventionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id(
            person_id, encounter_id, health_concern_id, goal_id, intervention_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok22:
        """
        Returns a list of care plan outcomes for the specified person, encounter, concern, and goal after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care plan outcomes are being retrieved

        encounter_id : str
            (Required) (Required) Encounter id for outcome

        health_concern_id : str
            (Required) (Required) Care plan health concern id of patient

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok22
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                intervention_id="interventionId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Add new outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

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
            await client.goals.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                intervention_id="interventionId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        expand: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok23:
        """
        Gets the care plan outcome details for the given outcome id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care plan outcomes are being retrieved

        encounter_id : str
            (Required) (Required) Encounter id for outcome

        health_concern_id : str
            (Required) (Required) Care plan health concern id of patient

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient

        outcome_id : str
            (Required) (Required) Care plan outcome id for patient

        expand : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok23
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.goals.get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                intervention_id="interventionId",
                outcome_id="outcomeId",
                expand="$expand",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            outcome_id,
            expand=expand,
            request_options=request_options,
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) The id of the patient encounter.

        health_concern_id : str
            (Required) (Required) The id of the health concern.

        goal_id : str
            (Required) (Required) Care plan goal id of patient.

        intervention_id : str
            (Required) (Required) Care plan intervention id for patient.

        outcome_id : str
            (Required) (Required) Care plan outcome id for patient.

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
            await client.goals.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                intervention_id="interventionId",
                outcome_id="outcomeId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            outcome_id,
            request=request,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        goal_id: str,
        intervention_id: str,
        outcome_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete outcome details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

        goal_id : str
            (Required) (Required) Care plan goal id of patient

        intervention_id : str
            (Required) (Required) Care plan intervention id of the patient

        outcome_id : str
            (Required) (Required) Care plan outcome of the patient

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
            await client.goals.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                goal_id="goalId",
                intervention_id="interventionId",
                outcome_id="outcomeId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id(
            person_id,
            encounter_id,
            health_concern_id,
            goal_id,
            intervention_id,
            outcome_id,
            request_options=request_options,
        )
        return _response.data
