# README

使用 Github Action 获取 Github 的 IP 地址便于修改 HOSTS 文件
## QUICK START

```bash
pip install -r requirements

python main.py 'github.com,gist.github.com,assets-cdn.github.com,raw.githubusercontent.com,gist.githubusercontent.com,cloud.githubusercontent.com,camo.githubusercontent.com,avatars.githubusercontent.com,avatars0.githubusercontent.com,avatars1.githubusercontent.com,avatars2.githubusercontent.com,avatars3.githubusercontent.com,avatars4.githubusercontent.com,avatars5.githubusercontent.com,avatars6.githubusercontent.com,avatars7.githubusercontent.com,avatars8.githubusercontent.com,avatars.githubusercontent.com,github.githubassets.com,user-images.githubusercontent.com,codeload.github.com,favicons.githubusercontent.com,marketplace-screenshots.githubusercontent.com,repository-images.githubusercontent.com,api.github.com'

cat hosts.txt
```

## 使用 Github Aciton

```txt
${{secrets.DOMAINS}} -> 需要查询的域名用逗号分隔拼接为字符串，eg：'test01.com,test02.com'
${{secrets.MAIL_USERNAME}} -> 发送邮件的 Gmail 用户名
${{secrets.MAIL_PASSWORD}} -> 发送邮件的密码，需要 Gmail 应用密码
${{secrets.MAIL_RECEIVER}} -> 接收邮件的邮箱地址
```

## REFERENCE

> https://github.com/ButterAndButterfly/GithubHost

> https://github.com/marketplace/actions/send-email