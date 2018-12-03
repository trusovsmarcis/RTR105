Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /home/user/RTR105/MonteCarlo_1.py =================

========================
Random Number Generation
========================

==================== =========================================================
Utility functions
==============================================================================
random_sample        Uniformly distributed floats over ``[0, 1)``.
random               Alias for `random_sample`.
bytes                Uniformly distributed random bytes.
random_integers      Uniformly distributed integers in a given range.
permutation          Randomly permute a sequence / generate a random sequence.
shuffle              Randomly permute a sequence in place.
seed                 Seed the random number generator.
choice               Random sample from 1-D array.

==================== =========================================================

==================== =========================================================
Compatibility functions
==============================================================================
rand                 Uniformly distributed values.
randn                Normally distributed values.
ranf                 Uniformly distributed floating point numbers.
randint              Uniformly distributed integers in a given range.
==================== =========================================================

==================== =========================================================
Univariate distributions
==============================================================================
beta                 Beta distribution over ``[0, 1]``.
binomial             Binomial distribution.
chisquare            :math:`\chi^2` distribution.
exponential          Exponential distribution.
f                    F (Fisher-Snedecor) distribution.
gamma                Gamma distribution.
geometric            Geometric distribution.
gumbel               Gumbel distribution.
hypergeometric       Hypergeometric distribution.
laplace              Laplace distribution.
logistic             Logistic distribution.
lognormal            Log-normal distribution.
logseries            Logarithmic series distribution.
negative_binomial    Negative binomial distribution.
noncentral_chisquare Non-central chi-square distribution.
noncentral_f         Non-central F distribution.
normal               Normal / Gaussian distribution.
pareto               Pareto distribution.
poisson              Poisson distribution.
power                Power distribution.
rayleigh             Rayleigh distribution.
triangular           Triangular distribution.
uniform              Uniform distribution.
vonmises             Von Mises circular distribution.
wald                 Wald (inverse Gaussian) distribution.
weibull              Weibull distribution.
zipf                 Zipf's distribution over ranked data.
==================== =========================================================

==================== =========================================================
Multivariate distributions
==============================================================================
dirichlet            Multivariate generalization of Beta distribution.
multinomial          Multivariate generalization of the binomial distribution.
multivariate_normal  Multivariate generalization of the normal distribution.
==================== =========================================================

==================== =========================================================
Standard distributions
==============================================================================
standard_cauchy      Standard Cauchy-Lorentz distribution.
standard_exponential Standard exponential distribution.
standard_gamma       Standard Gamma distribution.
standard_normal      Standard normal distribution.
standard_t           Standard Student's t-distribution.
==================== =========================================================

==================== =========================================================
Internal functions
==============================================================================
get_state            Get tuple representing internal state of generator.
set_state            Set state of generator.
==================== =========================================================


>>> 
================= RESTART: /home/user/RTR105/MonteCarlo_1.py =================

Traceback (most recent call last):
  File "/home/user/RTR105/MonteCarlo_1.py", line 9, in <module>
    print(random.unifrom.__doc__)
AttributeError: 'module' object has no attribute 'unifrom'
>>> 
================= RESTART: /home/user/RTR105/MonteCarlo_1.py =================

        uniform(low=0.0, high=1.0, size=None)

        Draw samples from a uniform distribution.

        Samples are uniformly distributed over the half-open interval
        ``[low, high)`` (includes low, but excludes high).  In other words,
        any value within the given interval is equally likely to be drawn
        by `uniform`.

        Parameters
        ----------
        low : float, optional
            Lower boundary of the output interval.  All values generated will be
            greater than or equal to low.  The default value is 0.
        high : float
            Upper boundary of the output interval.  All values generated will be
            less than high.  The default value is 1.0.
        size : int or tuple of ints, optional
            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
            ``m * n * k`` samples are drawn.  Default is None, in which case a
            single value is returned.

        Returns
        -------
        out : ndarray
            Drawn samples, with shape `size`.

        See Also
        --------
        randint : Discrete uniform distribution, yielding integers.
        random_integers : Discrete uniform distribution over the closed
                          interval ``[low, high]``.
        random_sample : Floats uniformly distributed over ``[0, 1)``.
        random : Alias for `random_sample`.
        rand : Convenience function that accepts dimensions as input, e.g.,
               ``rand(2,2)`` would generate a 2-by-2 array of floats,
               uniformly distributed over ``[0, 1)``.

        Notes
        -----
        The probability density function of the uniform distribution is

        .. math:: p(x) = \frac{1}{b - a}

        anywhere within the interval ``[a, b)``, and zero elsewhere.

        Examples
        --------
        Draw samples from the distribution:

        >>> s = np.random.uniform(-1,0,1000)

        All values are within the given interval:

        >>> np.all(s >= -1)
        True
        >>> np.all(s < 0)
        True

        Display the histogram of the samples, along with the
        probability density function:

        >>> import matplotlib.pyplot as plt
        >>> count, bins, ignored = plt.hist(s, 15, normed=True)
        >>> plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
        >>> plt.show()

        
