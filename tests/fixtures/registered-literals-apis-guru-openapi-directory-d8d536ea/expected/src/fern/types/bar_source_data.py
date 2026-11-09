

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bar_source_data_administrative_actions_array_item import BarSourceDataAdministrativeActionsArrayItem
from .bar_source_data_advanced_degree_array_item import BarSourceDataAdvancedDegreeArrayItem
from .bar_source_data_bar_status_array_item import BarSourceDataBarStatusArrayItem
from .bar_source_data_board_certifications_array_item import BarSourceDataBoardCertificationsArrayItem
from .bar_source_data_committees_array_item import BarSourceDataCommitteesArrayItem
from .bar_source_data_court_history_array_item import BarSourceDataCourtHistoryArrayItem
from .bar_source_data_court_of_admissions import BarSourceDataCourtOfAdmissions
from .bar_source_data_disciplinary_history_array_item import BarSourceDataDisciplinaryHistoryArrayItem
from .bar_source_data_discipline_summaries_array_item import BarSourceDataDisciplineSummariesArrayItem
from .bar_source_data_employment_history_array_item import BarSourceDataEmploymentHistoryArrayItem
from .bar_source_data_fees_options_array_item import BarSourceDataFeesOptionsArrayItem
from .bar_source_data_involvements_array_item import BarSourceDataInvolvementsArrayItem
from .bar_source_data_law_school_array_item import BarSourceDataLawSchoolArrayItem
from .bar_source_data_name import BarSourceDataName
from .bar_source_data_open_action_status_array_item import BarSourceDataOpenActionStatusArrayItem
from .bar_source_data_other_jurisdiction_array_item import BarSourceDataOtherJurisdictionArrayItem
from .bar_source_data_public_hearing_array_item import BarSourceDataPublicHearingArrayItem
from .bar_source_data_reason_for_inactivation import BarSourceDataReasonForInactivation
from .bar_source_data_related_cases_array_item import BarSourceDataRelatedCasesArrayItem
from .bar_source_data_source_info import BarSourceDataSourceInfo
from .bar_source_data_statewide_grievance_committee_history_array_item import (
    BarSourceDataStatewideGrievanceCommitteeHistoryArrayItem,
)
from .bar_source_data_status_history_array_item import BarSourceDataStatusHistoryArrayItem
from .bar_source_data_ten_year_discipline_array_item import BarSourceDataTenYearDisciplineArrayItem


