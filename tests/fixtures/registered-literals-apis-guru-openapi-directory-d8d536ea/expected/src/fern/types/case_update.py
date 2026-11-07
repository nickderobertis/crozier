

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case import Case
from .case_update_pacer_options_response import CaseUpdatePacerOptionsResponse
from .case_update_status import CaseUpdateStatus
from .exception import Exception


class CaseUpdate(UniversalBaseModel):
    case: typing.Optional[Case] = None
    case_api: typing_extensions.Annotated[str, FieldMetadata(alias="caseAPI"), pydantic.Field(alias="caseAPI")]
    case_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseId"),
        pydantic.Field(alias="caseId", description="Unique Id for a Case in UniCourt."),
    ]
    """
    Unique Id for a Case in UniCourt.
    """

    exception: typing.Optional[Exception] = None
    object: str = pydantic.Field()
    """
    Name of the object.
    """

    pacer_options: typing_extensions.Annotated[
        typing.Optional[CaseUpdatePacerOptionsResponse],
        FieldMetadata(alias="pacerOptions"),
        pydantic.Field(alias="pacerOptions"),
    ] = None
    requested_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="requestedDate"),
        pydantic.Field(
            alias="requestedDate", description="The date and time when the case was last requested for update "
        ),
    ]
    """
    The date and time when the case was last requested for update 
    """

    status: CaseUpdateStatus = pydantic.Field()
    """
    Status of the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
