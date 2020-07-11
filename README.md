# Trained A Neural Network To Play 2048 using Deep-Reinforcement Learning

| **Title**      |Deep Q-learning net plays 2048 game|
| ---------- |-------------------|
| **Team**       |Vu Quoc Anh - moonmtwo@gmail.com|
| **Predicting** | 2048 is a simple yet addictive puzzle game which has an objective is to combine equal-value and adjacent grids to a bigger one until reaching the value of 2048 to win, else the game is considered over when there is no more available grids to combine. According to the game creator, only 5% of total games played achieved 2048.<br/> The input is the current state of the game and the output are 4 possible moves: go up-down-right-left|
| **Data**       | The raw data consists of a grid of 4x4 tiles, each tile carries a value of 2 power N (N ranges from 0 to 15 theoretically). The raw data is then normalized into a cube of 4x4x16. Data is acquired simutaneously along training phase, and is labeled according to the gained reward of current action and maximum Q point of next state.|
| **Features**   | The features come from chosen kernels and the training of the network. |
| **Models**     | This network uses a Deep Q-learning model. Please find below the model architecture's image. In short, the model consists of 2 convolution layers and a fully connected layer at the end. All layers' outputs go through a ReLU activation function and the optimizers used is RMSProp. <br/> Loss function used is MSE loss: $ \zeta(\delta) = \frac{1}{2} \times {\delta}^2$ where $ \delta $ is temporal difference: $ \delta = Q(s,a) - (r + \gamma \times \max_{a}(Q(s',a)) $|
| **Discussion** ||
| **Future**     ||
|**References**  ||
| **Results**    ||

## Network Architecture
![](https://github.com/navjindervirdee/2048-deep-reinforcement-learning/blob/master/Architecture/Architecture.JPG?raw=true)
