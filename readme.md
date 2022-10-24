# Bilibili-Download-Extension

原项目：[here200/Bilibili-Project: 有关Bilibili的项目 (github.com)](https://github.com/here200/Bilibili-Project)

原项目的重构版本。易于使用，扩展性高。

### 功能

- 获取单个用户所有的收藏夹
- 获取单个收藏夹里所有的视频信息
- 根据AV号、BV号，返回一个可以访问的URL地址
- 获取单个视频里的标题、音频链接、视频链接
- 根据单个视频链接，获取它所有的选集标题。
- 下载
  - 下载音频
  - 下载视频（包括音频数据）
    - 使用到 ffmpeg去合成音视频。需要把ffmpeg配置到 环境变量 中。

### 输出日志

请查看 **./ouput_log/***

### 图片（仅供参考，以实物为主）

![image-20221024165901352](images/image-20221024165901352.png)

![image-20221024165944091](images/image-20221024165944091.png)