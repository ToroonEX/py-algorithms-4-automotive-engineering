from scipy.optimize import minimize
import control
import numpy as np
from matplotlib import pyplot as plt
import os


def find_csv(filename):
    if os.path.isfile(filename):
        file = filename
    else:
        file = '04_mini-projects/' + filename
    return file


wheel_ang = np.genfromtxt(find_csv('wheel_angle.csv'), delimiter=",")
beta = np.genfromtxt(find_csv('beta.csv'), delimiter=",")
psi = np.genfromtxt(find_csv('psi.csv'), delimiter=",")


def plot_input_and_states(psi, beta, title):
    plt.figure()
    plt.plot(wheel_ang[1])
    plt.plot(psi)
    plt.plot(beta)
    plt.legend(
        ["Wheel angle in rad", r"$\dot{\psi}$ in rad per second", r"$\beta$ in rad", ])
    plt.xlabel("time in 1/100 seconds")
    plt.title(title)
    plt.show()


plot_input_and_states(psi=psi[1], beta=beta[1],
                      title="Double lane Simulink model")


def single_track_model(c_f, c_r, l_f, l_r, m, theta, v):
    """
    Vehicle single track model from [p. 230, Schramm2018]
    states = [\dot{psi} in rad/s\\
              beta in rad]
    Args:
        c_f: Front cornering stiffness [N/rad]
        c_r: Rear cornering stiffness [N/rad]
        l_f: Distance CoG to front axles [m]
        l_r: Distance CoG to rear axles [m]
        m: Vehicle mass [kg]
        theta: Vehicle yaw inertia [kgm^2]
        v: Vehicle Speed [m/s]

    Returns:
        state space model
    """
    a_11 = -1 / v * (c_f * l_f ** 2 + c_r * l_r ** 2) / theta
    a_12 = -(c_f * l_f - c_r * l_r) / theta
    a_21 = -1 - 1 / (v ** 2) * (c_f * l_f - c_r * l_r) / m
    a_22 = -1 / v * (c_f + c_r) / m
    a_matrix = np.array([[a_11, a_12], [a_21, a_22]])

    b_1 = (c_f * l_f) / theta
    b_2 = 1 / v * c_f / m
    b_matrix = np.array([[b_1], [b_2]])

    c_matrix = np.array([[1, 0], [0, 1]])
    d_matrix = np.array([[0], [0]])

    return control.ss(a_matrix, b_matrix, c_matrix, d_matrix)


ss_model = single_track_model(
    c_f=12e3, c_r=11e3, l_f=1.4, l_r=1.6, m=2000, theta=4000, v=10)

y, x = control.forced_response(
    ss_model, T=wheel_ang[0], U=wheel_ang[1], X0=np.array([0, 0]))[1:3]

plot_input_and_states(psi=y[0], beta=y[1], title="Single track model")


def validation_plot(y_single_track_model):
    plt.figure()
    plt.plot(psi[1])
    plt.plot(y_single_track_model[0])
    plt.plot(beta[1])
    plt.plot(y_single_track_model[1])
    plt.legend([r"$\dot{\psi}$ reference", r"$\dot{\psi}$ model",
                r"$\beta$ reference", r"$\beta$ model"])
    plt.show()


validation_plot(y)