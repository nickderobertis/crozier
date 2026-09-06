

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .terms_and_conditions_item import TermsAndConditionsItem


class TermsAndConditionsDetails(UniversalBaseModel):
    """
    Details of TnC
    """

    requires_signing: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="RequiresSigning"),
        pydantic.Field(alias="RequiresSigning", description="Does the Directory TnC require signing"),
    ] = None
    """
    Does the Directory TnC require signing
    """

    terms_and_conditions_item: typing_extensions.Annotated[
        typing.Optional[TermsAndConditionsItem],
        FieldMetadata(alias="TermsAndConditionsItem"),
        pydantic.Field(alias="TermsAndConditionsItem"),
    ] = None
    updated: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="Updated"),
        pydantic.Field(alias="Updated", description="Has the document updated since the user signed"),
    ] = None
    """
    Has the document updated since the user signed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
