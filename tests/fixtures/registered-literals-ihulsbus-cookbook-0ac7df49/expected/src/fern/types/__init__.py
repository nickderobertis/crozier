



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .paginated_category_response import PaginatedCategoryResponse
    from .paginated_cuisine_type_response import PaginatedCuisineTypeResponse
    from .paginated_difficulty_level_response import PaginatedDifficultyLevelResponse
    from .paginated_image_response import PaginatedImageResponse
    from .paginated_ingredient_response import PaginatedIngredientResponse
    from .paginated_preparation_time_response import PaginatedPreparationTimeResponse
    from .paginated_recipe_response import PaginatedRecipeResponse
    from .paginated_tag_response import PaginatedTagResponse
    from .paginated_unit_response import PaginatedUnitResponse
    from .pagination_metadata import PaginationMetadata
_dynamic_imports: typing.Dict[str, str] = {
    "PaginatedCategoryResponse": ".paginated_category_response",
    "PaginatedCuisineTypeResponse": ".paginated_cuisine_type_response",
    "PaginatedDifficultyLevelResponse": ".paginated_difficulty_level_response",
    "PaginatedImageResponse": ".paginated_image_response",
    "PaginatedIngredientResponse": ".paginated_ingredient_response",
    "PaginatedPreparationTimeResponse": ".paginated_preparation_time_response",
    "PaginatedRecipeResponse": ".paginated_recipe_response",
    "PaginatedTagResponse": ".paginated_tag_response",
    "PaginatedUnitResponse": ".paginated_unit_response",
    "PaginationMetadata": ".pagination_metadata",
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
]
