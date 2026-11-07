

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AnnModeNprobe(UniversalBaseModel):
    """
    Search only in the clusters with the highest similarity scores to the query vector.
    The number of clusters to search is specified by the n-probe parameter.
    You cannot directly set a specific, guaranteed recall number (e.g., "always give me 95% recall@10"). There is no one-fits-all, there is no automatism.
    Instead, you manually tune parameters that control the tradeoff between query latency and accuracy.
    Because recall depends heavily on the structure of your specific data (distribution, dimensionality, and clustering) and queries,
    there is always a trial-and-error (benchmarking) phase required to determine the right settings for your data.
    Examples:
    wikipedia, VectorSimilarity::Dot, dimensions: 64, Precision::F32, Clustering::Auto, Clustering::I8, recall@10=95% -> Nprobe(55)
    wikipedia, VectorSimilarity::Dot, dimensions: 64, Precision::F32, Clustering::Auto, Clustering::I8, recall@10=99% -> Nprobe(140)
    sift1m, VectorSimilarity::Euclidean, dimensions: 128, Precision::F32, Clustering::Auto, Quantization::None, recall@10=95% -> Nprobe(11)
    sift1m, VectorSimilarity::Euclidean, dimensions: 128, Precision::F32, Clustering::Auto, Quantization::None, recall@10=99% -> Nprobe(22)
    """

    nprobe: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Nprobe"),
        pydantic.Field(
            alias="Nprobe",
            description='Search only in the clusters with the highest similarity scores to the query vector.\nThe number of clusters to search is specified by the n-probe parameter.\nYou cannot directly set a specific, guaranteed recall number (e.g., "always give me 95% recall@10"). There is no one-fits-all, there is no automatism.\nInstead, you manually tune parameters that control the tradeoff between query latency and accuracy.\nBecause recall depends heavily on the structure of your specific data (distribution, dimensionality, and clustering) and queries,\nthere is always a trial-and-error (benchmarking) phase required to determine the right settings for your data.\nExamples:\nwikipedia, VectorSimilarity::Dot, dimensions: 64, Precision::F32, Clustering::Auto, Clustering::I8, recall@10=95% -> Nprobe(55)\nwikipedia, VectorSimilarity::Dot, dimensions: 64, Precision::F32, Clustering::Auto, Clustering::I8, recall@10=99% -> Nprobe(140)\nsift1m, VectorSimilarity::Euclidean, dimensions: 128, Precision::F32, Clustering::Auto, Quantization::None, recall@10=95% -> Nprobe(11)\nsift1m, VectorSimilarity::Euclidean, dimensions: 128, Precision::F32, Clustering::Auto, Quantization::None, recall@10=99% -> Nprobe(22)',
        ),
    ]
    """
    Search only in the clusters with the highest similarity scores to the query vector.
    The number of clusters to search is specified by the n-probe parameter.
    You cannot directly set a specific, guaranteed recall number (e.g., "always give me 95% recall@10"). There is no one-fits-all, there is no automatism.
    Instead, you manually tune parameters that control the tradeoff between query latency and accuracy.
    Because recall depends heavily on the structure of your specific data (distribution, dimensionality, and clustering) and queries,
    there is always a trial-and-error (benchmarking) phase required to determine the right settings for your data.
    Examples:
    wikipedia, VectorSimilarity::Dot, dimensions: 64, Precision::F32, Clustering::Auto, Clustering::I8, recall@10=95% -> Nprobe(55)
    wikipedia, VectorSimilarity::Dot, dimensions: 64, Precision::F32, Clustering::Auto, Clustering::I8, recall@10=99% -> Nprobe(140)
    sift1m, VectorSimilarity::Euclidean, dimensions: 128, Precision::F32, Clustering::Auto, Quantization::None, recall@10=95% -> Nprobe(11)
    sift1m, VectorSimilarity::Euclidean, dimensions: 128, Precision::F32, Clustering::Auto, Quantization::None, recall@10=99% -> Nprobe(22)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
