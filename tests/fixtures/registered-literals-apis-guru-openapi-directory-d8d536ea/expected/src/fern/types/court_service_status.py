

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .service_status import ServiceStatus


class CourtServiceStatus(UniversalBaseModel):
    case_class_id_array: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Optional[str]]],
        FieldMetadata(alias="caseClassIdArray"),
        pydantic.Field(alias="caseClassIdArray", description="All the Case class ids associated to the service status"),
    ] = None
    """
    All the Case class ids associated to the service status
    """

    case_document_order_service_status: typing_extensions.Annotated[
        typing.Optional[ServiceStatus],
        FieldMetadata(alias="caseDocumentOrderServiceStatus"),
        pydantic.Field(alias="caseDocumentOrderServiceStatus"),
    ] = None
    case_track_service_status: typing_extensions.Annotated[
        typing.Optional[ServiceStatus],
        FieldMetadata(alias="caseTrackServiceStatus"),
        pydantic.Field(alias="caseTrackServiceStatus"),
    ] = None
    case_update_service_status: typing_extensions.Annotated[
        typing.Optional[ServiceStatus],
        FieldMetadata(alias="caseUpdateServiceStatus"),
        pydantic.Field(alias="caseUpdateServiceStatus"),
    ] = None
    court_id_array: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Optional[str]]],
        FieldMetadata(alias="courtIdArray"),
        pydantic.Field(alias="courtIdArray", description="All the court ids associated to the service status"),
    ] = None
    """
    All the court ids associated to the service status
    """

    court_location_id_array: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Optional[str]]],
        FieldMetadata(alias="courtLocationIdArray"),
        pydantic.Field(
            alias="courtLocationIdArray", description="All the court location ids associated to the service status"
        ),
    ] = None
    """
    All the court location ids associated to the service status
    """

    court_service_status_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="courtServiceStatusId"),
        pydantic.Field(alias="courtServiceStatusId", description="Court Service Status Object ID"),
    ]
    """
    Court Service Status Object ID
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    service_status_as_on: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="serviceStatusAsOn"),
        pydantic.Field(alias="serviceStatusAsOn", description="Date when the service status was last fetched."),
    ] = None
    """
    Date when the service status was last fetched.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
