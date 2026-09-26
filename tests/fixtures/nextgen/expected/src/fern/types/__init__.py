



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .acknowledged_problem import AcknowledgedProblem
    from .bad_request1 import BadRequest1
    from .base_url_persons_person_id_chart_care_team_members_care_team_member_id_request import (
        BaseUrlPersonsPersonIdChartCareTeamMembersCareTeamMemberIdRequest,
    )
    from .base_url_persons_person_id_chart_care_team_members_request import (
        BaseUrlPersonsPersonIdChartCareTeamMembersRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesAllergyIdReactionsReactionIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesAllergyIdReactionsRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesAllergyIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_allergies_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdOutcomesOutcomeIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdOutcomesRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdVisHistoriesRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_vis_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdVisHistoriesVisIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdWastedVaccinesRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_lab_orders_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdLabOrdersRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_renew_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsMedicationIdRenewRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsMedicationIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_request1 import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsMedicationIdRequest1,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_medications_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdProceduresProcedureIdRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_procedures_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdProceduresRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_vitals_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdVitalsRequest,
    )
    from .base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id_request import (
        BaseUrlPersonsPersonIdChartEncountersEncounterIdVitalsVitalsIdRequest,
    )
    from .base_url_persons_person_id_chart_immunizations_exclusions_exclusion_id_request import (
        BaseUrlPersonsPersonIdChartImmunizationsExclusionsExclusionIdRequest,
    )
    from .base_url_persons_person_id_chart_immunizations_exclusions_request import (
        BaseUrlPersonsPersonIdChartImmunizationsExclusionsRequest,
    )
    from .base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments_request import (
        BaseUrlPersonsPersonIdChartImmunizationsOrdersOrderIdTrackingCommentsRequest,
    )
    from .base_url_persons_person_id_chart_immunizations_series_completions_request import (
        BaseUrlPersonsPersonIdChartImmunizationsSeriesCompletionsRequest,
    )
    from .base_url_persons_person_id_chart_immunizations_series_completions_series_id_request import (
        BaseUrlPersonsPersonIdChartImmunizationsSeriesCompletionsSeriesIdRequest,
    )
    from .base_url_persons_person_id_chart_lab_orders_order_id_request import (
        BaseUrlPersonsPersonIdChartLabOrdersOrderIdRequest,
    )
    from .base_url_persons_person_id_chart_lab_orders_order_id_schedule_request import (
        BaseUrlPersonsPersonIdChartLabOrdersOrderIdScheduleRequest,
    )
    from .base_url_persons_person_id_chart_lab_orders_order_id_tests_request import (
        BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsRequest,
    )
    from .base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id_request import (
        BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdOrderEntryAnswersAnswerIdRequest,
    )
    from .base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_request import (
        BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdOrderEntryAnswersRequest,
    )
    from .base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_request import (
        BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdRequest,
    )
    from .base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_request import (
        BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdSuspectedDiagnosesRequest,
    )
    from .base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments_request import (
        BaseUrlPersonsPersonIdChartLabOrdersOrderIdTrackingCommentsRequest,
    )
    from .base_url_persons_person_id_chart_lab_panels_panel_id_request import (
        BaseUrlPersonsPersonIdChartLabPanelsPanelIdRequest,
    )
    from .base_url_persons_person_id_chart_lab_panels_panel_id_results_request import (
        BaseUrlPersonsPersonIdChartLabPanelsPanelIdResultsRequest,
    )
    from .base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number_request import (
        BaseUrlPersonsPersonIdChartLabPanelsPanelIdResultsSequenceNumberRequest,
    )
    from .base_url_persons_person_id_chart_lab_panels_request import BaseUrlPersonsPersonIdChartLabPanelsRequest
    from .base_url_persons_person_id_chart_medications_medication_id_notes_note_id_request import (
        BaseUrlPersonsPersonIdChartMedicationsMedicationIdNotesNoteIdRequest,
    )
    from .base_url_persons_person_id_chart_medications_medication_id_notes_request import (
        BaseUrlPersonsPersonIdChartMedicationsMedicationIdNotesRequest,
    )
    from .base_url_persons_person_id_chart_medications_medication_id_send_erx_request import (
        BaseUrlPersonsPersonIdChartMedicationsMedicationIdSendErxRequest,
    )
    from .base_url_persons_person_id_chart_medications_medication_id_stop_request import (
        BaseUrlPersonsPersonIdChartMedicationsMedicationIdStopRequest,
    )
    from .base_url_persons_person_id_chart_problems_problem_id_notes_note_id_request import (
        BaseUrlPersonsPersonIdChartProblemsProblemIdNotesNoteIdRequest,
    )
    from .base_url_persons_person_id_chart_problems_problem_id_notes_request import (
        BaseUrlPersonsPersonIdChartProblemsProblemIdNotesRequest,
    )
    from .base_url_persons_person_id_chart_problems_problem_id_request import (
        BaseUrlPersonsPersonIdChartProblemsProblemIdRequest,
    )
    from .base_url_persons_person_id_chart_problems_request import BaseUrlPersonsPersonIdChartProblemsRequest
    from .base_url_persons_person_id_medication_history_create_consent_request import (
        BaseUrlPersonsPersonIdMedicationHistoryCreateConsentRequest,
    )
    from .base_url_persons_person_id_request import BaseUrlPersonsPersonIdRequest
    from .base_url_persons_request import BaseUrlPersonsRequest
    from .forbidden1 import Forbidden1
    from .interaction import Interaction
    from .item import Item
    from .item10 import Item10
    from .item11 import Item11
    from .item12 import Item12
    from .item14 import Item14
    from .item15 import Item15
    from .item16 import Item16
    from .item17 import Item17
    from .item18 import Item18
    from .item2 import Item2
    from .item20 import Item20
    from .item21 import Item21
    from .item22 import Item22
    from .item23 import Item23
    from .item24 import Item24
    from .item25 import Item25
    from .item26 import Item26
    from .item27 import Item27
    from .item28 import Item28
    from .item29 import Item29
    from .item3 import Item3
    from .item32 import Item32
    from .item34 import Item34
    from .item36 import Item36
    from .item37 import Item37
    from .item38 import Item38
    from .item39 import Item39
    from .item40 import Item40
    from .item41 import Item41
    from .item5 import Item5
    from .item6 import Item6
    from .item7 import Item7
    from .item9 import Item9
    from .link import Link
    from .ok import Ok
    from .ok1 import Ok1
    from .ok10 import Ok10
    from .ok11 import Ok11
    from .ok12 import Ok12
    from .ok15 import Ok15
    from .ok16 import Ok16
    from .ok17 import Ok17
    from .ok19 import Ok19
    from .ok20 import Ok20
    from .ok21 import Ok21
    from .ok22 import Ok22
    from .ok23 import Ok23
    from .ok24 import Ok24
    from .ok25 import Ok25
    from .ok26 import Ok26
    from .ok28 import Ok28
    from .ok29 import Ok29
    from .ok30 import Ok30
    from .ok31 import Ok31
    from .ok32 import Ok32
    from .ok34 import Ok34
    from .ok35 import Ok35
    from .ok36 import Ok36
    from .ok37 import Ok37
    from .ok38 import Ok38
    from .ok39 import Ok39
    from .ok4 import Ok4
    from .ok40 import Ok40
    from .ok41 import Ok41
    from .ok42 import Ok42
    from .ok43 import Ok43
    from .ok44 import Ok44
    from .ok45 import Ok45
    from .ok46 import Ok46
    from .ok47 import Ok47
    from .ok49 import Ok49
    from .ok51 import Ok51
    from .ok52 import Ok52
    from .ok53 import Ok53
    from .ok54 import Ok54
    from .ok56 import Ok56
    from .ok57 import Ok57
    from .ok58 import Ok58
    from .ok59 import Ok59
    from .ok6 import Ok6
    from .ok60 import Ok60
    from .ok61 import Ok61
    from .ok63 import Ok63
    from .ok64 import Ok64
    from .ok65 import Ok65
    from .ok66 import Ok66
    from .ok67 import Ok67
    from .ok68 import Ok68
    from .ok7 import Ok7
    from .ok70 import Ok70
    from .ok73 import Ok73
    from .ok74 import Ok74
    from .ok75 import Ok75
    from .ok76 import Ok76
    from .ok78 import Ok78
    from .ok79 import Ok79
    from .ok8 import Ok8
    from .ok81 import Ok81
    from .ok83 import Ok83
    from .ok84 import Ok84
    from .ok86 import Ok86
    from .ok87 import Ok87
    from .ok89 import Ok89
    from .ok90 import Ok90
    from .ok92 import Ok92
    from .ok93 import Ok93
    from .ok94 import Ok94
    from .ok95 import Ok95
    from .ok96 import Ok96
    from .ok97 import Ok97
    from .ok98 import Ok98
