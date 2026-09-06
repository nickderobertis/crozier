

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_system_models_client_status import UpdateSystemModelsClientStatus
from .update_system_models_paged_client_status_metadata import UpdateSystemModelsPagedClientStatusMetadata


class ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata(UniversalBaseModel):
    """
    A response containing a page of results and metadata concerning the results
    """

    entities: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateSystemModelsClientStatus]],
        FieldMetadata(alias="Entities"),
        pydantic.Field(alias="Entities", description="The set of entities that make up this page."),
    ] = None
    """
    The set of entities that make up this page.
    """

    metadata: typing_extensions.Annotated[
        typing.Optional[UpdateSystemModelsPagedClientStatusMetadata],
        FieldMetadata(alias="Metadata"),
        pydantic.Field(alias="Metadata", description="Metadata about this paged response"),
    ] = None
    """
    Metadata about this paged response
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
