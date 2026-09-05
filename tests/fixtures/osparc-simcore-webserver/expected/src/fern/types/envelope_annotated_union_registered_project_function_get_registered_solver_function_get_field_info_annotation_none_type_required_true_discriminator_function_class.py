

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .envelope_annotated_union_registered_project_function_get_registered_solver_function_get_field_info_annotation_none_type_required_true_discriminator_function_class_data import (
    EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClassData,
)


class EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass(
    UniversalBaseModel
):
    data: typing.Optional[
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClassData
    ] = None
    error: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
