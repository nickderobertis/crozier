

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_versions_response_item_attributes import FilesVersionsResponseItemAttributes
from .files_versions_response_item_links import FilesVersionsResponseItemLinks


class FilesVersionsResponseItem(UniversalBaseModel):
    attributes: typing.Optional[FilesVersionsResponseItemAttributes] = pydantic.Field(default=None)
    """
    The properties of the file versions entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the file version.
    """

    links: typing.Optional[FilesVersionsResponseItemLinks] = pydantic.Field(default=None)
    """
    Links to alternative representations of the file version entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the file versions entity (`file_versions`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
