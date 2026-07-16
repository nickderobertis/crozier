

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod(enum.StrEnum):
    """
    The method used to extract the uncorrelated risk factors from the asset covariance matrix
    """

    PRINCIPAL_COMPONENT_ANALYSIS = "principalComponentAnalysis"
    EXACT_MINIMUM_LINEAR_TORSION = "exactMinimumLinearTorsion"
    APPROXIMATE_MINIMUM_LINEAR_TORSION = "approximateMinimumLinearTorsion"

    def visit(
        self,
        principal_component_analysis: typing.Callable[[], T_Result],
        exact_minimum_linear_torsion: typing.Callable[[], T_Result],
        approximate_minimum_linear_torsion: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod.PRINCIPAL_COMPONENT_ANALYSIS
        ):
            return principal_component_analysis()
        if (
            self
            is PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod.EXACT_MINIMUM_LINEAR_TORSION
        ):
            return exact_minimum_linear_torsion()
        if (
            self
            is PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod.APPROXIMATE_MINIMUM_LINEAR_TORSION
        ):
            return approximate_minimum_linear_torsion()
