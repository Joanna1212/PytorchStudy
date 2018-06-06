# PytorchStudy
记录我的Pytorch学习过程（from 2018.6.6）

参考书籍《深度学习框架-PyTorch入门与实践》

作者：陈云

## 第一章. PyTorch简介

### PyTorch诞生
2017年1月，Facebook提出

### 2. 常见深度学习框架简介

#### Theano
已经停止开发

#### Tensorflow
Google Brain团队2015年提出，静态图
编程接口支持Python和C++
社区强大，适合生产环境

#### Keras
高层神经网络API，使用TensorFlow,Theano,CNTK作为后端
优点：最容易上手，入门简单
缺点：不够灵活（过度封装），几个框架中最慢的一个

#### Caffe/Caffe2
核心语言C++
优点：简介快速
缺点：缺少灵活性（因为设计）
Caffe2:兼具表现力，速度和模块性，强调便携性
文档可能不够完善，性能优异，适合生产环境

#### MXNet
支持很多语言，美男陈天奇
超强的分布式支持，明显的内存、显存优化，适合AWS云平台使用

#### CNTK
社区不够活跃，擅长语音方面的相关研究

### 动态图的未来
动态计算图运行过程中被定义，运行时候构建，可以多次构建多次运行。
优点：直观明了，复核人的思考过程，交互式查看修改，调试更加容易

### PyTorch优点

#### 简洁
遵循三个由低到高的抽象层次
tensor(高位数组/张量)->variable/autograd(自动求导/变量)->nn.Module(神经网络/层模块)

#### 速度
胜于TF和Keras

#### 易用

#### 活跃的社区

Keep it simple, Stupid.
我们开始系统学习PyTorch吧