"""Spearman's correlation coefficient."""
from scipy.stats import spearmanr


def Spearman(poly, dist, sample=10000, retall=False, **kws):
    """
    Calculate Spearman's rank-order correlation coefficient.

    Args:
        poly (Poly) :
            Polynomial of interest.
        dist (Dist) :
            Defines the space where correlation is taken.
        sample (int) :
            Number of samples used in estimation.
        retall (bool) :
            If true, return p-value as well.
        **kws (optional) :
            Extra keywords passed to dist.sample.

    Returns:
        rho (float, ndarray) :
            Correlation output. Of type float if two-dimensional problem.
            Correleation matrix if larger.
        p-value (optional, float, ndarray) :
            The two-sided p-value for a hypothesis test whose null hypothesis
            is that two sets of data are uncorrelated, has same dimension as
            rho.
    """
    samples = dist.sample(sample, **kws)
    poly = polynomials.flatten(poly)
    Y = poly(*samples)
    if retall:
        return spearmanr(Y.T)
    return spearmanr(Y.T)[0]