>>> random.uniform(5)
2.3577452712890272
>>> random.uniform(5)
3.6924122469751897
>>> random.uniform(25,30)
28.740482251978563
>>> random.seed(1)
>>> random.uniform(25,30)
27.08511002351287
>>> random.uniform(25,30)
28.60162246721079
>>> random.uniform(25,30)
25.000571874086724
>>> random.seed(1)
>>> random.uniform(25,30)
27.08511002351287
>>> random.uniform(0,5,100)
array([  3.60162247e+00,   5.71874087e-04,   1.51166286e+00,
         7.33779454e-01,   4.61692974e-01,   9.31301057e-01,
         1.72780364e+00,   1.98383737e+00,   2.69408367e+00,
         2.09597257e+00,   3.42609750e+00,   1.02226125e+00,
         4.39058718e+00,   1.36937966e-01,   3.35233755e+00,
         2.08652401e+00,   2.79344914e+00,   7.01934693e-01,
         9.90507445e-01,   4.00372284e+00,   4.84130788e+00,
         1.56712089e+00,   3.46161308e+00,   4.38194576e+00,
         4.47303332e+00,   4.25221057e-01,   1.95273916e-01,
         8.49152098e-01,   4.39071252e+00,   4.91734169e-01,
         2.10553813e+00,   4.78944765e+00,   2.66582642e+00,
         3.45938557e+00,   1.57757816e+00,   3.43250464e+00,
         4.17312836e+00,   9.14413867e-02,   3.75072157e+00,
         4.94430544e+00,   3.74082827e+00,   1.40221996e+00,
         3.94639664e+00,   5.16130033e-01,   2.23946763e+00,
         4.54297752e+00,   1.46807074e+00,   1.43887669e+00,
         6.50142861e-01,   9.68347894e-02,   3.39417766e+00,
         1.05814058e+00,   1.32773330e+00,   2.45786580e+00,
         2.66812726e-01,   2.87058803e+00,   7.33642875e-01,
         2.94652768e+00,   3.49879180e+00,   5.11672144e-01,
         2.07027994e+00,   3.47200079e+00,   2.07089635e+00,
         2.49767295e-01,   2.67948203e+00,   3.31897323e+00,
         2.57444556e+00,   4.72297378e+00,   2.93277520e+00,
         4.51700958e+00,   6.87373521e-01,   6.96381736e-01,
         4.03695644e+00,   1.98838418e+00,   8.26770986e-01,
         4.63754290e+00,   1.73882930e+00,   3.75406052e+00,
         3.62998993e+00,   4.41653046e+00,   3.11836104e+00,
         3.75471217e+00,   1.74449171e+00,   1.34963946e+00,
         4.47943109e+00,   2.14045595e+00,   4.82420024e+00,
         3.31720749e+00,   3.10847860e+00,   5.73729865e-01,
         4.74744629e+00,   2.24956067e+00,   2.89194807e+00,
         2.04068401e+00,   1.18513490e+00,   4.51689760e+00,
         2.86839743e+00,   1.43516352e-02,   3.08572457e+00,
         1.63322451e+00])
>>> random.uniform(0,5,10)
array([ 2.63529051,  4.4297105 ,  1.7863488 ,  4.54267575,  3.11680058,
        0.07910621,  4.64718617,  3.45448459,  4.98661425,  0.86170254])
>>> 
================= RESTART: /home/user/RTR105/MonteCarlo_1.py =================
[24, 16, 0, 21, 39]
>>> 
================= RESTART: /home/user/RTR105/MonteCarlo_1.py =================
[203, 186, 0, 212, 399]
>>> 
================= RESTART: /home/user/RTR105/MonteCarlo_1.py =================
[182, 217, 0, 202, 399]
>>> 
================= RESTART: /home/user/RTR105/MonteCarlo_1.py =================

Warning (from warnings module):
  File "/usr/lib/python2.7/dist-packages/matplotlib/font_manager.py", line 273
    warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
12.4775
>>> 
