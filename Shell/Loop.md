Linux Shell

- if  循环控制 和 判断文件夹是否存在

      ```
      if [ ! -s "trainDataBeforeProcess" ]; then
              mkdir trainDataBeforeProcess
      else
              rm -rf trainDataBeforeProcess/*
      fi
      ```

