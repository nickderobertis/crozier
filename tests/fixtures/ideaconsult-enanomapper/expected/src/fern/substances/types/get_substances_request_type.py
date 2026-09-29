

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSubstancesRequestType(enum.StrEnum):
    SUBSTANCETYPE = "substancetype"
    NAME = "name"
    LIKE = "like"
    REGEXP = "regexp"
    UUIF = "uuif"
    COMP_TOX = "CompTox"
    DOI = "DOI"
    RELIABILITY = "reliability"
    PURPOSE_FLAG = "purposeFlag"
    STUDY_RESULT_TYPE = "studyResultType"
    IS_ROBUST_STUDY = "isRobustStudy"
    CITATION = "citation"
    CITATIONOWNER = "citationowner"
    TOPCATEGORY = "topcategory"
    ENDPOINTCATEGORY = "endpointcategory"
    PARAMS = "params"
    OWNER_NAME = "owner_name"
    OWNER_UUID = "owner_uuid"
    RELATED = "related"
    REFERENCE = "reference"
    FACET = "facet"

    def visit(
        self,
        substancetype: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        like: typing.Callable[[], T_Result],
        regexp: typing.Callable[[], T_Result],
        uuif: typing.Callable[[], T_Result],
        comp_tox: typing.Callable[[], T_Result],
        doi: typing.Callable[[], T_Result],
        reliability: typing.Callable[[], T_Result],
        purpose_flag: typing.Callable[[], T_Result],
        study_result_type: typing.Callable[[], T_Result],
        is_robust_study: typing.Callable[[], T_Result],
        citation: typing.Callable[[], T_Result],
        citationowner: typing.Callable[[], T_Result],
        topcategory: typing.Callable[[], T_Result],
        endpointcategory: typing.Callable[[], T_Result],
        params: typing.Callable[[], T_Result],
        owner_name: typing.Callable[[], T_Result],
        owner_uuid: typing.Callable[[], T_Result],
        related: typing.Callable[[], T_Result],
        reference: typing.Callable[[], T_Result],
        facet: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSubstancesRequestType.SUBSTANCETYPE:
            return substancetype()
        if self is GetSubstancesRequestType.NAME:
            return name()
        if self is GetSubstancesRequestType.LIKE:
            return like()
        if self is GetSubstancesRequestType.REGEXP:
            return regexp()
        if self is GetSubstancesRequestType.UUIF:
            return uuif()
        if self is GetSubstancesRequestType.COMP_TOX:
            return comp_tox()
        if self is GetSubstancesRequestType.DOI:
            return doi()
        if self is GetSubstancesRequestType.RELIABILITY:
            return reliability()
        if self is GetSubstancesRequestType.PURPOSE_FLAG:
            return purpose_flag()
        if self is GetSubstancesRequestType.STUDY_RESULT_TYPE:
            return study_result_type()
        if self is GetSubstancesRequestType.IS_ROBUST_STUDY:
            return is_robust_study()
        if self is GetSubstancesRequestType.CITATION:
            return citation()
        if self is GetSubstancesRequestType.CITATIONOWNER:
            return citationowner()
        if self is GetSubstancesRequestType.TOPCATEGORY:
            return topcategory()
        if self is GetSubstancesRequestType.ENDPOINTCATEGORY:
            return endpointcategory()
        if self is GetSubstancesRequestType.PARAMS:
            return params()
        if self is GetSubstancesRequestType.OWNER_NAME:
            return owner_name()
        if self is GetSubstancesRequestType.OWNER_UUID:
            return owner_uuid()
        if self is GetSubstancesRequestType.RELATED:
            return related()
        if self is GetSubstancesRequestType.REFERENCE:
            return reference()
        if self is GetSubstancesRequestType.FACET:
            return facet()
