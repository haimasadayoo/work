
BASIC認証の概要
該当ディレクトリに
.htaccess
.htpasswd
を生成する。

.htaccessに.htpasswdのパスを入れる

その後
confでAllowOverrideがnoneとなっている場合はAuthConfig 或いはAllに切り替える

このconfの場所は
CentOs
/etc/httpd/conf/httpd.conf

Ubuntu
/etc/apache2/conf.d

MAC
/etc/apache2/httpd.conf

Windows
C:\Program Files (x86)\Apache software Foundation\pache2.2\conf\httpd.conf

最後に
systemctl restart apache2
で再起動かければ終了