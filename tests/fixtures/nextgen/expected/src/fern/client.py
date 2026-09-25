

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .allergies_and_intolerances.client import AllergiesAndIntolerancesClient, AsyncAllergiesAndIntolerancesClient
    from .assessment_and_plan_of_treatment.client import (
        AssessmentAndPlanOfTreatmentClient,
        AsyncAssessmentAndPlanOfTreatmentClient,
    )
    from .care_team_members.client import AsyncCareTeamMembersClient, CareTeamMembersClient
    from .clinical_notes.client import AsyncClinicalNotesClient, ClinicalNotesClient
    from .goals.client import AsyncGoalsClient, GoalsClient
    from .health_concerns.client import AsyncHealthConcernsClient, HealthConcernsClient
    from .immunizations.client import AsyncImmunizationsClient, ImmunizationsClient
    from .implantable_device_identifiers.client import (
        AsyncImplantableDeviceIdentifiersClient,
        ImplantableDeviceIdentifiersClient,
    )
    from .laboratory.client import AsyncLaboratoryClient, LaboratoryClient
    from .medications.client import AsyncMedicationsClient, MedicationsClient
    from .patient_demographics.client import AsyncPatientDemographicsClient, PatientDemographicsClient
    from .problems.client import AsyncProblemsClient, ProblemsClient
    from .procedures.client import AsyncProceduresClient, ProceduresClient
    from .smoking_status.client import AsyncSmokingStatusClient, SmokingStatusClient
    from .vital_signs.client import AsyncVitalSignsClient, VitalSignsClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    accept : typing.Optional[str]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        accept="YOUR_ACCEPT",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        accept: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            accept=accept,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._allergies_and_intolerances: typing.Optional[AllergiesAndIntolerancesClient] = None
        self._assessment_and_plan_of_treatment: typing.Optional[AssessmentAndPlanOfTreatmentClient] = None
        self._care_team_members: typing.Optional[CareTeamMembersClient] = None
        self._clinical_notes: typing.Optional[ClinicalNotesClient] = None
        self._goals: typing.Optional[GoalsClient] = None
        self._health_concerns: typing.Optional[HealthConcernsClient] = None
        self._immunizations: typing.Optional[ImmunizationsClient] = None
        self._implantable_device_identifiers: typing.Optional[ImplantableDeviceIdentifiersClient] = None
        self._laboratory: typing.Optional[LaboratoryClient] = None
        self._medications: typing.Optional[MedicationsClient] = None
        self._patient_demographics: typing.Optional[PatientDemographicsClient] = None
        self._problems: typing.Optional[ProblemsClient] = None
        self._procedures: typing.Optional[ProceduresClient] = None
        self._smoking_status: typing.Optional[SmokingStatusClient] = None
        self._vital_signs: typing.Optional[VitalSignsClient] = None

    @property
    def allergies_and_intolerances(self):
        if self._allergies_and_intolerances is None:
            from .allergies_and_intolerances.client import AllergiesAndIntolerancesClient

            self._allergies_and_intolerances = AllergiesAndIntolerancesClient(client_wrapper=self._client_wrapper)
        return self._allergies_and_intolerances

    @property
    def assessment_and_plan_of_treatment(self):
        if self._assessment_and_plan_of_treatment is None:
            from .assessment_and_plan_of_treatment.client import AssessmentAndPlanOfTreatmentClient

            self._assessment_and_plan_of_treatment = AssessmentAndPlanOfTreatmentClient(
                client_wrapper=self._client_wrapper
            )
        return self._assessment_and_plan_of_treatment

    @property
    def care_team_members(self):
        if self._care_team_members is None:
            from .care_team_members.client import CareTeamMembersClient

            self._care_team_members = CareTeamMembersClient(client_wrapper=self._client_wrapper)
        return self._care_team_members

    @property
    def clinical_notes(self):
        if self._clinical_notes is None:
            from .clinical_notes.client import ClinicalNotesClient

            self._clinical_notes = ClinicalNotesClient(client_wrapper=self._client_wrapper)
        return self._clinical_notes

    @property
    def goals(self):
        if self._goals is None:
            from .goals.client import GoalsClient

            self._goals = GoalsClient(client_wrapper=self._client_wrapper)
        return self._goals

    @property
    def health_concerns(self):
        if self._health_concerns is None:
            from .health_concerns.client import HealthConcernsClient

            self._health_concerns = HealthConcernsClient(client_wrapper=self._client_wrapper)
        return self._health_concerns

    @property
    def immunizations(self):
        if self._immunizations is None:
            from .immunizations.client import ImmunizationsClient

            self._immunizations = ImmunizationsClient(client_wrapper=self._client_wrapper)
        return self._immunizations

    @property
    def implantable_device_identifiers(self):
        if self._implantable_device_identifiers is None:
            from .implantable_device_identifiers.client import ImplantableDeviceIdentifiersClient

            self._implantable_device_identifiers = ImplantableDeviceIdentifiersClient(
                client_wrapper=self._client_wrapper
            )
        return self._implantable_device_identifiers

    @property
    def laboratory(self):
        if self._laboratory is None:
            from .laboratory.client import LaboratoryClient

            self._laboratory = LaboratoryClient(client_wrapper=self._client_wrapper)
        return self._laboratory

    @property
    def medications(self):
        if self._medications is None:
            from .medications.client import MedicationsClient

            self._medications = MedicationsClient(client_wrapper=self._client_wrapper)
        return self._medications

    @property
    def patient_demographics(self):
        if self._patient_demographics is None:
            from .patient_demographics.client import PatientDemographicsClient

            self._patient_demographics = PatientDemographicsClient(client_wrapper=self._client_wrapper)
        return self._patient_demographics

    @property
    def problems(self):
        if self._problems is None:
            from .problems.client import ProblemsClient

            self._problems = ProblemsClient(client_wrapper=self._client_wrapper)
        return self._problems

    @property
    def procedures(self):
        if self._procedures is None:
            from .procedures.client import ProceduresClient

            self._procedures = ProceduresClient(client_wrapper=self._client_wrapper)
        return self._procedures

    @property
    def smoking_status(self):
        if self._smoking_status is None:
            from .smoking_status.client import SmokingStatusClient

            self._smoking_status = SmokingStatusClient(client_wrapper=self._client_wrapper)
        return self._smoking_status

    @property
    def vital_signs(self):
        if self._vital_signs is None:
            from .vital_signs.client import VitalSignsClient

            self._vital_signs = VitalSignsClient(client_wrapper=self._client_wrapper)
        return self._vital_signs


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    accept : typing.Optional[str]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        accept="YOUR_ACCEPT",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        accept: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            accept=accept,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._allergies_and_intolerances: typing.Optional[AsyncAllergiesAndIntolerancesClient] = None
        self._assessment_and_plan_of_treatment: typing.Optional[AsyncAssessmentAndPlanOfTreatmentClient] = None
        self._care_team_members: typing.Optional[AsyncCareTeamMembersClient] = None
        self._clinical_notes: typing.Optional[AsyncClinicalNotesClient] = None
        self._goals: typing.Optional[AsyncGoalsClient] = None
        self._health_concerns: typing.Optional[AsyncHealthConcernsClient] = None
        self._immunizations: typing.Optional[AsyncImmunizationsClient] = None
        self._implantable_device_identifiers: typing.Optional[AsyncImplantableDeviceIdentifiersClient] = None
        self._laboratory: typing.Optional[AsyncLaboratoryClient] = None
        self._medications: typing.Optional[AsyncMedicationsClient] = None
        self._patient_demographics: typing.Optional[AsyncPatientDemographicsClient] = None
        self._problems: typing.Optional[AsyncProblemsClient] = None
        self._procedures: typing.Optional[AsyncProceduresClient] = None
        self._smoking_status: typing.Optional[AsyncSmokingStatusClient] = None
        self._vital_signs: typing.Optional[AsyncVitalSignsClient] = None

    @property
    def allergies_and_intolerances(self):
        if self._allergies_and_intolerances is None:
            from .allergies_and_intolerances.client import AsyncAllergiesAndIntolerancesClient

            self._allergies_and_intolerances = AsyncAllergiesAndIntolerancesClient(client_wrapper=self._client_wrapper)
        return self._allergies_and_intolerances

    @property
    def assessment_and_plan_of_treatment(self):
        if self._assessment_and_plan_of_treatment is None:
            from .assessment_and_plan_of_treatment.client import AsyncAssessmentAndPlanOfTreatmentClient

            self._assessment_and_plan_of_treatment = AsyncAssessmentAndPlanOfTreatmentClient(
                client_wrapper=self._client_wrapper
            )
        return self._assessment_and_plan_of_treatment

    @property
    def care_team_members(self):
        if self._care_team_members is None:
            from .care_team_members.client import AsyncCareTeamMembersClient

            self._care_team_members = AsyncCareTeamMembersClient(client_wrapper=self._client_wrapper)
        return self._care_team_members

    @property
    def clinical_notes(self):
        if self._clinical_notes is None:
            from .clinical_notes.client import AsyncClinicalNotesClient

            self._clinical_notes = AsyncClinicalNotesClient(client_wrapper=self._client_wrapper)
        return self._clinical_notes

    @property
    def goals(self):
        if self._goals is None:
            from .goals.client import AsyncGoalsClient

            self._goals = AsyncGoalsClient(client_wrapper=self._client_wrapper)
        return self._goals

    @property
    def health_concerns(self):
        if self._health_concerns is None:
            from .health_concerns.client import AsyncHealthConcernsClient

            self._health_concerns = AsyncHealthConcernsClient(client_wrapper=self._client_wrapper)
        return self._health_concerns

    @property
    def immunizations(self):
        if self._immunizations is None:
            from .immunizations.client import AsyncImmunizationsClient

            self._immunizations = AsyncImmunizationsClient(client_wrapper=self._client_wrapper)
        return self._immunizations

    @property
    def implantable_device_identifiers(self):
        if self._implantable_device_identifiers is None:
            from .implantable_device_identifiers.client import AsyncImplantableDeviceIdentifiersClient

            self._implantable_device_identifiers = AsyncImplantableDeviceIdentifiersClient(
                client_wrapper=self._client_wrapper
            )
        return self._implantable_device_identifiers

    @property
    def laboratory(self):
        if self._laboratory is None:
            from .laboratory.client import AsyncLaboratoryClient

            self._laboratory = AsyncLaboratoryClient(client_wrapper=self._client_wrapper)
        return self._laboratory

    @property
    def medications(self):
        if self._medications is None:
            from .medications.client import AsyncMedicationsClient

            self._medications = AsyncMedicationsClient(client_wrapper=self._client_wrapper)
        return self._medications

    @property
    def patient_demographics(self):
        if self._patient_demographics is None:
            from .patient_demographics.client import AsyncPatientDemographicsClient

            self._patient_demographics = AsyncPatientDemographicsClient(client_wrapper=self._client_wrapper)
        return self._patient_demographics

    @property
    def problems(self):
        if self._problems is None:
            from .problems.client import AsyncProblemsClient

            self._problems = AsyncProblemsClient(client_wrapper=self._client_wrapper)
        return self._problems

    @property
    def procedures(self):
        if self._procedures is None:
            from .procedures.client import AsyncProceduresClient

            self._procedures = AsyncProceduresClient(client_wrapper=self._client_wrapper)
        return self._procedures

    @property
    def smoking_status(self):
        if self._smoking_status is None:
            from .smoking_status.client import AsyncSmokingStatusClient

            self._smoking_status = AsyncSmokingStatusClient(client_wrapper=self._client_wrapper)
        return self._smoking_status

    @property
    def vital_signs(self):
        if self._vital_signs is None:
            from .vital_signs.client import AsyncVitalSignsClient

            self._vital_signs = AsyncVitalSignsClient(client_wrapper=self._client_wrapper)
        return self._vital_signs


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
