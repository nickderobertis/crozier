

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tn_cs_to_be_signed import TnCsToBeSigned


class OrganisationWithTncTncDetails(UniversalBaseModel):
    tn_c_signed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="TnCSigned"),
        pydantic.Field(
            alias="TnCSigned",
            description="true - the terms and conditions have been signed. false - the terms and conditions have not been signed",
        ),
    ] = None
    """
    true - the terms and conditions have been signed. false - the terms and conditions have not been signed
    """

    tn_c_updated: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="TnCUpdated"),
        pydantic.Field(
            alias="TnCUpdated",
            description="true - attached signer template has been updated. false - no tnc present/not updated",
        ),
    ] = None
    """
    true - attached signer template has been updated. false - no tnc present/not updated
    """

    tn_cs_to_be_signed: typing_extensions.Annotated[
        typing.Optional[TnCsToBeSigned], FieldMetadata(alias="TnCsToBeSigned"), pydantic.Field(alias="TnCsToBeSigned")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
