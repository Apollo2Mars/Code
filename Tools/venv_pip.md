- 安装制定版本
  - pip install keras=="1.2.2“

Worked

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple keras=="1.2.2"



Start 

    source venv-emnlp/bin/activate venv

venv is virtualenv folder



Stop

deactivate

---

- 其他方式，暂时不好用

    sudo pip --proxy=http://username:password@proxyURL:portNumber install sunburnt

    sudo pip --proxy=http://huadong.wang:samsung2017@109.105.4.28:1087 install keras

    set HTTP_PROXY=domain\huadong.wang:samsung2017@109.105.4.28:1087
    set HTTPS_PROXY=domain\huadong.wang:samsung2017@109.105.4.28:1087
    
    pip --proxy http://109.105.4.28:1087 install keras=="1.2.2"

 

- 新建venv
  - virtualenv venv-emnlp
