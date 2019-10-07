import logging

#日志常用的等级
    #DEBUG 调试，最详细的日志等级，通常用于问题问诊
    #INFO 详细程度只次与debug,记录的通常是关键节点的信息
    #WARNING 当某些不被期望的事情发生，但是程序还在正常运行
    #ERROR 出现严重的问题导致某部分功能不可用或者不可用正常使用
    #CRITICAL  严重错误，导致程序中断

# logging.basicConfig(level=logging.INFO) #设置显示的日志等级
#
# logging.debug("这是一个debug信息") #默认输出被过滤掉
# logging.info("这是一个info信息") #默认输出被过滤掉
# logging.warning("这是一个warning信息")
# logging.error("这是一个error信息")
# logging.critical("这是一个critical信息")

logging_header=logging.FileHandler("text.log",encoding="utf-8")
stream_header=logging.StreamHandler()

log_format="%(asctime)s-%(levelname)s-%(message)s" #日志格式
time_format="%Y-%m-%d %H:%M:%S"

logging.basicConfig(level=logging.DEBUG,format=log_format,datefmt=time_format,handlers=[logging_header,stream_header]) #设置显示的日志等级
logging.debug("这是一个debug信息") #m默认输出被过滤掉
logging.info("这是一个info信息") #m默认输出被过滤掉
logging.warning("这是一个warning信息")
logging.error("这是一个error信息")
logging.critical("这是一个critical信息")