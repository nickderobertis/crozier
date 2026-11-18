

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PagePostResponseDataAnnotationsAnnotationsItemReferenceAttributes(UniversalBaseModel):
    notebook_page_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="notebookPageId"), pydantic.Field(alias="notebookPageId")
    ]
    notebook_uuid: typing_extensions.Annotated[
        str, FieldMetadata(alias="notebookUuid"), pydantic.Field(alias="notebookUuid")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
