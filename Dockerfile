# 使用轻量的 Python 镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /jieba

# 先复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制脚本文件
COPY jieba.py .

# 容器启动时运行测试脚本
CMD ["python", "jieba.py"]