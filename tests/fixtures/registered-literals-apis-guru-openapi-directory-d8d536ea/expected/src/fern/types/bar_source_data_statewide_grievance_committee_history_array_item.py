

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataStatewideGrievanceCommitteeHistoryArrayItem(UniversalBaseModel):
    final_decision: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="finalDecision"), pydantic.Field(alias="finalDecision")
    ] = None
    final_decision_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="finalDecisionDate"),
        pydantic.Field(alias="finalDecisionDate"),
    ] = None
    grievance_complaint_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="grievanceComplaintNumber"),
        pydantic.Field(alias="grievanceComplaintNumber"),
    ] = None
    public_comments: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="publicComments"), pydantic.Field(alias="publicComments")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
