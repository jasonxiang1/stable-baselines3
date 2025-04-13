"""
Example script to train and evaluate a DQN agent on the LunarLander-v3 environment.

This script demonstrates the basic usage of the stable-baselines3 library
for training a Deep Q-Network (DQN) agent on the LunarLander-v3 environment
from Gymnasium. It includes steps for environment creation, agent instantiation,
training, saving and loading the trained agent, evaluation, and visualization
of the agent's performance.
"""
import gymnasium as gym

from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy

import matplotlib.pyplot as plt

# Create environment
env = gym.make("LunarLander-v3", render_mode="rgb_array")

# Instantiate the agent
model = DQN("MlpPolicy", env, verbose=1)
# Train the agent and display a progress bar
model.learn(total_timesteps=int(2e3), progress_bar=True)
# Save the agent
model.save("dqn_lunar")
del model  # delete trained model to demonstrate loading

# Load the trained agent
# NOTE: if you have loading issue, you can pass `print_system_info=True`
# to compare the system on which the model was trained vs the current one
# model = DQN.load("dqn_lunar", env=env, print_system_info=True)
model = DQN.load("dqn_lunar", env=env)

# Evaluate the agent
# NOTE: If you use wrappers with your environment that modify rewards,
#       this will be reflected here. To evaluate with original rewards,
#       wrap environment in a "Monitor" wrapper before other wrappers.
mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

# Enjoy trained agent
vec_env = model.get_env()
obs = vec_env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = vec_env.step(action)
    plt.imshow(vec_env.render("rgb_array"))
    plt.savefig('test.png')
