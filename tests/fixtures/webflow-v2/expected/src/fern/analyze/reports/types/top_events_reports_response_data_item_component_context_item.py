

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class TopEventsReportsResponseDataItemComponentContextItem(UniversalBaseModel):
    """
    Component rendering context for a top event row.
    """

    component_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="componentId"),
        pydantic.Field(alias="componentId", description="Identifier of the component definition."),
    ]
    """
    Identifier of the component definition.
    """

    instance_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="instanceId"),
        pydantic.Field(alias="instanceId", description="Identifier of the component instance."),
    ]
    """
    Identifier of the component instance.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
