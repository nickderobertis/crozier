

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .group_kind import GroupKind


class AnnotationSettingSpec(UniversalBaseModel):
    """
    Desired annotation form configuration for a target resource kind.
    """

    form_schema: typing_extensions.Annotated[
        typing.List[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="formSchema"),
        pydantic.Field(alias="formSchema", description="FormKit-compatible schema used to render annotation fields."),
    ]
    """
    FormKit-compatible schema used to render annotation fields.
    """

    target_ref: typing_extensions.Annotated[
        GroupKind, FieldMetadata(alias="targetRef"), pydantic.Field(alias="targetRef")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
