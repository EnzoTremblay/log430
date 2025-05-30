from numbers import Integral as Integral, Real as Real
from typing import Any, ClassVar, Literal
from typing_extensions import Self

import numpy as np
import scipy.sparse as sp
from numpy import ndarray
from numpy.random import RandomState
from scipy.sparse.linalg import svds as svds

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin
from ..utils import check_array as check_array, check_random_state as check_random_state
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import randomized_svd as randomized_svd, safe_sparse_dot as safe_sparse_dot, svd_flip as svd_flip
from ..utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from ..utils.validation import check_is_fitted as check_is_fitted

__all__ = ["TruncatedSVD"]

class TruncatedSVD(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    singular_values_: ndarray = ...
    explained_variance_ratio_: ndarray = ...
    explained_variance_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: Int = 2,
        *,
        algorithm: Literal["arpack", "randomized"] = "randomized",
        n_iter: Int = 5,
        n_oversamples: Int = 10,
        power_iteration_normalizer: Literal["auto", "QR", "LU", "none"] = "auto",
        random_state: RandomState | None | Int = None,
        tol: Float = 0.0,
    ) -> None: ...
    def fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Self: ...
    def fit_transform(self, X: MatrixLike | ArrayLike, y: Any = None) -> ndarray: ...
    def transform(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def inverse_transform(self, X: MatrixLike) -> ndarray: ...
