

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .body_fields_type import BodyFieldsType
from .key_to_multi_value import KeyToMultiValue


class BodyFields(UniversalBaseModel):
    """
    multipart form-data body matcher
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    optional: typing.Optional[bool] = None
    type: typing.Optional[BodyFieldsType] = None
    fields: typing.Optional[KeyToMultiValue] = None
    filenames: typing.Optional[KeyToMultiValue] = None
    part_content_types: typing_extensions.Annotated[
        typing.Optional[KeyToMultiValue],
        FieldMetadata(alias="partContentTypes"),
        pydantic.Field(alias="partContentTypes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
