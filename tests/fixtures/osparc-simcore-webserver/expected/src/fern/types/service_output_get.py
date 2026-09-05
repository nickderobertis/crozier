

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .widget import Widget


class ServiceOutputGet(UniversalBaseModel):
    """
    Extends fields of api_schemas_catalog.services.ServiceGet.outputs[*]
    """

    unit_long: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unitLong"),
        pydantic.Field(
            alias="unitLong", description="Long name of the unit for display (html-compatible), if available"
        ),
    ] = None
    """
    Long name of the unit for display (html-compatible), if available
    """

    unit_short: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unitShort"),
        pydantic.Field(
            alias="unitShort", description="Short name for the unit for display (html-compatible), if available"
        ),
    ] = None
    """
    Short name for the unit for display (html-compatible), if available
    """

    display_order: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="displayOrder"),
        pydantic.Field(
            alias="displayOrder",
            description="DEPRECATED: new display order is taken from the item position. This will be removed.",
        ),
    ] = None
    """
    DEPRECATED: new display order is taken from the item position. This will be removed.
    """

    label: str = pydantic.Field()
    """
    short name for the property
    """

    description: str = pydantic.Field()
    """
    description of the property
    """

    type: str = pydantic.Field()
    """
    data type expected on this input glob matching for data type is allowed
    """

    content_schema: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="contentSchema"),
        pydantic.Field(
            alias="contentSchema", description="jsonschema of this input/output. Required when type='ref_contentSchema'"
        ),
    ] = None
    """
    jsonschema of this input/output. Required when type='ref_contentSchema'
    """

    file_to_key_map: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="fileToKeyMap"),
        pydantic.Field(alias="fileToKeyMap", description="Place the data associated with the named keys in files"),
    ] = None
    """
    Place the data associated with the named keys in files
    """

    unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Units, when it refers to a physical quantity
    """

    widget: typing.Optional[Widget] = pydantic.Field(default=None)
    """
    custom widget to use instead of the default one determined from the data-type
    """

    key_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="keyId"),
        pydantic.Field(alias="keyId", description="Unique name identifier for this input"),
    ]
    """
    Unique name identifier for this input
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
