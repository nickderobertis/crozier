

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sos_associated_norm_organization_relationship_type import SosAssociatedNormOrganizationRelationshipType


class SosAssociatedNormOrganization(UniversalBaseModel):
    from_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="fromDate"), pydantic.Field(alias="fromDate")
    ]
    name: str
    norm_organization_api: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="normOrganizationAPI"), pydantic.Field(alias="normOrganizationAPI")
    ] = None
    norm_organization_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="normOrganizationId"), pydantic.Field(alias="normOrganizationId")
    ] = None
    object: str
    relationship_type: typing_extensions.Annotated[
        SosAssociatedNormOrganizationRelationshipType,
        FieldMetadata(alias="relationshipType"),
        pydantic.Field(alias="relationshipType"),
    ]
    to_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="toDate"), pydantic.Field(alias="toDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
