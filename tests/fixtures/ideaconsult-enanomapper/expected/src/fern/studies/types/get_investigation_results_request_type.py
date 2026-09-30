

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetInvestigationResultsRequestType(enum.StrEnum):
    BYINVESTIGATION = "byinvestigation"
    BYASSAY = "byassay"
    BYSUBSTANCE = "bysubstance"
    BYPROVIDER = "byprovider"
    BYCITATION = "bycitation"
    BYSTUDYTYPE = "bystudytype"
    BYSTRUCTURE_INCHIKEY = "bystructure_inchikey"
    BYSTRUCTURE_SMILES = "bystructure_smiles"
    BYSTRUCTURE_NAME = "bystructure_name"
    BYSUBSTANCE_NAME = "bysubstance_name"
    BYSUBSTANCE_TYPE = "bysubstance_type"

    def visit(
        self,
        byinvestigation: typing.Callable[[], T_Result],
        byassay: typing.Callable[[], T_Result],
        bysubstance: typing.Callable[[], T_Result],
        byprovider: typing.Callable[[], T_Result],
        bycitation: typing.Callable[[], T_Result],
        bystudytype: typing.Callable[[], T_Result],
        bystructure_inchikey: typing.Callable[[], T_Result],
        bystructure_smiles: typing.Callable[[], T_Result],
        bystructure_name: typing.Callable[[], T_Result],
        bysubstance_name: typing.Callable[[], T_Result],
        bysubstance_type: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetInvestigationResultsRequestType.BYINVESTIGATION:
            return byinvestigation()
        if self is GetInvestigationResultsRequestType.BYASSAY:
            return byassay()
        if self is GetInvestigationResultsRequestType.BYSUBSTANCE:
            return bysubstance()
        if self is GetInvestigationResultsRequestType.BYPROVIDER:
            return byprovider()
        if self is GetInvestigationResultsRequestType.BYCITATION:
            return bycitation()
        if self is GetInvestigationResultsRequestType.BYSTUDYTYPE:
            return bystudytype()
        if self is GetInvestigationResultsRequestType.BYSTRUCTURE_INCHIKEY:
            return bystructure_inchikey()
        if self is GetInvestigationResultsRequestType.BYSTRUCTURE_SMILES:
            return bystructure_smiles()
        if self is GetInvestigationResultsRequestType.BYSTRUCTURE_NAME:
            return bystructure_name()
        if self is GetInvestigationResultsRequestType.BYSUBSTANCE_NAME:
            return bysubstance_name()
        if self is GetInvestigationResultsRequestType.BYSUBSTANCE_TYPE:
            return bysubstance_type()
