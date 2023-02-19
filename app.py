#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/2/19 20:26
# @Author  : notI
# @Site    : 
# @File    : app.py
# @Software: streamlitVideoPlayer
import cv2
import streamlit as st

# 定义侧边栏控件
st.sidebar.title("Video Player")
rtsp_url = st.sidebar.text_input("Enter RTSP URL")

if rtsp_url:
    # 打开视频流
    cap = cv2.VideoCapture(rtsp_url)

    # 创建主要的显示窗口
    st_frame = st.empty()

    # 循环读取并显示视频帧
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            st.warning("End of video stream!")
            break

        # 将视频帧转换为可显示的格式
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 显示视频帧
        st_frame.image(frame)

    # 关闭视频流
    cap.release()
