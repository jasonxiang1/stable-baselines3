"""
Evaluate Humanoid-v5 environment by running a random policy and rendering a frame.

To run file without OpenGL error when initializing the Humanoid environment,
run the following command in terminal:

xvfb-run -a python scripts/lunarlander_test.py

To debug the script with DAP, run the following command:
xvfb-run -a python -m debugpy --listen localhost:5678 scripts/lunarlander_test.py
"""
import gymnasium as gym
import matplotlib.pyplot as plt

env = gym.make("Humanoid-v5", render_mode="rgb_array")
observation, info = env.reset()

episode_over = False
while not episode_over:
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)

    frame = env.render()
    plt.imshow(frame)
    plt.savefig('test.png')
    episode_over = terminated or truncated

env.close()

# xvfb-run -a python -m debugpy --listen localhost:5678 scripts/lunarlander_test.py