class BarSourceData(UniversalBaseModel):
    administrative_actions_array: typing_extensions.Annotated[
        typing.List[BarSourceDataAdministrativeActionsArrayItem],
        FieldMetadata(alias="administrativeActionsArray"),
        pydantic.Field(alias="administrativeActionsArray"),
    ]
    admission_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="admissionType"), pydantic.Field(alias="admissionType")
    ] = None
    advanced_degree_array: typing_extensions.Annotated[
        typing.List[BarSourceDataAdvancedDegreeArrayItem],
        FieldMetadata(alias="advancedDegreeArray"),
        pydantic.Field(alias="advancedDegreeArray"),
    ]
    appellate_court_district: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="appellateCourtDistrict"),
        pydantic.Field(alias="appellateCourtDistrict"),
    ] = None
    appellate_division_department: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="appellateDivisionDepartment"),
        pydantic.Field(alias="appellateDivisionDepartment"),
    ] = None
    attorney_group: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="attorneyGroup"), pydantic.Field(alias="attorneyGroup")
    ] = None
    authorized: typing.Optional[str] = None
    bar_law_firm: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="barLawFirm"), pydantic.Field(alias="barLawFirm")
    ] = None
    bar_service_class: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="barServiceClass"), pydantic.Field(alias="barServiceClass")
    ] = None
    bar_status_array: typing_extensions.Annotated[
        typing.List[BarSourceDataBarStatusArrayItem],
        FieldMetadata(alias="barStatusArray"),
        pydantic.Field(alias="barStatusArray"),
    ]
    bio: typing.Optional[str] = None
    board_certifications_array: typing_extensions.Annotated[
        typing.List[BarSourceDataBoardCertificationsArrayItem],
        FieldMetadata(alias="boardCertificationsArray"),
        pydantic.Field(alias="boardCertificationsArray"),
    ]
    board_district: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="boardDistrict"), pydantic.Field(alias="boardDistrict")
    ] = None
    circuit: typing.Optional[str] = None
    clients_represented_array: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="clientsRepresentedArray"),
        pydantic.Field(alias="clientsRepresentedArray"),
    ]
    comments: typing.Optional[str] = None
    committees_array: typing_extensions.Annotated[
        typing.List[BarSourceDataCommitteesArrayItem],
        FieldMetadata(alias="committeesArray"),
        pydantic.Field(alias="committeesArray"),
    ]
    court_history_array: typing_extensions.Annotated[
        typing.List[BarSourceDataCourtHistoryArrayItem],
        FieldMetadata(alias="courtHistoryArray"),
        pydantic.Field(alias="courtHistoryArray"),
    ]
    court_of_admissions: typing_extensions.Annotated[
        typing.Optional[BarSourceDataCourtOfAdmissions],
        FieldMetadata(alias="courtOfAdmissions"),
        pydantic.Field(alias="courtOfAdmissions"),
    ] = None
    court_service_email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="courtServiceEmail"), pydantic.Field(alias="courtServiceEmail")
    ] = None
    disciplinary_history_array: typing_extensions.Annotated[
        typing.List[BarSourceDataDisciplinaryHistoryArrayItem],
        FieldMetadata(alias="disciplinaryHistoryArray"),
        pydantic.Field(alias="disciplinaryHistoryArray"),
    ]
    discipline_summaries_array: typing_extensions.Annotated[
        typing.List[BarSourceDataDisciplineSummariesArrayItem],
        FieldMetadata(alias="disciplineSummariesArray"),
        pydantic.Field(alias="disciplineSummariesArray"),
    ]
    dismissals_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="dismissalsArray"), pydantic.Field(alias="dismissalsArray")
    ]
    district: typing.Optional[str] = None
    employment_history_array: typing_extensions.Annotated[
        typing.List[BarSourceDataEmploymentHistoryArrayItem],
        FieldMetadata(alias="employmentHistoryArray"),
        pydantic.Field(alias="employmentHistoryArray"),
    ]
    expiration_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expirationDate"), pydantic.Field(alias="expirationDate")
    ] = None
    fees_options_array: typing_extensions.Annotated[
        typing.List[BarSourceDataFeesOptionsArrayItem],
        FieldMetadata(alias="feesOptionsArray"),
        pydantic.Field(alias="feesOptionsArray"),
    ]
    firm_size: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firmSize"), pydantic.Field(alias="firmSize")
    ] = None
    firm_website: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firmWebsite"), pydantic.Field(alias="firmWebsite")
    ] = None
    first_admitted_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="firstAdmittedDate"),
        pydantic.Field(
            alias="firstAdmittedDate",
            description="The firstAdmittedDate is the date when an attorney was admitted to the bar for the very first time regardless of which U.S state.",
        ),
    ] = None
    """
    The firstAdmittedDate is the date when an attorney was admitted to the bar for the very first time regardless of which U.S state.
    """

    first_admitted_year: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="firstAdmittedYear"), pydantic.Field(alias="firstAdmittedYear")
    ] = None
    home_county: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="homeCounty"), pydantic.Field(alias="homeCounty")
    ] = None
    in_good_standing: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="inGoodStanding"), pydantic.Field(alias="inGoodStanding")
    ] = None
    insurance: typing.Optional[str] = None
    involvements_array: typing_extensions.Annotated[
        typing.List[BarSourceDataInvolvementsArrayItem],
        FieldMetadata(alias="involvementsArray"),
        pydantic.Field(alias="involvementsArray"),
    ]
    judicial_district: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="judicialDistrict"), pydantic.Field(alias="judicialDistrict")
    ] = None
    juris_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="jurisType"), pydantic.Field(alias="jurisType")
    ] = None
    languages_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="languagesArray"), pydantic.Field(alias="languagesArray")
    ]
    last_renewal_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastRenewalDate"), pydantic.Field(alias="lastRenewalDate")
    ] = None
    law_school_array: typing_extensions.Annotated[
        typing.List[BarSourceDataLawSchoolArrayItem],
        FieldMetadata(alias="lawSchoolArray"),
        pydantic.Field(alias="lawSchoolArray"),
    ]
    legal_speciality_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="legalSpecialityArray"), pydantic.Field(alias="legalSpecialityArray")
    ]
    license_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="licenseType"), pydantic.Field(alias="licenseType")
    ] = None
    name: BarSourceDataName
    next_registration: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="nextRegistration"), pydantic.Field(alias="nextRegistration")
    ] = None
    next_renewal_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="nextRenewalDate"), pydantic.Field(alias="nextRenewalDate")
    ] = None
    object: str
    open_action_status_array: typing_extensions.Annotated[
        typing.List[BarSourceDataOpenActionStatusArrayItem],
        FieldMetadata(alias="openActionStatusArray"),
        pydantic.Field(alias="openActionStatusArray"),
    ]
    other_jurisdiction_array: typing_extensions.Annotated[
        typing.List[BarSourceDataOtherJurisdictionArrayItem],
        FieldMetadata(alias="otherJurisdictionArray"),
        pydantic.Field(alias="otherJurisdictionArray"),
    ]
    other_name_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="otherNameArray"), pydantic.Field(alias="otherNameArray")
    ]
    parish: typing.Optional[str] = None
    pending_proceeding_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="pendingProceedingArray"), pydantic.Field(alias="pendingProceedingArray")
    ]
    position: typing.Optional[str] = None
    practice_area_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="practiceAreaArray"), pydantic.Field(alias="practiceAreaArray")
    ]
    practice_location_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="practiceLocationArray"), pydantic.Field(alias="practiceLocationArray")
    ]
    private_law_practice: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="privateLawPractice"), pydantic.Field(alias="privateLawPractice")
    ] = None
    profile_last_certified: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="profileLastCertified"),
        pydantic.Field(alias="profileLastCertified"),
    ] = None
    public_hearing_array: typing_extensions.Annotated[
        typing.List[BarSourceDataPublicHearingArrayItem],
        FieldMetadata(alias="publicHearingArray"),
        pydantic.Field(alias="publicHearingArray"),
    ]
    reason_for_inactivation: typing_extensions.Annotated[
        typing.Optional[BarSourceDataReasonForInactivation],
        FieldMetadata(alias="reasonForInactivation"),
        pydantic.Field(alias="reasonForInactivation"),
    ] = None
    related_cases_array: typing_extensions.Annotated[
        typing.List[BarSourceDataRelatedCasesArrayItem],
        FieldMetadata(alias="relatedCasesArray"),
        pydantic.Field(alias="relatedCasesArray"),
    ]
    sections_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="sectionsArray"), pydantic.Field(alias="sectionsArray")
    ]
    services_array: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="servicesArray"), pydantic.Field(alias="servicesArray")
    ]
    source_info: typing_extensions.Annotated[
        typing.Optional[BarSourceDataSourceInfo], FieldMetadata(alias="sourceInfo"), pydantic.Field(alias="sourceInfo")
    ] = None
    statewide_grievance_committee_history_array: typing_extensions.Annotated[
        typing.List[BarSourceDataStatewideGrievanceCommitteeHistoryArrayItem],
        FieldMetadata(alias="statewideGrievanceCommitteeHistoryArray"),
        pydantic.Field(alias="statewideGrievanceCommitteeHistoryArray"),
    ]
    status: typing.Optional[str] = None
    status_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="statusDate"), pydantic.Field(alias="statusDate")
    ] = None
    status_hint: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="statusHint"), pydantic.Field(alias="statusHint")
    ] = None
    status_history_array: typing_extensions.Annotated[
        typing.List[BarSourceDataStatusHistoryArrayItem],
        FieldMetadata(alias="statusHistoryArray"),
        pydantic.Field(alias="statusHistoryArray"),
    ]
    ten_year_discipline_array: typing_extensions.Annotated[
        typing.List[BarSourceDataTenYearDisciplineArrayItem],
        FieldMetadata(alias="tenYearDisciplineArray"),
        pydantic.Field(alias="tenYearDisciplineArray"),
    ]
    undergraduate_school: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="undergraduateSchool"), pydantic.Field(alias="undergraduateSchool")
    ] = None
    years_of_practice: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="yearsOfPractice"), pydantic.Field(alias="yearsOfPractice")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
