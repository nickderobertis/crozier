

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1bulk_import_response_errors import V1BulkImportResponseErrors


class V1BulkImportResponse(UniversalBaseModel):
    deleted_ids: typing.List[int] = pydantic.Field()
    """
    IDs of successfully deleted entries
    """

    created_ids: typing.List[int] = pydantic.Field()
    """
    IDs of successfully created entries
    """

    updated_ids: typing.List[int] = pydantic.Field()
    """
    IDs of successfully updated entries
    """

    errors: V1BulkImportResponseErrors = pydantic.Field()
    """
    Errors encountered during import
    """

    job: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Job details if operation is asynchronous (100+ records)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
