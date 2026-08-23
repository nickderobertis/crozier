

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dpp_status import DppStatus
from .granularity import Granularity
from .identifier import Identifier
from .timestamp import Timestamp


class DppEnvelope(UniversalBaseModel):
    """
    EN 18223 DigitalProductPassport envelope (clause 4.1.2.1, Table 1).
    """

    digital_product_passport_id: typing_extensions.Annotated[
        Identifier,
        FieldMetadata(alias="digitalProductPassportId"),
        pydantic.Field(alias="digitalProductPassportId", description="Globally unique DPP identifier (URI)."),
    ]
    """
    Globally unique DPP identifier (URI).
    """

    unique_product_identifier: typing_extensions.Annotated[
        Identifier,
        FieldMetadata(alias="uniqueProductIdentifier"),
        pydantic.Field(alias="uniqueProductIdentifier", description="GS1 Digital Link per EN 18219."),
    ]
    """
    GS1 Digital Link per EN 18219.
    """

    granularity: Granularity
    dpp_schema_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="dppSchemaVersion"), pydantic.Field(alias="dppSchemaVersion")
    ]
    dpp_status: typing_extensions.Annotated[
        DppStatus, FieldMetadata(alias="dppStatus"), pydantic.Field(alias="dppStatus")
    ]
    last_updated: typing_extensions.Annotated[
        Timestamp, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    economic_operator_id: typing_extensions.Annotated[
        Identifier,
        FieldMetadata(alias="economicOperatorId"),
        pydantic.Field(alias="economicOperatorId", description="Economic operator identifier per EN 18219."),
    ]
    """
    Economic operator identifier per EN 18219.
    """

    facility_id: typing_extensions.Annotated[
        typing.Optional[Identifier],
        FieldMetadata(alias="facilityId"),
        pydantic.Field(alias="facilityId", description="Optional facility identifier per EN 18219."),
    ] = None
    """
    Optional facility identifier per EN 18219.
    """

    content_specification_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="contentSpecificationIds"),
        pydantic.Field(
            alias="contentSpecificationIds",
            description="Content/product-type specification namespaces the payload cites.",
        ),
    ] = None
    """
    Content/product-type specification namespaces the payload cites.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
