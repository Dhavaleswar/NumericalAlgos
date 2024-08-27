import numpy as np

def forward_euler(func: callable, y0: float, t0:float, tf:float, time_step:float, **kwargs) -> tuple:
    """
    Forward Euler method to solve ODEs

    Parameters
    ----------
        func: callable
            The function tact returns the derivative of y at a given y and t, func(y, t, **kwargs)
        y0: float
            the initial condition for y at t0
        t0: float
            the initial time
        tf: float
            the final time
        time_step: float
            the time step size
    Returns
    -------
    tuple
        A tuple containing the time points and the solution to the ODE
    """

    ts = np.arange(t0, tf, time_step)
    ys = np.zeros(len(ts))
    ys[0] = y0

    for i in range(1, len(ts)):
        ys[i] = ys[i-1] + time_step * func(ys[i-1], ts[i-1], **kwargs)

    return ts, ys
