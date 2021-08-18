import numpy as np
import  matplotlib.pyplot as plt
# mu是目标角度（范围：0到359）， x是当前角度

class OrnsteinUhlenbeckActionNoise:
    def __init__(self,size=1,mu=0.,sigma=400.,theta=4,dt=0.01):
        self.theta=theta
        self.mu=mu
        self.sigma=sigma
        self.dt=dt
        self.size=size

    def reset(self,x=0.):
        # x=self.x_prev+self.theta*(self.mu-self.x_prev)*self.dt+\
        #     self.sigma*np.sqrt(self.dt)*np.random.normal(size=self.mu.shape)
        self.x=x*np.ones(self.size)

    def __call__(self):
        n=np.random.normal(size=self.size)
        self.x+=(self.theta*(self.mu-self.x)*self.dt+self.sigma*np.sqrt(self.dt)*n)

        return self.x

    def __repr__(self):
        return 'OrnsteinUhlenbeckActionNoise(mu={}, sigma={})'.format(self.mu, self.sigma)
