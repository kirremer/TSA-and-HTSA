# TSA-HTSA 人体过渡动作识别数据集

## 数据集概述

TSA-HTSA 数据集是一个专注于人体过渡动作识别的传感器数据集，包含完整过渡动作(TSA)和不完整过渡动作(HTSA)两个子集。该数据集使用佩戴在右手腕的惯性传感器采集加速度和角速度数据，适用于人体活动识别、过渡动作检测等研究领域。

## 数据集特点

- **两种数据集**：TSA(完整过渡动作)和HTSA(不完整过渡动作)
- **6类过渡动作**：站到坐、坐到站、坐到躺、躺到坐、站到躺、躺到站
- **传感器数据**：6维特征(3轴加速度+3轴角速度)
- **采样率**：50Hz
- **窗口大小**：128帧(约2.56秒)
- **标准划分**：训练集(60%)和测试集(40%)

## 数据格式

所有数据以NumPy (.npy)格式存储，包含以下文件：

### TSA数据集 (完整过渡动作)

- `X_tsa.npy`: 特征数据，形状为(N, 128, 6)
- `y_tsa.npy`: 标签数据，形状为(N,)
- `X_tsa_train.npy`, `y_tsa_train.npy`: 训练集(60%)
- `X_tsa_test.npy`, `y_tsa_test.npy`: 测试集(40%)

### HTSA数据集 (不完整过渡动作)

- `X_htsa.npy`: 特征数据，形状为(N, 128, 6)
- `y_htsa.npy`: 标签数据，形状为(N,)
- `X_htsa_train.npy`, `y_htsa_train.npy`: 训练集(60%)
- `X_htsa_test.npy`, `y_htsa_test.npy`: 测试集(40%)

## 标签说明

数据集使用以下标签编码：

1. 站到坐 (Standing to Sitting)
2. 坐到站 (Sitting to Standing)
3. 坐到躺 (Sitting to Lying)
4. 躺到坐 (Lying to Sitting)
5. 站到躺 (Standing to Lying)
6. 躺到站 (Lying to Standing)

## HTSA数据集说明

HTSA数据集是基于TSA数据集构建的，包含两种类型的不完整过渡动作：

1. **类型1**: 部分静态活动 + 部分过渡活动，其中过渡活动占整个样本的60%-80%
2. **类型2**: 仅包含原完整过渡活动的60%-80%部分(开始、中间或结束部分)

HTSA数据集保留了80%的完整过渡样本，20%为不完整过渡样本。

## 数据加载示例

```python
import numpy as np

# 加载TSA数据集
X_tsa = np.load('TSA/X_tsa.npy')
y_tsa = np.load('TSA/y_tsa.npy')

# 加载HTSA数据集
X_htsa = np.load('HTSA/X_htsa.npy')
y_htsa = np.load('HTSA/y_htsa.npy')

# 加载训练和测试集
X_tsa_train = np.load('TSA/X_tsa_train.npy')
y_tsa_train = np.load('TSA/y_tsa_train.npy')

print(f"TSA数据集形状: {X_tsa.shape}, {y_tsa.shape}")
print(f"HTSA数据集形状: {X_htsa.shape}, {y_htsa.shape}")
```

## 引用

如使用本数据集，请在您的工作中注明数据来源。
