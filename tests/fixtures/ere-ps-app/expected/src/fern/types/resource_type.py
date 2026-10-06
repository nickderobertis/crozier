

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResourceType(enum.StrEnum):
    ACCOUNT = "Account"
    ACTIVITY_DEFINITION = "ActivityDefinition"
    ADVERSE_EVENT = "AdverseEvent"
    ALLERGY_INTOLERANCE = "AllergyIntolerance"
    APPOINTMENT = "Appointment"
    APPOINTMENT_RESPONSE = "AppointmentResponse"
    AUDIT_EVENT = "AuditEvent"
    BASIC = "Basic"
    BINARY = "Binary"
    BIOLOGICALLY_DERIVED_PRODUCT = "BiologicallyDerivedProduct"
    BODY_STRUCTURE = "BodyStructure"
    BUNDLE = "Bundle"
    CAPABILITY_STATEMENT = "CapabilityStatement"
    CARE_PLAN = "CarePlan"
    CARE_TEAM = "CareTeam"
    CATALOG_ENTRY = "CatalogEntry"
    CHARGE_ITEM = "ChargeItem"
    CHARGE_ITEM_DEFINITION = "ChargeItemDefinition"
    CLAIM = "Claim"
    CLAIM_RESPONSE = "ClaimResponse"
    CLINICAL_IMPRESSION = "ClinicalImpression"
    CODE_SYSTEM = "CodeSystem"
    COMMUNICATION = "Communication"
    COMMUNICATION_REQUEST = "CommunicationRequest"
    COMPARTMENT_DEFINITION = "CompartmentDefinition"
    COMPOSITION = "Composition"
    CONCEPT_MAP = "ConceptMap"
    CONDITION = "Condition"
    CONSENT = "Consent"
    CONTRACT = "Contract"
    COVERAGE = "Coverage"
    COVERAGE_ELIGIBILITY_REQUEST = "CoverageEligibilityRequest"
    COVERAGE_ELIGIBILITY_RESPONSE = "CoverageEligibilityResponse"
    DETECTED_ISSUE = "DetectedIssue"
    DEVICE = "Device"
    DEVICE_DEFINITION = "DeviceDefinition"
    DEVICE_METRIC = "DeviceMetric"
    DEVICE_REQUEST = "DeviceRequest"
    DEVICE_USE_STATEMENT = "DeviceUseStatement"
    DIAGNOSTIC_REPORT = "DiagnosticReport"
    DOCUMENT_MANIFEST = "DocumentManifest"
    DOCUMENT_REFERENCE = "DocumentReference"
    EFFECT_EVIDENCE_SYNTHESIS = "EffectEvidenceSynthesis"
    ENCOUNTER = "Encounter"
    ENDPOINT = "Endpoint"
    ENROLLMENT_REQUEST = "EnrollmentRequest"
    ENROLLMENT_RESPONSE = "EnrollmentResponse"
    EPISODE_OF_CARE = "EpisodeOfCare"
    EVENT_DEFINITION = "EventDefinition"
    EVIDENCE = "Evidence"
    EVIDENCE_VARIABLE = "EvidenceVariable"
    EXAMPLE_SCENARIO = "ExampleScenario"
    EXPLANATION_OF_BENEFIT = "ExplanationOfBenefit"
    FAMILY_MEMBER_HISTORY = "FamilyMemberHistory"
    FLAG = "Flag"
    GOAL = "Goal"
    GRAPH_DEFINITION = "GraphDefinition"
    GROUP = "Group"
    GUIDANCE_RESPONSE = "GuidanceResponse"
    HEALTHCARE_SERVICE = "HealthcareService"
    IMAGING_STUDY = "ImagingStudy"
    IMMUNIZATION = "Immunization"
    IMMUNIZATION_EVALUATION = "ImmunizationEvaluation"
    IMMUNIZATION_RECOMMENDATION = "ImmunizationRecommendation"
    IMPLEMENTATION_GUIDE = "ImplementationGuide"
    INSURANCE_PLAN = "InsurancePlan"
    INVOICE = "Invoice"
    LIBRARY = "Library"
    LINKAGE = "Linkage"
    LIST = "List"
    LOCATION = "Location"
    MEASURE = "Measure"
    MEASURE_REPORT = "MeasureReport"
    MEDIA = "Media"
    MEDICATION = "Medication"
    MEDICATION_ADMINISTRATION = "MedicationAdministration"
    MEDICATION_DISPENSE = "MedicationDispense"
    MEDICATION_KNOWLEDGE = "MedicationKnowledge"
    MEDICATION_REQUEST = "MedicationRequest"
    MEDICATION_STATEMENT = "MedicationStatement"
    MEDICINAL_PRODUCT = "MedicinalProduct"
    MEDICINAL_PRODUCT_AUTHORIZATION = "MedicinalProductAuthorization"
    MEDICINAL_PRODUCT_CONTRAINDICATION = "MedicinalProductContraindication"
    MEDICINAL_PRODUCT_INDICATION = "MedicinalProductIndication"
    MEDICINAL_PRODUCT_INGREDIENT = "MedicinalProductIngredient"
    MEDICINAL_PRODUCT_INTERACTION = "MedicinalProductInteraction"
    MEDICINAL_PRODUCT_MANUFACTURED = "MedicinalProductManufactured"
    MEDICINAL_PRODUCT_PACKAGED = "MedicinalProductPackaged"
    MEDICINAL_PRODUCT_PHARMACEUTICAL = "MedicinalProductPharmaceutical"
    MEDICINAL_PRODUCT_UNDESIRABLE_EFFECT = "MedicinalProductUndesirableEffect"
    MESSAGE_DEFINITION = "MessageDefinition"
    MESSAGE_HEADER = "MessageHeader"
    MOLECULAR_SEQUENCE = "MolecularSequence"
    NAMING_SYSTEM = "NamingSystem"
    NUTRITION_ORDER = "NutritionOrder"
    OBSERVATION = "Observation"
    OBSERVATION_DEFINITION = "ObservationDefinition"
    OPERATION_DEFINITION = "OperationDefinition"
    OPERATION_OUTCOME = "OperationOutcome"
    ORGANIZATION = "Organization"
    ORGANIZATION_AFFILIATION = "OrganizationAffiliation"
    PARAMETERS = "Parameters"
    PATIENT = "Patient"
    PAYMENT_NOTICE = "PaymentNotice"
    PAYMENT_RECONCILIATION = "PaymentReconciliation"
    PERSON = "Person"
    PLAN_DEFINITION = "PlanDefinition"
    PRACTITIONER = "Practitioner"
    PRACTITIONER_ROLE = "PractitionerRole"
    PROCEDURE = "Procedure"
    PROVENANCE = "Provenance"
    QUESTIONNAIRE = "Questionnaire"
    QUESTIONNAIRE_RESPONSE = "QuestionnaireResponse"
    RELATED_PERSON = "RelatedPerson"
    REQUEST_GROUP = "RequestGroup"
    RESEARCH_DEFINITION = "ResearchDefinition"
    RESEARCH_ELEMENT_DEFINITION = "ResearchElementDefinition"
    RESEARCH_STUDY = "ResearchStudy"
    RESEARCH_SUBJECT = "ResearchSubject"
    RISK_ASSESSMENT = "RiskAssessment"
    RISK_EVIDENCE_SYNTHESIS = "RiskEvidenceSynthesis"
    SCHEDULE = "Schedule"
    SEARCH_PARAMETER = "SearchParameter"
    SERVICE_REQUEST = "ServiceRequest"
    SLOT = "Slot"
    SPECIMEN = "Specimen"
    SPECIMEN_DEFINITION = "SpecimenDefinition"
    STRUCTURE_DEFINITION = "StructureDefinition"
    STRUCTURE_MAP = "StructureMap"
    SUBSCRIPTION = "Subscription"
    SUBSTANCE = "Substance"
    SUBSTANCE_NUCLEIC_ACID = "SubstanceNucleicAcid"
    SUBSTANCE_POLYMER = "SubstancePolymer"
    SUBSTANCE_PROTEIN = "SubstanceProtein"
    SUBSTANCE_REFERENCE_INFORMATION = "SubstanceReferenceInformation"
    SUBSTANCE_SOURCE_MATERIAL = "SubstanceSourceMaterial"
    SUBSTANCE_SPECIFICATION = "SubstanceSpecification"
    SUPPLY_DELIVERY = "SupplyDelivery"
    SUPPLY_REQUEST = "SupplyRequest"
    TASK = "Task"
    TERMINOLOGY_CAPABILITIES = "TerminologyCapabilities"
    TEST_REPORT = "TestReport"
    TEST_SCRIPT = "TestScript"
    VALUE_SET = "ValueSet"
    VERIFICATION_RESULT = "VerificationResult"
    VISION_PRESCRIPTION = "VisionPrescription"

    def visit(
        self,
        account: typing.Callable[[], T_Result],
        activity_definition: typing.Callable[[], T_Result],
        adverse_event: typing.Callable[[], T_Result],
        allergy_intolerance: typing.Callable[[], T_Result],
        appointment: typing.Callable[[], T_Result],
        appointment_response: typing.Callable[[], T_Result],
        audit_event: typing.Callable[[], T_Result],
        basic: typing.Callable[[], T_Result],
        binary: typing.Callable[[], T_Result],
        biologically_derived_product: typing.Callable[[], T_Result],
        body_structure: typing.Callable[[], T_Result],
        bundle: typing.Callable[[], T_Result],
        capability_statement: typing.Callable[[], T_Result],
        care_plan: typing.Callable[[], T_Result],
        care_team: typing.Callable[[], T_Result],
        catalog_entry: typing.Callable[[], T_Result],
        charge_item: typing.Callable[[], T_Result],
        charge_item_definition: typing.Callable[[], T_Result],
        claim: typing.Callable[[], T_Result],
        claim_response: typing.Callable[[], T_Result],
        clinical_impression: typing.Callable[[], T_Result],
        code_system: typing.Callable[[], T_Result],
        communication: typing.Callable[[], T_Result],
        communication_request: typing.Callable[[], T_Result],
        compartment_definition: typing.Callable[[], T_Result],
        composition: typing.Callable[[], T_Result],
        concept_map: typing.Callable[[], T_Result],
        condition: typing.Callable[[], T_Result],
        consent: typing.Callable[[], T_Result],
        contract: typing.Callable[[], T_Result],
        coverage: typing.Callable[[], T_Result],
        coverage_eligibility_request: typing.Callable[[], T_Result],
        coverage_eligibility_response: typing.Callable[[], T_Result],
        detected_issue: typing.Callable[[], T_Result],
        device: typing.Callable[[], T_Result],
        device_definition: typing.Callable[[], T_Result],
        device_metric: typing.Callable[[], T_Result],
        device_request: typing.Callable[[], T_Result],
        device_use_statement: typing.Callable[[], T_Result],
        diagnostic_report: typing.Callable[[], T_Result],
        document_manifest: typing.Callable[[], T_Result],
        document_reference: typing.Callable[[], T_Result],
        effect_evidence_synthesis: typing.Callable[[], T_Result],
        encounter: typing.Callable[[], T_Result],
        endpoint: typing.Callable[[], T_Result],
        enrollment_request: typing.Callable[[], T_Result],
        enrollment_response: typing.Callable[[], T_Result],
        episode_of_care: typing.Callable[[], T_Result],
        event_definition: typing.Callable[[], T_Result],
        evidence: typing.Callable[[], T_Result],
        evidence_variable: typing.Callable[[], T_Result],
        example_scenario: typing.Callable[[], T_Result],
        explanation_of_benefit: typing.Callable[[], T_Result],
        family_member_history: typing.Callable[[], T_Result],
        flag: typing.Callable[[], T_Result],
        goal: typing.Callable[[], T_Result],
        graph_definition: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
        guidance_response: typing.Callable[[], T_Result],
        healthcare_service: typing.Callable[[], T_Result],
        imaging_study: typing.Callable[[], T_Result],
        immunization: typing.Callable[[], T_Result],
        immunization_evaluation: typing.Callable[[], T_Result],
        immunization_recommendation: typing.Callable[[], T_Result],
        implementation_guide: typing.Callable[[], T_Result],
        insurance_plan: typing.Callable[[], T_Result],
        invoice: typing.Callable[[], T_Result],
        library: typing.Callable[[], T_Result],
        linkage: typing.Callable[[], T_Result],
        list_: typing.Callable[[], T_Result],
        location: typing.Callable[[], T_Result],
        measure: typing.Callable[[], T_Result],
        measure_report: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        medication: typing.Callable[[], T_Result],
        medication_administration: typing.Callable[[], T_Result],
        medication_dispense: typing.Callable[[], T_Result],
        medication_knowledge: typing.Callable[[], T_Result],
        medication_request: typing.Callable[[], T_Result],
        medication_statement: typing.Callable[[], T_Result],
        medicinal_product: typing.Callable[[], T_Result],
        medicinal_product_authorization: typing.Callable[[], T_Result],
        medicinal_product_contraindication: typing.Callable[[], T_Result],
        medicinal_product_indication: typing.Callable[[], T_Result],
        medicinal_product_ingredient: typing.Callable[[], T_Result],
        medicinal_product_interaction: typing.Callable[[], T_Result],
        medicinal_product_manufactured: typing.Callable[[], T_Result],
        medicinal_product_packaged: typing.Callable[[], T_Result],
        medicinal_product_pharmaceutical: typing.Callable[[], T_Result],
        medicinal_product_undesirable_effect: typing.Callable[[], T_Result],
        message_definition: typing.Callable[[], T_Result],
        message_header: typing.Callable[[], T_Result],
        molecular_sequence: typing.Callable[[], T_Result],
        naming_system: typing.Callable[[], T_Result],
        nutrition_order: typing.Callable[[], T_Result],
        observation: typing.Callable[[], T_Result],
        observation_definition: typing.Callable[[], T_Result],
        operation_definition: typing.Callable[[], T_Result],
        operation_outcome: typing.Callable[[], T_Result],
        organization: typing.Callable[[], T_Result],
        organization_affiliation: typing.Callable[[], T_Result],
        parameters: typing.Callable[[], T_Result],
        patient: typing.Callable[[], T_Result],
        payment_notice: typing.Callable[[], T_Result],
        payment_reconciliation: typing.Callable[[], T_Result],
        person: typing.Callable[[], T_Result],
        plan_definition: typing.Callable[[], T_Result],
        practitioner: typing.Callable[[], T_Result],
        practitioner_role: typing.Callable[[], T_Result],
        procedure: typing.Callable[[], T_Result],
        provenance: typing.Callable[[], T_Result],
        questionnaire: typing.Callable[[], T_Result],
        questionnaire_response: typing.Callable[[], T_Result],
        related_person: typing.Callable[[], T_Result],
        request_group: typing.Callable[[], T_Result],
        research_definition: typing.Callable[[], T_Result],
        research_element_definition: typing.Callable[[], T_Result],
        research_study: typing.Callable[[], T_Result],
        research_subject: typing.Callable[[], T_Result],
        risk_assessment: typing.Callable[[], T_Result],
        risk_evidence_synthesis: typing.Callable[[], T_Result],
        schedule: typing.Callable[[], T_Result],
        search_parameter: typing.Callable[[], T_Result],
        service_request: typing.Callable[[], T_Result],
        slot: typing.Callable[[], T_Result],
        specimen: typing.Callable[[], T_Result],
        specimen_definition: typing.Callable[[], T_Result],
        structure_definition: typing.Callable[[], T_Result],
        structure_map: typing.Callable[[], T_Result],
        subscription: typing.Callable[[], T_Result],
        substance: typing.Callable[[], T_Result],
        substance_nucleic_acid: typing.Callable[[], T_Result],
        substance_polymer: typing.Callable[[], T_Result],
        substance_protein: typing.Callable[[], T_Result],
        substance_reference_information: typing.Callable[[], T_Result],
        substance_source_material: typing.Callable[[], T_Result],
        substance_specification: typing.Callable[[], T_Result],
        supply_delivery: typing.Callable[[], T_Result],
        supply_request: typing.Callable[[], T_Result],
        task: typing.Callable[[], T_Result],
        terminology_capabilities: typing.Callable[[], T_Result],
        test_report: typing.Callable[[], T_Result],
        test_script: typing.Callable[[], T_Result],
        value_set: typing.Callable[[], T_Result],
        verification_result: typing.Callable[[], T_Result],
        vision_prescription: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResourceType.ACCOUNT:
            return account()
        if self is ResourceType.ACTIVITY_DEFINITION:
            return activity_definition()
        if self is ResourceType.ADVERSE_EVENT:
            return adverse_event()
        if self is ResourceType.ALLERGY_INTOLERANCE:
            return allergy_intolerance()
        if self is ResourceType.APPOINTMENT:
            return appointment()
        if self is ResourceType.APPOINTMENT_RESPONSE:
            return appointment_response()
        if self is ResourceType.AUDIT_EVENT:
            return audit_event()
        if self is ResourceType.BASIC:
            return basic()
        if self is ResourceType.BINARY:
            return binary()
        if self is ResourceType.BIOLOGICALLY_DERIVED_PRODUCT:
            return biologically_derived_product()
        if self is ResourceType.BODY_STRUCTURE:
            return body_structure()
        if self is ResourceType.BUNDLE:
            return bundle()
        if self is ResourceType.CAPABILITY_STATEMENT:
            return capability_statement()
        if self is ResourceType.CARE_PLAN:
            return care_plan()
        if self is ResourceType.CARE_TEAM:
            return care_team()
        if self is ResourceType.CATALOG_ENTRY:
            return catalog_entry()
        if self is ResourceType.CHARGE_ITEM:
            return charge_item()
        if self is ResourceType.CHARGE_ITEM_DEFINITION:
            return charge_item_definition()
        if self is ResourceType.CLAIM:
            return claim()
        if self is ResourceType.CLAIM_RESPONSE:
            return claim_response()
        if self is ResourceType.CLINICAL_IMPRESSION:
            return clinical_impression()
        if self is ResourceType.CODE_SYSTEM:
            return code_system()
        if self is ResourceType.COMMUNICATION:
            return communication()
        if self is ResourceType.COMMUNICATION_REQUEST:
            return communication_request()
        if self is ResourceType.COMPARTMENT_DEFINITION:
            return compartment_definition()
        if self is ResourceType.COMPOSITION:
            return composition()
        if self is ResourceType.CONCEPT_MAP:
            return concept_map()
        if self is ResourceType.CONDITION:
            return condition()
        if self is ResourceType.CONSENT:
            return consent()
        if self is ResourceType.CONTRACT:
            return contract()
        if self is ResourceType.COVERAGE:
            return coverage()
        if self is ResourceType.COVERAGE_ELIGIBILITY_REQUEST:
            return coverage_eligibility_request()
        if self is ResourceType.COVERAGE_ELIGIBILITY_RESPONSE:
            return coverage_eligibility_response()
        if self is ResourceType.DETECTED_ISSUE:
            return detected_issue()
        if self is ResourceType.DEVICE:
            return device()
        if self is ResourceType.DEVICE_DEFINITION:
            return device_definition()
        if self is ResourceType.DEVICE_METRIC:
            return device_metric()
        if self is ResourceType.DEVICE_REQUEST:
            return device_request()
        if self is ResourceType.DEVICE_USE_STATEMENT:
            return device_use_statement()
        if self is ResourceType.DIAGNOSTIC_REPORT:
            return diagnostic_report()
        if self is ResourceType.DOCUMENT_MANIFEST:
            return document_manifest()
        if self is ResourceType.DOCUMENT_REFERENCE:
            return document_reference()
        if self is ResourceType.EFFECT_EVIDENCE_SYNTHESIS:
            return effect_evidence_synthesis()
        if self is ResourceType.ENCOUNTER:
            return encounter()
        if self is ResourceType.ENDPOINT:
            return endpoint()
        if self is ResourceType.ENROLLMENT_REQUEST:
            return enrollment_request()
        if self is ResourceType.ENROLLMENT_RESPONSE:
            return enrollment_response()
        if self is ResourceType.EPISODE_OF_CARE:
            return episode_of_care()
        if self is ResourceType.EVENT_DEFINITION:
            return event_definition()
        if self is ResourceType.EVIDENCE:
            return evidence()
        if self is ResourceType.EVIDENCE_VARIABLE:
            return evidence_variable()
        if self is ResourceType.EXAMPLE_SCENARIO:
            return example_scenario()
        if self is ResourceType.EXPLANATION_OF_BENEFIT:
            return explanation_of_benefit()
        if self is ResourceType.FAMILY_MEMBER_HISTORY:
            return family_member_history()
        if self is ResourceType.FLAG:
            return flag()
        if self is ResourceType.GOAL:
            return goal()
        if self is ResourceType.GRAPH_DEFINITION:
            return graph_definition()
        if self is ResourceType.GROUP:
            return group()
        if self is ResourceType.GUIDANCE_RESPONSE:
            return guidance_response()
        if self is ResourceType.HEALTHCARE_SERVICE:
            return healthcare_service()
        if self is ResourceType.IMAGING_STUDY:
            return imaging_study()
        if self is ResourceType.IMMUNIZATION:
            return immunization()
        if self is ResourceType.IMMUNIZATION_EVALUATION:
            return immunization_evaluation()
        if self is ResourceType.IMMUNIZATION_RECOMMENDATION:
            return immunization_recommendation()
        if self is ResourceType.IMPLEMENTATION_GUIDE:
            return implementation_guide()
        if self is ResourceType.INSURANCE_PLAN:
            return insurance_plan()
        if self is ResourceType.INVOICE:
            return invoice()
        if self is ResourceType.LIBRARY:
            return library()
        if self is ResourceType.LINKAGE:
            return linkage()
        if self is ResourceType.LIST:
            return list_()
        if self is ResourceType.LOCATION:
            return location()
        if self is ResourceType.MEASURE:
            return measure()
        if self is ResourceType.MEASURE_REPORT:
            return measure_report()
        if self is ResourceType.MEDIA:
            return media()
        if self is ResourceType.MEDICATION:
            return medication()
        if self is ResourceType.MEDICATION_ADMINISTRATION:
            return medication_administration()
        if self is ResourceType.MEDICATION_DISPENSE:
            return medication_dispense()
        if self is ResourceType.MEDICATION_KNOWLEDGE:
            return medication_knowledge()
        if self is ResourceType.MEDICATION_REQUEST:
            return medication_request()
        if self is ResourceType.MEDICATION_STATEMENT:
            return medication_statement()
        if self is ResourceType.MEDICINAL_PRODUCT:
            return medicinal_product()
        if self is ResourceType.MEDICINAL_PRODUCT_AUTHORIZATION:
            return medicinal_product_authorization()
        if self is ResourceType.MEDICINAL_PRODUCT_CONTRAINDICATION:
            return medicinal_product_contraindication()
        if self is ResourceType.MEDICINAL_PRODUCT_INDICATION:
            return medicinal_product_indication()
        if self is ResourceType.MEDICINAL_PRODUCT_INGREDIENT:
            return medicinal_product_ingredient()
        if self is ResourceType.MEDICINAL_PRODUCT_INTERACTION:
            return medicinal_product_interaction()
        if self is ResourceType.MEDICINAL_PRODUCT_MANUFACTURED:
            return medicinal_product_manufactured()
        if self is ResourceType.MEDICINAL_PRODUCT_PACKAGED:
            return medicinal_product_packaged()
        if self is ResourceType.MEDICINAL_PRODUCT_PHARMACEUTICAL:
            return medicinal_product_pharmaceutical()
        if self is ResourceType.MEDICINAL_PRODUCT_UNDESIRABLE_EFFECT:
            return medicinal_product_undesirable_effect()
        if self is ResourceType.MESSAGE_DEFINITION:
            return message_definition()
        if self is ResourceType.MESSAGE_HEADER:
            return message_header()
        if self is ResourceType.MOLECULAR_SEQUENCE:
            return molecular_sequence()
        if self is ResourceType.NAMING_SYSTEM:
            return naming_system()
        if self is ResourceType.NUTRITION_ORDER:
            return nutrition_order()
        if self is ResourceType.OBSERVATION:
            return observation()
        if self is ResourceType.OBSERVATION_DEFINITION:
            return observation_definition()
        if self is ResourceType.OPERATION_DEFINITION:
            return operation_definition()
        if self is ResourceType.OPERATION_OUTCOME:
            return operation_outcome()
        if self is ResourceType.ORGANIZATION:
            return organization()
        if self is ResourceType.ORGANIZATION_AFFILIATION:
            return organization_affiliation()
        if self is ResourceType.PARAMETERS:
            return parameters()
        if self is ResourceType.PATIENT:
            return patient()
        if self is ResourceType.PAYMENT_NOTICE:
            return payment_notice()
        if self is ResourceType.PAYMENT_RECONCILIATION:
            return payment_reconciliation()
        if self is ResourceType.PERSON:
            return person()
        if self is ResourceType.PLAN_DEFINITION:
            return plan_definition()
        if self is ResourceType.PRACTITIONER:
            return practitioner()
        if self is ResourceType.PRACTITIONER_ROLE:
            return practitioner_role()
        if self is ResourceType.PROCEDURE:
            return procedure()
        if self is ResourceType.PROVENANCE:
            return provenance()
        if self is ResourceType.QUESTIONNAIRE:
            return questionnaire()
        if self is ResourceType.QUESTIONNAIRE_RESPONSE:
            return questionnaire_response()
        if self is ResourceType.RELATED_PERSON:
            return related_person()
        if self is ResourceType.REQUEST_GROUP:
            return request_group()
        if self is ResourceType.RESEARCH_DEFINITION:
            return research_definition()
        if self is ResourceType.RESEARCH_ELEMENT_DEFINITION:
            return research_element_definition()
        if self is ResourceType.RESEARCH_STUDY:
            return research_study()
        if self is ResourceType.RESEARCH_SUBJECT:
            return research_subject()
        if self is ResourceType.RISK_ASSESSMENT:
            return risk_assessment()
        if self is ResourceType.RISK_EVIDENCE_SYNTHESIS:
            return risk_evidence_synthesis()
        if self is ResourceType.SCHEDULE:
            return schedule()
        if self is ResourceType.SEARCH_PARAMETER:
            return search_parameter()
        if self is ResourceType.SERVICE_REQUEST:
            return service_request()
        if self is ResourceType.SLOT:
            return slot()
        if self is ResourceType.SPECIMEN:
            return specimen()
        if self is ResourceType.SPECIMEN_DEFINITION:
            return specimen_definition()
        if self is ResourceType.STRUCTURE_DEFINITION:
            return structure_definition()
        if self is ResourceType.STRUCTURE_MAP:
            return structure_map()
        if self is ResourceType.SUBSCRIPTION:
            return subscription()
        if self is ResourceType.SUBSTANCE:
            return substance()
        if self is ResourceType.SUBSTANCE_NUCLEIC_ACID:
            return substance_nucleic_acid()
        if self is ResourceType.SUBSTANCE_POLYMER:
            return substance_polymer()
        if self is ResourceType.SUBSTANCE_PROTEIN:
            return substance_protein()
        if self is ResourceType.SUBSTANCE_REFERENCE_INFORMATION:
            return substance_reference_information()
        if self is ResourceType.SUBSTANCE_SOURCE_MATERIAL:
            return substance_source_material()
        if self is ResourceType.SUBSTANCE_SPECIFICATION:
            return substance_specification()
        if self is ResourceType.SUPPLY_DELIVERY:
            return supply_delivery()
        if self is ResourceType.SUPPLY_REQUEST:
            return supply_request()
        if self is ResourceType.TASK:
            return task()
        if self is ResourceType.TERMINOLOGY_CAPABILITIES:
            return terminology_capabilities()
        if self is ResourceType.TEST_REPORT:
            return test_report()
        if self is ResourceType.TEST_SCRIPT:
            return test_script()
        if self is ResourceType.VALUE_SET:
            return value_set()
        if self is ResourceType.VERIFICATION_RESULT:
            return verification_result()
        if self is ResourceType.VISION_PRESCRIPTION:
            return vision_prescription()
