from abc import abstractmethod, abstractproperty
import torch.nn as nn
import torch.nn.functional as F

class ACModel(nn.Module):
    @abstractmethod
    def __init__(self, obs_space, action_space):
        pass
        
    @abstractmethod
    def forward(self, obs):
        pass

class RecurrentACModel(nn.Module):
    @abstractmethod
    def __init__(self, obs_space, action_space):
        pass

    @abstractmethod
    def forward(self, obs, state):
        pass
    
    @property
    @abstractmethod
    def state_size(self):
        pass