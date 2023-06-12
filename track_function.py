# @Time : 23:33
# @Author : Yao Zhao
# @File:  track_function
# All the code was done by Yao Zhao, a PhD student of Hong Kong Polytechnic University(Polyu)
# you can connect me by E-mail
# 22117696r@connect.polyu.hk

# 引用函数在3.py里

import numpy as np
import matplotlib

def plot_tennis_trajectory_No_rotate(x,y,z, v_x, v_y, v_z):
    # 网球的参数
    mass = 0.057  # 网球的质量，单位：kg
    diameter = 0.067  # 网球的直径，单位：m
    Cd = 0.35  # 空气阻力系数
    A = np.pi * (diameter / 2) ** 2  # 网球的横截面积

    # 重力加速度
    g = 10  # 重力加速度，单位：m/s^2

    # 初始条件
    initial_position = np.array([x, y, z])  # 初始位置 (x, y, z)，单位：m
    initial_velocity = np.array([v_x, v_y, v_z])  # 初始速度 (v_x, v_y, v_z)，单位：m/s, 由角度和初始速度计算得出
    dt = 0.01  # 时间步长，单位：s
    total_time = 10.0  # 总时间，单位：s

    # 计算模拟步数
    num_steps = int(total_time / dt)

    # 初始化数组来存储网球的位置和速度
    positions = np.zeros((num_steps, 3))
    velocities = np.zeros((num_steps, 3))

    # 将初始位置和速度赋值给第一个步数
    positions[0] = initial_position
    velocities[0] = initial_velocity

    for step in range(1, num_steps):
        velocity = velocities[step - 1]
        velocity_magnitude = np.linalg.norm(velocity)
        air_drag = -0.5 * Cd * A * velocity_magnitude * velocity / mass

        # 计算重力的加速度
        gravity = np.array([0.0, 0.0, -g])

        # 计算网球的加速度
        acceleration = gravity + air_drag

        # 使用欧拉方法更新位置和速度
        positions[step] = positions[step - 1] + velocities[step - 1] * dt
        velocities[step] = velocities[step - 1] + acceleration * dt

        if(positions[step][2] < 0):
            break

    return positions

def plot_tennis_trajectory_rotate(x,y,z, v_x, v_y, v_z):
    # 网球的参数
    mass = 0.057  # 网球的质量，单位：kg
    diameter = 0.067  # 网球的直径，单位：m
    Cd = 0.35  # 空气阻力系数
    CL = 0.196
    A = np.pi * (diameter / 2) ** 2  # 网球的横截面积

    # 重力加速度
    g = 9.81  # 重力加速度，单位：m/s^2

    # 初始条件
    initial_position = np.array([x, y, z])  # 初始位置 (x, y, z)，单位：m
    initial_velocity = np.array([v_x, v_y, v_z])  # 初始速度 (v_x, v_y, v_z)，单位：m/s, 由角度和初始速度计算得出
    dt = 0.01  # 时间步长，单位：s
    total_time = 10.0  # 总时间，单位：s

    # 计算模拟步数
    num_steps = int(total_time / dt)

    # 初始化数组来存储网球的位置和速度
    positions = np.zeros((num_steps, 3))
    velocities = np.zeros((num_steps, 3))

    # 将初始位置和速度赋值给第一个步数
    positions[0] = initial_position
    velocities[0] = initial_velocity

    for step in range(1, num_steps):
        speed = np.linalg.norm(velocities[step - 1])
        velocity_unit = velocities[step-1] / speed

        drag = -0.5 * Cd * np.pi * (diameter/2) * (diameter/2) * speed * velocities[step-1]

        # calculate the direction of lift
        perpendicular_vector = np.array([-velocity_unit[1], velocity_unit[0], 0.0])  # 速度方向的垂直向量
        lift_direction = np.cross(velocity_unit, perpendicular_vector)
        lift_unit = lift_direction / np.linalg.norm(lift_direction)

        lift = 0.5 * CL * np.pi * (diameter/2) * (diameter/2) * speed * speed * lift_unit

        gravity = np.array([0.0, 0.0, -mass * 9.8])

        # 计算加速度
        acceleration = (drag + lift + gravity) / mass

        positions[step] = positions[step - 1] + velocities[step - 1] * dt
        velocities[step] = velocities[step - 1] + acceleration * dt

        # 网球落地
        if (positions[step][2] < 0):
            break
    return positions







