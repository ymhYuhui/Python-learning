from win10toast import ToastNotifier
import time

mydelaymin = 60 # 窗口提示的延迟时间，以分钟计
toaster = ToastNotifier()
toaster.show_toast(u'定时提醒已启动', u'开始上班吧！')

while True:
  time.sleep(mydelaymin*60)  # 参数为秒
  toaster.show_toast(u'已经工作一个小时了', u'起来溜达溜达！！！！！！！！')




