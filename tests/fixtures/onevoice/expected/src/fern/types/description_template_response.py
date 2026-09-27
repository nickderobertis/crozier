

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DescriptionTemplateResponse(UniversalBaseModel):
    description_template: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="descriptionTemplate"),
        pydantic.Field(alias="descriptionTemplate", description="Stored template override; empty string when unset."),
    ]
    """
    Stored template override; empty string when unset.
    """

    placeholders: typing.List[str] = pydantic.Field()
    """
    Allowed placeholder names the template may reference.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
