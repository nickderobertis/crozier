

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .w2 import W2


class Taxform(UniversalBaseModel):
    """
    Data about an official document used to report the user's income to the IRS.
    """

    doc_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An identifier of the document referenced by the document metadata.
    """

    document_type: str = pydantic.Field()
    """
    The type of tax document. Currently, the only supported value is `w2`.
    """

    w2: typing.Optional[W2] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
