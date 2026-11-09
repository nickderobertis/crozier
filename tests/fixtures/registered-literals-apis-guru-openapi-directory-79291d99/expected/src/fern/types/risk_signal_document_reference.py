

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RiskSignalDocumentReference(UniversalBaseModel):
    """
    Object containing metadata for the document
    """

    document_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An identifier of the document referenced by the document metadata.
    """

    document_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
