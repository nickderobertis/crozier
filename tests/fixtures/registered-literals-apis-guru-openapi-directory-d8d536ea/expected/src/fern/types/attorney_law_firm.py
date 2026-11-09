

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AttorneyLawFirm(UniversalBaseModel):
    """
    Name of the attorney's law firm as provided by Court. This can be null as some Courts do not provide this as a separate field.
    """

    attorney_law_firm_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="attorneyLawFirmId"),
        pydantic.Field(
            alias="attorneyLawFirmId",
            description="ID for the law firm of an attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.",
        ),
    ] = None
    """
    ID for the law firm of an attorney in this case. This ID is unique within a case and NOT across cases. If the same attorney were to appear in another case this ID would be different.
    """

    first_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(
            alias="firstFetchDate", description="Is the date when the document was first fetched from the court site."
        ),
    ]
    """
    Is the date when the document was first fetched from the court site.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(
            alias="isVisible",
            description="Signifies if the attorney as this attorney type is currently isVisible or not for the case.",
        ),
    ]
    """
    Signifies if the attorney as this attorney type is currently isVisible or not for the case.
    """

    last_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(
            alias="lastFetchDate", description="Is the date when the document was last fetched from the court site."
        ),
    ]
    """
    Is the date when the document was last fetched from the court site.
    """

    name: str = pydantic.Field()
    """
    Name of the law firm as provided by Court.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
