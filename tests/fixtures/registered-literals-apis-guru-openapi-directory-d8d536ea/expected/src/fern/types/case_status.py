

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CaseStatus(UniversalBaseModel):
    case_class_array: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="caseClassArray"), pydantic.Field(alias="caseClassArray")
    ] = None
    case_status_group: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseStatusGroup"), pydantic.Field(alias="caseStatusGroup")
    ]
    case_status_group_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseStatusGroupId"), pydantic.Field(alias="caseStatusGroupId")
    ]
    case_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseStatusId"), pydantic.Field(alias="caseStatusId")
    ]
    created_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdDate"),
        pydantic.Field(
            alias="createdDate",
            description="The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.",
        ),
    ]
    """
    The date and time when it was first created. This date and time is in UTC. Formatted as YYYY-MM-DD HH:MM:SS.
    """

    name: typing.Optional[str] = None
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
