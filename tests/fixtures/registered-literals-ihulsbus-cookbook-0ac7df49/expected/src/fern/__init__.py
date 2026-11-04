



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PaginatedCategoryResponse,
        PaginatedCuisineTypeResponse,
        PaginatedDifficultyLevelResponse,
        PaginatedImageResponse,
        PaginatedIngredientResponse,
        PaginatedPreparationTimeResponse,
        PaginatedRecipeResponse,
        PaginatedTagResponse,
        PaginatedUnitResponse,
        PaginationMetadata,
    )
    from .errors import BadRequestError, ForbiddenError, InternalServerError, NotFoundError, UnauthorizedError
    from . import (
        amount,
        category,
        cuisinetype,
        difficultylevel,
        error,
        image,
        ingredient,
        instruction,
        metadata,
        preparationtime,
        recipe,
        search,
        tag,
        unit,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .amount import IngredientAmounts
    from .category import Category
    from .client import AsyncFernApi, FernApi
    from .cuisinetype import CuisineType
    from .difficultylevel import DifficultyLevel
    from .environment import FernApiEnvironment
    from .error import Error
    from .image import CreateImageRequestEntityType, ImageData
    from .ingredient import Ingredient
    from .instruction import Instruction, InstructionSearch
    from .metadata import MetadataSearchResponse
    from .preparationtime import PreparationTime
    from .recipe import Recipe
    from .search import GlobalSearchResponse
    from .tag import Tag
    from .unit import Unit
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Category": ".category",
    "CreateImageRequestEntityType": ".image",
    "CuisineType": ".cuisinetype",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DifficultyLevel": ".difficultylevel",
    "Error": ".error",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "GlobalSearchResponse": ".search",
    "ImageData": ".image",
    "Ingredient": ".ingredient",
    "IngredientAmounts": ".amount",
    "Instruction": ".instruction",
    "InstructionSearch": ".instruction",
    "InternalServerError": ".errors",
    "MetadataSearchResponse": ".metadata",
    "NotFoundError": ".errors",
    "PaginatedCategoryResponse": ".types",
    "PaginatedCuisineTypeResponse": ".types",
    "PaginatedDifficultyLevelResponse": ".types",
    "PaginatedImageResponse": ".types",
    "PaginatedIngredientResponse": ".types",
    "PaginatedPreparationTimeResponse": ".types",
    "PaginatedRecipeResponse": ".types",
    "PaginatedTagResponse": ".types",
    "PaginatedUnitResponse": ".types",
    "PaginationMetadata": ".types",
    "PreparationTime": ".preparationtime",
    "Recipe": ".recipe",
    "Tag": ".tag",
    "UnauthorizedError": ".errors",
    "Unit": ".unit",
    "__version__": ".version",
    "amount": ".amount",
    "category": ".category",
    "cuisinetype": ".cuisinetype",
    "difficultylevel": ".difficultylevel",
    "error": ".error",
    "image": ".image",
    "ingredient": ".ingredient",
    "instruction": ".instruction",
    "metadata": ".metadata",
    "preparationtime": ".preparationtime",
    "recipe": ".recipe",
    "search": ".search",
    "tag": ".tag",
    "unit": ".unit",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AsyncFernApi",
    "BadRequestError",
    "Category",
    "CreateImageRequestEntityType",
    "CuisineType",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DifficultyLevel",
    "Error",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "GlobalSearchResponse",
    "ImageData",
    "Ingredient",
    "IngredientAmounts",
    "Instruction",
    "InstructionSearch",
    "InternalServerError",
    "MetadataSearchResponse",
    "NotFoundError",
    "PaginatedCategoryResponse",
    "PaginatedCuisineTypeResponse",
    "PaginatedDifficultyLevelResponse",
    "PaginatedImageResponse",
    "PaginatedIngredientResponse",
    "PaginatedPreparationTimeResponse",
    "PaginatedRecipeResponse",
    "PaginatedTagResponse",
    "PaginatedUnitResponse",
    "PaginationMetadata",
    "PreparationTime",
    "Recipe",
    "Tag",
    "UnauthorizedError",
    "Unit",
    "__version__",
    "amount",
    "category",
    "cuisinetype",
    "difficultylevel",
    "error",
    "image",
    "ingredient",
    "instruction",
    "metadata",
    "preparationtime",
    "recipe",
    "search",
    "tag",
    "unit",
]
