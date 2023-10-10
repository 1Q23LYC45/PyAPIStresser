# PyAPIStresser
一个基于Python3的API压力测试工具。仅支持单个参数。支持GET。支持多进程并发。
# 依赖
python3.4+  
request库
# 用法
python pyapistresser.py  
输入目标URL，类似http://127.0.0.1/?key=这样的  
或者http://127.0.0.1/key/这样的  
最后空出来参数即可，软件使用随机数作为参数请求  
Ctrl+C停止测试