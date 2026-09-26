

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class DocumentsImportFromRequestSource_Url(UniversalBaseModel):
    """
    Where CloudPDF pulls the bytes from. The two shapes differ in WHO supplies the authority to read, not in which storage vendor holds the file.
    """

    kind: typing.Literal["url"] = "url"
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocumentsImportFromRequestSource_Connection(UniversalBaseModel):
    """
    Where CloudPDF pulls the bytes from. The two shapes differ in WHO supplies the authority to read, not in which storage vendor holds the file.
    """

    kind: typing.Literal["connection"] = "connection"
    connection_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="connectionId"), pydantic.Field(alias="connectionId")
    ]
    key: str
    revision: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocumentsImportFromRequestSource = typing_extensions.Annotated[
    typing.Union[DocumentsImportFromRequestSource_Url, DocumentsImportFromRequestSource_Connection],
    pydantic.Field(discriminator="kind"),
]
