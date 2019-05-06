import numpy as np
import gym
from keras import models
from IPython import embed

env = gym.make('MountainCar-v0')

#play 20 times
#load the network
model=models.load_model('trainedModel/trainNetworkInEPS399.h5')

for i_episode in range(20):
    currentState = env.reset().reshape(1, 2)

    print("============================================")
    embed()
    rewardSum=0
    for t in range(200):
        env.render()
        action = np.argmax(model.predict(currentState)[0])

        new_state, reward, done, info = env.step(action)

        new_state = new_state.reshape(1, 2)

        currentState=new_state

        rewardSum+=reward
        if done:
            print("Episode finished after {} timesteps reward is {}".format(t+1,rewardSum))
            break