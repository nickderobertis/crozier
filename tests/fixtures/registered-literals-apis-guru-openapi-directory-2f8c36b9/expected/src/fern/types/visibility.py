

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Visibility(UniversalBaseModel):
    public: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Document is publicly readable (if ID4N is owned by the same organization)
    """

    shared_organization_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="sharedOrganizationIds"),
        pydantic.Field(
            alias="sharedOrganizationIds",
            description="Document is readable by these organizations (independend of ID4N ownership)",
        ),
    ] = None
    """
    Document is readable by these organizations (independend of ID4N ownership)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
