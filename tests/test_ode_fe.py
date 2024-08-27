import numpy as np

from dhavalgos.odes.euler import forward_euler

def test_ode_fe():
    """Test that a linear ODE is solved exactly by the forward Euler method."""
    def exact_solution(t:float, a:float, b:float) -> float:
        return a * t + b

    def deriv_func(y:float, t:float, a:float) -> float:
        return a

    a = 4
    b = -1

    dt = 0.5
    t0 = 0
    tf = 20

    ts, ys = forward_euler(deriv_func, b, t0, tf, dt, a=a)
    actual_ys = [exact_solution(t, a, b) for t in ts]

    diff_ = np.allclose(ys, actual_ys, atol=1e-6, rtol=1e-6)

    assert diff_ == True