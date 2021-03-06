# Trained A Neural Network To Play 2048 using Deep-Reinforcement Learning
## Dependencies
To play the game with pretrained model:
* Python 3++ (Python2 can also be used but requires additional tinkering the code)
* TensorFlow 2.0 (TensorFlow 1 can also be used but requires additional tinkering the code)   
* Tkinter (should come with python 3)

To train:
* Jupyter notebook

## How to run
```
git clone https://github.com/moonmedtwo/PractionerProject.git
python Code/GamePlay.py
```

## Poster
| **Title**      |Deep Q-learning net plays 2048 game|
| ---------- |-------------------|
| **Team**       |Vu Quoc Anh - moonmtwo@gmail.com|
| **Predicting** | 2048 is a simple yet addictive puzzle game which has an objective is to combine equal-value and adjacent grids to a bigger one until reaching the value of 2048 to win, else the game is considered over when there is no more available grids to combine. According to the game creator, only 5% of total games played achieved 2048.<br/> The input is the current state of the game and the output are 4 possible moves: go up-down-right-left|
| **Data**       | The raw data consists of a grid of 4x4 tiles, each tile carries a value of 2 power N (N ranges from 0 to 15 theoretically). The raw data is then normalized into a cube of 4x4x16. Data is acquired simutaneously along training phase, and is labeled according to the gained reward of current action and maximum Q point of next state.|
| **Features**   | The features come from chosen kernels and the training of the network. |
| **Models**     | This network uses a Deep Q-learning model. Please find below the model architecture's image. In short, the model consists of 2 convolution layers and a fully connected layer at the end. All layers' outputs go through a ReLU activation function and the optimizers used is RMSProp. <br/> Loss function used is MSE loss: <br/><img src="https://render.githubusercontent.com/render/math?math=\zeta(\delta) = \frac{1}{2} \times {\delta}^2"/> <br/> where <img src="https://render.githubusercontent.com/render/math?math=\delta"> is temporal difference:<br/> <img src="https://render.githubusercontent.com/render/math?math=\delta=Q(s,a)-(\gamma\times\max_{a}(Q(s',a)) %2B r)"> <br/> The policies for rewards are combined of: reward when generating higher value tile, if a move generated a tile with new maximum value <img src="https://render.githubusercontent.com/render/math?math=r%2b=0.1\times\log_2(newMax)"> else <img src="https://render.githubusercontent.com/render/math?math=r%2b=0">; and reward when maximizing number of empty cells/tiles<img src="https://render.githubusercontent.com/render/math?math=r%2B=NnextEmptyCells - NcurEmptyCells">|
| **Discussion** |The 2048 game is not entirely deterministic, as a tile is randomly spawn after each move with random value. This makes a Q-learning model is not ideally suitable to play the game, thus even for a long-trained model, we cannot guarantee it to win every game. However, the more trainings we do, we can assure the higher chance for the model to win the game. <br/> One big down side of this model is that it requires a lot of trainings, around 5 hours to reach 20000 episodes to have its first win.|
| **Future**     |Tune the kernels so that it requires less training time but still preserves the performance. <br/> Apply Double Q Learning which may improve the stability of the model (A trained model should be able to win the game everytime)|
|**References**  |[1] https://github.com/navjindervirdee/2048-deep-reinforcement-learning <br/> [2] http://web.stanford.edu/class/archive/cs/cs221/cs221.1192/2018/restricted/posters/cwang17/poster.pdf  <br/> [3] https://cs.uwaterloo.ca/~mli/zalevine-dqn-2048.pdf |
| **Results**    ||

## Network Architecture
![](https://github.com/navjindervirdee/2048-deep-reinforcement-learning/blob/master/Architecture/Architecture.JPG?raw=true)
