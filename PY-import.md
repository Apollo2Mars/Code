## import 与 from import 的区别
  两个import语义有差异import datetime
  print(datetime.datetime.now())
  是引入整个datetime包from datetime import datetime
  print(datetime.now())
  是只引入datetime包里的datetime类所以import之后前者是datetime这个包可见 后者是datetime.datetime这个类可见
