# @Time : 13:10
# @Author : Yao Zhao
# @File:  Frame
# All the code was done by Yao Zhao, a PhD student of Hong Kong Polytechnic University(Polyu)
# you can connect me by E-mail
# 22117696r@connect.polyu.hk

from matplotlib import pyplot as plt
from track_function import plot_tennis_trajectory_rotate, plot_tennis_trajectory_No_rotate
import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_tennis_rotate():
    height = float(height_entry.get())
    x_position = float(x_entry.get())
    angle_x = float(angle_entry_x.get())
    angle_z = float(angle_entry_z.get())
    v = float(v_entry.get())

    angle_x_pai = np.pi * angle_x / 180
    angle_z_pai = np.pi * angle_z / 180


    # initial value
    initial = [x_position, 0.0, height]
    initial_v = [v * np.cos(angle_z_pai) * np.cos(angle_x_pai)]
    track = plot_tennis_trajectory_rotate(x_position, 0.0, height, v * np.cos(angle_z_pai) * np.cos(angle_x_pai), v * np.cos(angle_z_pai)* np.sin(angle_x_pai), v*np.sin(angle_z_pai))
    track = track[[not np.all(track[i] == 0) for i in range(track.shape[0])], :]

    ax.cla()

    # 绘制三维轨迹图
    ax.plot3D(track[:,0], track[:,1], track[:,2])
    # ax.plot([0, court_width, court_width, 0, 0], [0, 0, court_length, court_length, 0], [0, 0, 0, 0, 0], 'k-')  # 地面
    ax.plot([0, court_width, court_width, 0, 0], [0, 0, court_length, court_length, 0], [0, 0, 0, 0, 0], 'k-')  # 地面
    ax.plot([0, 0, court_width, court_width, 0],
            [court_length / 2, court_length / 2, court_length / 2, court_length / 2, court_length / 2],
            [0, 1.07, 1.07, 0, 0], 'k-')  # 网

    ax.set_xlim(0, court_width)
    ax.set_ylim(0, court_length)
    ax.set_zlim(0, 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # ax.plot([0, court_length, court_length, 0, 0], [0, 0, court_width, court_width, 0], [0, 0, 0, 0, 0], 'k-')  # 地面
    plt.gca().set_box_aspect((court_width, court_length, 2))  # 当x、y、z轴范围之比为3:5:2时。
    plt.axis('off')
    ax.view_init(elev=20, azim=-45)

    ax.set_title('Tennis Trajectory with rotating')

def plot_tennis_without_rotate():
    height = float(height_entry.get())
    x_position = float(x_entry.get())
    angle_x = float(angle_entry_x.get())
    angle_z = float(angle_entry_z.get())
    v = float(v_entry.get())

    angle_x_pai = np.pi * angle_x / 180
    angle_z_pai = np.pi * angle_z / 180


    # initial value
    initial = [x_position, 0.0, height]
    initial_v = [v * np.cos(angle_z_pai) * np.cos(angle_x_pai)]
    track = plot_tennis_trajectory_No_rotate(x_position, 0.0, height, v * np.cos(angle_z_pai) * np.cos(angle_x_pai), v * np.cos(angle_z_pai)* np.sin(angle_x_pai), v*np.sin(angle_z_pai))
    track = track[[not np.all(track[i] == 0) for i in range(track.shape[0])], :]

    ax.cla()

    # 绘制三维轨迹图
    ax.plot3D(track[:,0], track[:,1], track[:,2])
    # ax.plot([0, court_width, court_width, 0, 0], [0, 0, court_length, court_length, 0], [0, 0, 0, 0, 0], 'k-')  # 地面
    ax.plot([0, court_width, court_width, 0, 0], [0, 0, court_length, court_length, 0], [0, 0, 0, 0, 0], 'k-')  # 地面
    ax.plot([0, 0, court_width, court_width, 0],
            [court_length / 2, court_length / 2, court_length / 2, court_length / 2, court_length / 2],
            [0, 1.07, 1.07, 0, 0], 'k-')  # 网

    ax.set_xlim(0, court_width)
    ax.set_ylim(0, court_length)
    ax.set_zlim(0, 2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # ax.plot([0, court_length, court_length, 0, 0], [0, 0, court_width, court_width, 0], [0, 0, 0, 0, 0], 'k-')  # 地面
    plt.gca().set_box_aspect((court_width, court_length, 2))  # 当x、y、z轴范围之比为3:5:2时。
    plt.axis('off')
    # plt.zticks([])
    ax.view_init(elev=20, azim=-45)

    ax.set_title('Tennis Trajectory without rotating')

 # 创建主窗口
window = tk.Tk()
window.title("用户交互界面")

# 创建左侧Frame
left_frame = tk.Frame(window)
left_frame.pack(side="left")

# 创建右侧Frame
right_frame = tk.Frame(window)
right_frame.pack(side="right")

# 建立网球场，以x为底线，此时y = 0

# 在左侧Frame中创建标签和输入框：高度
height_label = tk.Label(left_frame, text="Please enter the hit height(unit: m):")
height_label.pack()

height_entry = tk.Entry(left_frame)
height_entry.pack()

# 在左侧Frame中创建标签和输入框：位置
x_label = tk.Label(left_frame, text="Please enter the hit position(unit: m):")
x_label.pack()

x_entry = tk.Entry(left_frame)
x_entry.pack()

# 在左侧Frame中创建标签和输入框：竖直击球角度
angle_label_x = tk.Label(left_frame, text="Please enter the hit angle_x:")
angle_label_x.pack()

angle_entry_x = tk.Entry(left_frame)
angle_entry_x.pack()

# 在左侧Frame中创建标签和输入框：竖直击球角度
angle_label_z = tk.Label(left_frame, text="Please enter the hit angle_z:")
angle_label_z.pack()

angle_entry_z = tk.Entry(left_frame)
angle_entry_z.pack()

# 在左侧Frame中创建标签和输入框：击球速度
v_label = tk.Label(left_frame, text="Please enter the hit v:")
v_label.pack()

v_entry = tk.Entry(left_frame)
v_entry.pack()

# 在左侧Frame中创建按钮
plot_button = tk.Button(left_frame, text="Tennis Trajectory with rotating", command=plot_tennis_rotate)
plot_button.pack()

# 在左侧Frame中创建按钮
plot_button = tk.Button(left_frame, text="Tennis Trajectory without rotating", command=plot_tennis_without_rotate)
plot_button.pack()
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# 网球场数据
court_width = 10.97
court_length = 23.78

# 创建画布和图形对象
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot([0, court_width, court_width, 0, 0], [0, 0, court_length, court_length, 0], [0, 0, 0, 0, 0], 'k-')  # 地面
ax.plot([0, 0, court_width, court_width, 0], [court_length/2, court_length/2, court_length/2, court_length/2, court_length/2], [0, 1.07, 1.07, 0, 0], 'k-')  # 地面
# ax.plot([1.37, court_width, court_width, 0, 0], [0, 0, court_length, court_length, 0], [0, 0, 0, 0, 0], 'k-')  # 地面

ax.set_xlim(0, court_width)
ax.set_ylim(0, court_length)
ax.set_zlim(0, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# ax.plot([0, court_length, court_length, 0, 0], [0, 0, court_width, court_width, 0], [0, 0, 0, 0, 0], 'k-')  # 地面
plt.gca().set_box_aspect((court_width, court_length, 2))  # 当x、y、z轴范围之比为3:5:2时。
plt.axis('off')
# 设置初始视角
ax.view_init(elev=20, azim=-45)

# 创建绘图区域
canvas = FigureCanvasTkAgg(fig, right_frame)
canvas.draw()
canvas.get_tk_widget().pack()

# 运行界面
window.mainloop()
