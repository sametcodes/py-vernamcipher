<b>Vernam şifrelemesini uygulayabileceğiniz basit bir Python betiği.</b>

<h2>Kullanımı</h2>

<b>Şifreleme</b>

Aynı uzunluktaki metini, <b>belirli bir anahtar</b> ile şifrelemek için:<br>
<code>python2 py-vernamcipher.py -e [sifrelenecek_metin] [anahtar]</code>

Aynı uzunluktaki metini, <b>rastgele bir anahtar</b> ile şifrelemek için:<br>
<code>python2 py-vernamcipher.py -e [sifrelenecek_metin] -rkey</code>

<b>Şifre çözme</b>

<code>python2 py-vernamcipher.py -d [sifrelenmis_metin] [anahtar]</code>
