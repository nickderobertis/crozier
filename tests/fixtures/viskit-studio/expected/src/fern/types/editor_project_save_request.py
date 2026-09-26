

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EditorProjectSaveRequest(UniversalBaseModel):
    document: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Versioned ViskitEditorDocument JSON object
    """

    expected_revision: typing.Optional[int] = pydantic.Field(default=None)
    """
    Optimistic concurrency guard; 409 when it differs from stored revision.
    """

    source_image_ref: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional source_images.id backing this project import.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
