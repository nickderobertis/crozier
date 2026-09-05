

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .terms_and_conditions_detail import TermsAndConditionsDetail


class OrgTermsAndConditionsDetail(UniversalBaseModel):
    """
    Participant TnC details
    """

    initiated_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="InitiatedBy"),
        pydantic.Field(
            alias="InitiatedBy", description="Email of the user who initiated the External signing for this participant"
        ),
    ] = None
    """
    Email of the user who initiated the External signing for this participant
    """

    role: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Role"),
        pydantic.Field(
            alias="Role", description="Role of the user who initiated the External signing for this participant"
        ),
    ] = None
    """
    Role of the user who initiated the External signing for this participant
    """

    terms_and_conditions_detail: typing_extensions.Annotated[
        typing.Optional[TermsAndConditionsDetail],
        FieldMetadata(alias="TermsAndConditionsDetail"),
        pydantic.Field(alias="TermsAndConditionsDetail"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
