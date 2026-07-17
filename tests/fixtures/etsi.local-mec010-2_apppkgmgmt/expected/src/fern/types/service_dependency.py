

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .category_ref import CategoryRef
from .not_specified import NotSpecified
from .transport_dependency import TransportDependency


class ServiceDependency(UniversalBaseModel):
    requested_permissions: typing_extensions.Annotated[
        typing.Optional[typing.List[NotSpecified]],
        FieldMetadata(alias="requestedPermissions"),
        pydantic.Field(
            alias="requestedPermissions",
            description="Requested permissions regarding the access of the application to the service. See clause 8.2 of ETSI GS MEC 009 [4].\nThe format of this attribute is left for the data model design stage.",
        ),
    ] = None
    """
    Requested permissions regarding the access of the application to the service. See clause 8.2 of ETSI GS MEC 009 [4].
    The format of this attribute is left for the data model design stage.
    """

    ser_category: typing_extensions.Annotated[
        typing.Optional[CategoryRef], FieldMetadata(alias="serCategory"), pydantic.Field(alias="serCategory")
    ] = None
    ser_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serName"),
        pydantic.Field(
            alias="serName", description="The name of the service, for example, RNIS, LocationService, etc."
        ),
    ]
    """
    The name of the service, for example, RNIS, LocationService, etc.
    """

    ser_transport_dependencies: typing_extensions.Annotated[
        typing.Optional[typing.List[TransportDependency]],
        FieldMetadata(alias="serTransportDependencies"),
        pydantic.Field(
            alias="serTransportDependencies",
            description="Indicates transport and serialization format dependencies of consuming the service. Defaults to REST + JSON if absent. See note.",
        ),
    ] = None
    """
    Indicates transport and serialization format dependencies of consuming the service. Defaults to REST + JSON if absent. See note.
    """

    version: str = pydantic.Field()
    """
    The version of the service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