_dynamic_imports: typing.Dict[str, str] = {
    "AcknowledgedProblem": ".acknowledged_problem",
    "BadRequest1": ".bad_request1",
    "BaseUrlPersonsPersonIdChartCareTeamMembersCareTeamMemberIdRequest": ".base_url_persons_person_id_chart_care_team_members_care_team_member_id_request",
    "BaseUrlPersonsPersonIdChartCareTeamMembersRequest": ".base_url_persons_person_id_chart_care_team_members_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesAllergyIdReactionsReactionIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesAllergyIdReactionsRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesAllergyIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_allergies_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdOutcomesOutcomeIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_outcome_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdOutcomesRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_outcomes_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_intervention_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_interventions_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_goal_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_goals_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdVisHistoriesRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdVisHistoriesVisIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_vis_histories_vis_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdWastedVaccinesRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_order_id_vaccines_vaccine_id_wasted_vaccines_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_immunizations_orders_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdLabOrdersRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_lab_orders_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsMedicationIdRenewRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_renew_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsMedicationIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsMedicationIdRequest1": ".base_url_persons_person_id_chart_encounters_encounter_id_medications_medication_id_request1",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_medications_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdProceduresProcedureIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdProceduresRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_procedures_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdVitalsRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_vitals_request",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdVitalsVitalsIdRequest": ".base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id_request",
    "BaseUrlPersonsPersonIdChartImmunizationsExclusionsExclusionIdRequest": ".base_url_persons_person_id_chart_immunizations_exclusions_exclusion_id_request",
    "BaseUrlPersonsPersonIdChartImmunizationsExclusionsRequest": ".base_url_persons_person_id_chart_immunizations_exclusions_request",
    "BaseUrlPersonsPersonIdChartImmunizationsOrdersOrderIdTrackingCommentsRequest": ".base_url_persons_person_id_chart_immunizations_orders_order_id_tracking_comments_request",
    "BaseUrlPersonsPersonIdChartImmunizationsSeriesCompletionsRequest": ".base_url_persons_person_id_chart_immunizations_series_completions_request",
    "BaseUrlPersonsPersonIdChartImmunizationsSeriesCompletionsSeriesIdRequest": ".base_url_persons_person_id_chart_immunizations_series_completions_series_id_request",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdRequest": ".base_url_persons_person_id_chart_lab_orders_order_id_request",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdScheduleRequest": ".base_url_persons_person_id_chart_lab_orders_order_id_schedule_request",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsRequest": ".base_url_persons_person_id_chart_lab_orders_order_id_tests_request",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdOrderEntryAnswersAnswerIdRequest": ".base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_answer_id_request",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdOrderEntryAnswersRequest": ".base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_order_entry_answers_request",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdRequest": ".base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_request",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdSuspectedDiagnosesRequest": ".base_url_persons_person_id_chart_lab_orders_order_id_tests_test_id_suspected_diagnoses_request",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTrackingCommentsRequest": ".base_url_persons_person_id_chart_lab_orders_order_id_tracking_comments_request",
    "BaseUrlPersonsPersonIdChartLabPanelsPanelIdRequest": ".base_url_persons_person_id_chart_lab_panels_panel_id_request",
    "BaseUrlPersonsPersonIdChartLabPanelsPanelIdResultsRequest": ".base_url_persons_person_id_chart_lab_panels_panel_id_results_request",
    "BaseUrlPersonsPersonIdChartLabPanelsPanelIdResultsSequenceNumberRequest": ".base_url_persons_person_id_chart_lab_panels_panel_id_results_sequence_number_request",
    "BaseUrlPersonsPersonIdChartLabPanelsRequest": ".base_url_persons_person_id_chart_lab_panels_request",
    "BaseUrlPersonsPersonIdChartMedicationsMedicationIdNotesNoteIdRequest": ".base_url_persons_person_id_chart_medications_medication_id_notes_note_id_request",
    "BaseUrlPersonsPersonIdChartMedicationsMedicationIdNotesRequest": ".base_url_persons_person_id_chart_medications_medication_id_notes_request",
    "BaseUrlPersonsPersonIdChartMedicationsMedicationIdSendErxRequest": ".base_url_persons_person_id_chart_medications_medication_id_send_erx_request",
    "BaseUrlPersonsPersonIdChartMedicationsMedicationIdStopRequest": ".base_url_persons_person_id_chart_medications_medication_id_stop_request",
    "BaseUrlPersonsPersonIdChartProblemsProblemIdNotesNoteIdRequest": ".base_url_persons_person_id_chart_problems_problem_id_notes_note_id_request",
    "BaseUrlPersonsPersonIdChartProblemsProblemIdNotesRequest": ".base_url_persons_person_id_chart_problems_problem_id_notes_request",
    "BaseUrlPersonsPersonIdChartProblemsProblemIdRequest": ".base_url_persons_person_id_chart_problems_problem_id_request",
    "BaseUrlPersonsPersonIdChartProblemsRequest": ".base_url_persons_person_id_chart_problems_request",
    "BaseUrlPersonsPersonIdMedicationHistoryCreateConsentRequest": ".base_url_persons_person_id_medication_history_create_consent_request",
    "BaseUrlPersonsPersonIdRequest": ".base_url_persons_person_id_request",
    "BaseUrlPersonsRequest": ".base_url_persons_request",
    "Forbidden1": ".forbidden1",
    "Interaction": ".interaction",
    "Item": ".item",
    "Item10": ".item10",
    "Item11": ".item11",
    "Item12": ".item12",
    "Item14": ".item14",
    "Item15": ".item15",
    "Item16": ".item16",
    "Item17": ".item17",
    "Item18": ".item18",
    "Item2": ".item2",
    "Item20": ".item20",
    "Item21": ".item21",
    "Item22": ".item22",
    "Item23": ".item23",
    "Item24": ".item24",
    "Item25": ".item25",
    "Item26": ".item26",
    "Item27": ".item27",
    "Item28": ".item28",
    "Item29": ".item29",
    "Item3": ".item3",
    "Item32": ".item32",
    "Item34": ".item34",
    "Item36": ".item36",
    "Item37": ".item37",
    "Item38": ".item38",
    "Item39": ".item39",
    "Item40": ".item40",
    "Item41": ".item41",
    "Item5": ".item5",
    "Item6": ".item6",
    "Item7": ".item7",
    "Item9": ".item9",
    "Link": ".link",
    "Ok": ".ok",
    "Ok1": ".ok1",
    "Ok10": ".ok10",
    "Ok11": ".ok11",
    "Ok12": ".ok12",
    "Ok15": ".ok15",
    "Ok16": ".ok16",
    "Ok17": ".ok17",
    "Ok19": ".ok19",
    "Ok20": ".ok20",
    "Ok21": ".ok21",
    "Ok22": ".ok22",
    "Ok23": ".ok23",
    "Ok24": ".ok24",
    "Ok25": ".ok25",
    "Ok26": ".ok26",
    "Ok28": ".ok28",
    "Ok29": ".ok29",
    "Ok30": ".ok30",
    "Ok31": ".ok31",
    "Ok32": ".ok32",
    "Ok34": ".ok34",
    "Ok35": ".ok35",
    "Ok36": ".ok36",
    "Ok37": ".ok37",
    "Ok38": ".ok38",
    "Ok39": ".ok39",
    "Ok4": ".ok4",
    "Ok40": ".ok40",
    "Ok41": ".ok41",
    "Ok42": ".ok42",
    "Ok43": ".ok43",
    "Ok44": ".ok44",
    "Ok45": ".ok45",
    "Ok46": ".ok46",
    "Ok47": ".ok47",
    "Ok49": ".ok49",
    "Ok51": ".ok51",
    "Ok52": ".ok52",
    "Ok53": ".ok53",
    "Ok54": ".ok54",
    "Ok56": ".ok56",
    "Ok57": ".ok57",
    "Ok58": ".ok58",
    "Ok59": ".ok59",
    "Ok6": ".ok6",
    "Ok60": ".ok60",
    "Ok61": ".ok61",
    "Ok63": ".ok63",
    "Ok64": ".ok64",
    "Ok65": ".ok65",
    "Ok66": ".ok66",
    "Ok67": ".ok67",
    "Ok68": ".ok68",
    "Ok7": ".ok7",
    "Ok70": ".ok70",
    "Ok73": ".ok73",
    "Ok74": ".ok74",
    "Ok75": ".ok75",
    "Ok76": ".ok76",
    "Ok78": ".ok78",
    "Ok79": ".ok79",
    "Ok8": ".ok8",
    "Ok81": ".ok81",
    "Ok83": ".ok83",
    "Ok84": ".ok84",
    "Ok86": ".ok86",
    "Ok87": ".ok87",
    "Ok89": ".ok89",
    "Ok90": ".ok90",
    "Ok92": ".ok92",
    "Ok93": ".ok93",
    "Ok94": ".ok94",
    "Ok95": ".ok95",
    "Ok96": ".ok96",
    "Ok97": ".ok97",
    "Ok98": ".ok98",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AcknowledgedProblem",
    "BadRequest1",
    "BaseUrlPersonsPersonIdChartCareTeamMembersCareTeamMemberIdRequest",
    "BaseUrlPersonsPersonIdChartCareTeamMembersRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesAllergyIdReactionsReactionIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesAllergyIdReactionsRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesAllergyIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdOutcomesOutcomeIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdOutcomesRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdVisHistoriesRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdVisHistoriesVisIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdWastedVaccinesRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdLabOrdersRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsMedicationIdRenewRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsMedicationIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsMedicationIdRequest1",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdMedicationsRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdProceduresProcedureIdRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdProceduresRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdVitalsRequest",
    "BaseUrlPersonsPersonIdChartEncountersEncounterIdVitalsVitalsIdRequest",
    "BaseUrlPersonsPersonIdChartImmunizationsExclusionsExclusionIdRequest",
    "BaseUrlPersonsPersonIdChartImmunizationsExclusionsRequest",
    "BaseUrlPersonsPersonIdChartImmunizationsOrdersOrderIdTrackingCommentsRequest",
    "BaseUrlPersonsPersonIdChartImmunizationsSeriesCompletionsRequest",
    "BaseUrlPersonsPersonIdChartImmunizationsSeriesCompletionsSeriesIdRequest",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdRequest",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdScheduleRequest",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsRequest",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdOrderEntryAnswersAnswerIdRequest",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdOrderEntryAnswersRequest",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdRequest",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTestsTestIdSuspectedDiagnosesRequest",
    "BaseUrlPersonsPersonIdChartLabOrdersOrderIdTrackingCommentsRequest",
    "BaseUrlPersonsPersonIdChartLabPanelsPanelIdRequest",
    "BaseUrlPersonsPersonIdChartLabPanelsPanelIdResultsRequest",
    "BaseUrlPersonsPersonIdChartLabPanelsPanelIdResultsSequenceNumberRequest",
    "BaseUrlPersonsPersonIdChartLabPanelsRequest",
    "BaseUrlPersonsPersonIdChartMedicationsMedicationIdNotesNoteIdRequest",
    "BaseUrlPersonsPersonIdChartMedicationsMedicationIdNotesRequest",
    "BaseUrlPersonsPersonIdChartMedicationsMedicationIdSendErxRequest",
    "BaseUrlPersonsPersonIdChartMedicationsMedicationIdStopRequest",
    "BaseUrlPersonsPersonIdChartProblemsProblemIdNotesNoteIdRequest",
    "BaseUrlPersonsPersonIdChartProblemsProblemIdNotesRequest",
    "BaseUrlPersonsPersonIdChartProblemsProblemIdRequest",
    "BaseUrlPersonsPersonIdChartProblemsRequest",
    "BaseUrlPersonsPersonIdMedicationHistoryCreateConsentRequest",
    "BaseUrlPersonsPersonIdRequest",
    "BaseUrlPersonsRequest",
    "Forbidden1",
    "Interaction",
    "Item",
    "Item10",
    "Item11",
    "Item12",
    "Item14",
    "Item15",
    "Item16",
    "Item17",
    "Item18",
    "Item2",
    "Item20",
    "Item21",
    "Item22",
    "Item23",
    "Item24",
    "Item25",
    "Item26",
    "Item27",
    "Item28",
    "Item29",
    "Item3",
    "Item32",
    "Item34",
    "Item36",
    "Item37",
    "Item38",
    "Item39",
    "Item40",
    "Item41",
    "Item5",
    "Item6",
    "Item7",
    "Item9",
    "Link",
    "Ok",
    "Ok1",
    "Ok10",
    "Ok11",
    "Ok12",
    "Ok15",
    "Ok16",
    "Ok17",
    "Ok19",
    "Ok20",
    "Ok21",
    "Ok22",
    "Ok23",
    "Ok24",
    "Ok25",
    "Ok26",
    "Ok28",
    "Ok29",
    "Ok30",
    "Ok31",
    "Ok32",
    "Ok34",
    "Ok35",
    "Ok36",
    "Ok37",
    "Ok38",
    "Ok39",
    "Ok4",
    "Ok40",
    "Ok41",
    "Ok42",
    "Ok43",
    "Ok44",
    "Ok45",
    "Ok46",
    "Ok47",
    "Ok49",
    "Ok51",
    "Ok52",
    "Ok53",
    "Ok54",
    "Ok56",
    "Ok57",
    "Ok58",
    "Ok59",
    "Ok6",
    "Ok60",
    "Ok61",
    "Ok63",
    "Ok64",
    "Ok65",
    "Ok66",
    "Ok67",
    "Ok68",
    "Ok7",
    "Ok70",
    "Ok73",
    "Ok74",
    "Ok75",
    "Ok76",
    "Ok78",
    "Ok79",
    "Ok8",
    "Ok81",
    "Ok83",
    "Ok84",
    "Ok86",
    "Ok87",
    "Ok89",
    "Ok90",
    "Ok92",
    "Ok93",
    "Ok94",
    "Ok95",
    "Ok96",
    "Ok97",
    "Ok98",
]
