

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_update_pacer_options import CaseUpdatePacerOptions


class CaseUpdateRequest(UniversalBaseModel):
    case_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="caseId"), pydantic.Field(alias="caseId", description="UniCourt's Case Id for update.")
    ]
    """
    UniCourt's Case Id for update.
    """

    pacer_options: typing_extensions.Annotated[
        typing.Optional[CaseUpdatePacerOptions],
        FieldMetadata(alias="pacerOptions"),
        pydantic.Field(alias="pacerOptions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
