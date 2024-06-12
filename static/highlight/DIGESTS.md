## Subresource Integrity

If you are loading Highlight.js via CDN you may wish to use [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) to guarantee that you are using a legimitate build of the library.

To do this you simply need to add the `integrity` attribute for each JavaScript file you download via CDN. These digests are used by the browser to confirm the files downloaded have not been modified.

```html
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"
  integrity="sha384-9mu2JKpUImscOMmwjm1y6MA2YsW3amSoFNYwKeUHxaXYKQ1naywWmamEGMdviEen"></script>
<!-- including any other grammars you might need to load -->
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/go.min.js"
  integrity="sha384-WmGkHEmwSI19EhTfO1nrSk3RziUQKRWg3vO0Ur3VYZjWvJRdRnX4/scQg+S2w1fI"></script>
```

The full list of digests for every file can be found below.

### Digests

```
sha384-o2RvzuEpU78s+xoEWs/++kMfb71T2QoVpd5kcyephebSrCF7IBl82kpINu7hXFCB /es/languages/apache.js
sha384-T5Wi3CdvOgNTDa/TQF3guYZxiCaiLFKzgYxX57ZCt1rVax+G6GP9EOlNdg8spAUs /es/languages/apache.min.js
sha384-0OZaeLK1yb5eP3nW4y0JP1fVharSrsuv/1mkI/6/8aRFm9laYIWIMXjCOqu+vRW5 /es/languages/c.js
sha384-G7WtwjMBNGrPly3ZsbPhfnT0v88hG3Ea9fQhrSWfzj7cNAsXsU7EKMQLyLGj7vTH /es/languages/c.min.js
sha384-Wjwd1YEG/PYlkLHTWIx+RlPK6XboMN3bEpveERJ8D8Z4RaNE02Ho19ZFrSRPGi0j /es/languages/cpp.js
sha384-Q4zTNH8WsDVdSZbiZtzWS1HmAUcvMSdTmth9Uqgfjmx7Qzw6B8E3lC9ieUbE/9u4 /es/languages/cpp.min.js
sha384-Sp8E1Lb9fNhbvqBiogM60TCgpAIwYBi8WbHhIHcXO0bR5Z+9LeYwpDa1gkjzU99W /es/languages/csharp.js
sha384-huUb4Ol37G1WrtGV7bn1UArXcJSjD4tQswMGzgpNZYAPxR74MHTqW79z1dXWMvhk /es/languages/csharp.min.js
sha384-DA5ii4oN8R2fsamNkHOanSjuN4v7j5RIuheQqnxMQ4cFnfekeuhwu4IdNXiCf+UU /es/languages/css.js
sha384-OBugjfIr093hFCxTRdVfKH8Oe3yiBrS58bhyYYTUQJVobk6SUEjD7pnV8BPwsr8a /es/languages/css.min.js
sha384-CKR1L8zV+xW7x1ew3V6y1VNG5KK+PhSS3XuxR32anU4uXx52Sr6xhQIzLo+P56Tq /es/languages/dos.js
sha384-Lr5UvDlMpLCSLEdIc9Jbe7lSHTs1UqFkGAwkacIOzl/Vx34B82LFi+2CeClz1zC/ /es/languages/dos.min.js
sha384-7m427rj9OYl8KKObOk+aD0QhXmqXy6hU/sHGS6OUwW9hRiiHvr+tLTbLiSJYbIyD /es/languages/http.js
sha384-GdKwMgTrO0R3SPXhm+DuaN3Qr7WkqYmmTClINAGPuV/BUPE9WUI/WnTEntp522Sl /es/languages/http.min.js
sha384-7hMYwsnoFLW0Wnjv4vRnZxuedW1tCz7/pydl1b9w3fg7B+rldToCjqzXwCRHUE7C /es/languages/ini.js
sha384-LDu6uT3diI3jBUJtdoGFa787cYlVrR+aqFfmW+kW+TImOkpVe+P5LBdDzydIHo9Z /es/languages/ini.min.js
sha384-WFJdA9Hz+G9NQx5vPba/tcGyIibm57UkKVY32wNB/94iT2FmPma5W7gY8p2l6qps /es/languages/java.js
sha384-coaxfgI2lKuDqSxfMlfyPq5WM0THaLGyATZHzaFMrWdIbPcLdduuItTe6AmT/m33 /es/languages/java.min.js
sha384-WCznKe2n87QvV/L1MlXN+S8R6NPUQGU34+AqogMuWGZJswSD6rt3Mgih+xuKlDgm /es/languages/javascript.js
sha384-eGsBtetyKPDKaLiTnxTzhSzTFM6A/yjHBQIj4rAMVaLPKW5tJb8U6XLr/AikCPd+ /es/languages/javascript.min.js
sha384-12GbYFzdyZCSmfBTmO2CR/qE89K5uE1PEuJ3QUwXH0Q9u+uoLNigjH9dG7LAxxiI /es/languages/json.js
sha384-+DT7AtubDhVDciRc6CgjJJRsCt0L8NC3Dh8n9Tj2tZWU8rWxDIj1ViubmUDn8OCY /es/languages/json.min.js
sha384-tsX5LI0gdW2Xk9ZMsj7B2vRchm3jC0zoc1r99Z1377aXFJJXimRtRYQprUJpSuu0 /es/languages/kotlin.js
sha384-mfmdbPhLobPr5OJzSXlWHDQDymRYyzedurWjJBvKVhlQGE+Jz/pN3D9lPEBIkDK2 /es/languages/kotlin.min.js
sha384-JBkI+6623OoC1qCgG+MY/Ta0qRYSzTDH4NGMA+7U8RNOjkh7geFvYpRidvdHs3zT /es/languages/php.js
sha384-6Znh5S5q9F0hGNMtdaihFL3RJeMqL1a/UecjgzaBrhoxe4sjd5aiEOgokt7blhSW /es/languages/php.min.js
sha384-TTDGPCrk8Dg2oW6NghGM5WJQPbi34BdYJj6yfsDiGXlM5os/SebXT6KzATp19rzo /es/languages/plaintext.js
sha384-XXx7wj9KPm08AyGoGzzFKZP2S7S+S5MbKMPnQcWUyhJ3EjHvLuctK/O1ioJnG2ef /es/languages/plaintext.min.js
sha384-PpU3S+yZJ1Gj2R7L/OgTgkKELQOf7F1VcbaAEJwSFSM9lw2ON2wxq1FvUcUlm9ne /es/languages/powershell.js
sha384-pBczxETXXX/Ne92jpBviT47DPiv27FLNtvs0aMZH3W7rYXdwgf1gWg3pH4NmNC2V /es/languages/powershell.min.js
sha384-+5oyk7Ed3OlvEWGj8xracq/6e52BScKUN4kxcreNwB7kfRTVsAMs/aAJM58dzIFN /es/languages/python.js
sha384-ND/UH2UkaeWiej5v/oJspfKDz9BGUaVpoDcz4cof0jaiv/mCigjvy7RQ7e+3S6bg /es/languages/python.min.js
sha384-GLWbnkTbelVKeKv8VxFhtauUDfV8uqxjBPEEZ3WYks9zmbd1rFCWmdzGucZn0+ZQ /es/languages/r.js
sha384-T5hv8+GOm2ni1B0cuZtt+8T0cIMH1CTycc9OQQH0GLcIQhmeBosyhcmcIv4r/1ag /es/languages/r.min.js
sha384-vs4jXytP3N3d5zRX15Fqc4u/kDI5jDr3PNYIvQ0mmmoU+o/yxJfu/+VYme6qIOa2 /es/languages/ruby.js
sha384-O4a+vELXT191NhKLE3TR5WQwDmQZ2izAhb2zETRxcPSXr6CJruqJ4a+GJpDlaqCF /es/languages/ruby.min.js
sha384-lRhSX2XDrY27NzrAS1t4YaeRtwjsY41kFBbIEYltkmnsfSE7lbBJMQVds2u/MqTT /es/languages/scss.js
sha384-RDUehV4j9Do6iGkYq9Gjn3aUxh6x+NFER1sHpLUXsNoCFjah8Ysrlad8ukLbIr4J /es/languages/scss.min.js
sha384-dzLjhd9nNJH62idgKI1vZEKHRBtZXSgwWQdPR+emG7tfAN4BW2g+A5Xs2315Uxii /es/languages/shell.js
sha384-RKUoelG22/D7BV/bNpoGLNzdTgWRf/ACQX7y4BGyIzK6E+xUoXtm68WNQW2tSW8X /es/languages/shell.min.js
sha384-rBAFhyrcRcMNbVJ9g4k5y3eQDkjGdgoOb3oTWTbHgwyUgUNv3CK9wLsGy/d+52oa /es/languages/sql.js
sha384-8G3qMPeOeXVKZ0wGzMQHgMVQWixLw3EXFAcU+IFNLRe0WoZB5St3L3ZLTK62Nzns /es/languages/sql.min.js
sha384-CS3qiWid6Sod3yAiQwgPzy2ZerR00u/cwhnMxQrETuI74o006r1p5qj1U9Gdo4uD /es/languages/typescript.js
sha384-HHgazax8ozQ9RDWlJQyaFzaTk/OgTFRVHH+lcaYInkE8wVu5fnpkqkB3KUdzKcvE /es/languages/typescript.min.js
sha384-OFoR8IZ+CFwcY8plx8HSDZNoCwLxc701CwdNGfoIEhSgwAbwhvInaxnEi3HYTt2Q /es/languages/xml.js
sha384-yFd3InBtG6WtAVgIl6iIdFKis8HmMC7GbbronB4lHJq3OLef3U8K9puak6MuVZqx /es/languages/xml.min.js
sha384-MX3xn8TktkjONV3aWF6Qn6WZyq2Lh/98p0v7D0qEoJ4WLdYjoAyXF/L/80q3qaEc /es/languages/yaml.js
sha384-4IiaMbQ0LBiRJYBGoAXsN+dV9qu/cGLES6IuVowdeCu/FAMY5/MQfD/bHXoL2YBb /es/languages/yaml.min.js
sha384-hK+QzfKnkrwE7Fgc3q6lpKfnWWKMecpkQObMVOPiwopZiJni16bBGVm37SMGcz6G /languages/apache.js
sha384-bvrESIqIr21pkx86VgiN+Vfq8sRk/6xTxMfbo0PDENLfqYr123El7PUCzqJmir4P /languages/apache.min.js
sha384-VZxKf0mjKYDwZIgrW+InqDfJ0YwYUFEMw/4YmpV1oKtVXFVmVq/Ga1vgq6zKTUqS /languages/c.js
sha384-mWenE7UXKnmYRcJ3mh+Os3iZ43BmFf9x3AZMM6gi/2sT6vxouPWspbTdREwWDO3w /languages/c.min.js
sha384-J4Ge+xXjXgzbK2FP+OyzIGHLfKU/RR0+cH4JJCaczeLETtVIvJdvqfikWlDuQ66e /languages/cpp.js
sha384-LMyrRAiUz6we2SGvYrwDd4TJoJZ+m/5c+4n4E64KVkfWFcZdlrs4Wabr0crMesyy /languages/cpp.min.js
sha384-8sbRwiU8Ar2M7+w//1u7YiI1e7KsmB4k3QbW/m1IW5FVH51HiOpR7g5QGE3RqTNi /languages/csharp.js
sha384-wWP4JQEhRVshehTP7lUMDn3yhDI2+398vN2QW5LBt1xIpK0Gfu4dPviO8tP9XRo5 /languages/csharp.min.js
sha384-r9czyL17/ovexTOK33dRiTbHrtaMDzpUXW4iRpetdu1OhhckHXiFzpgZyni2t1PM /languages/css.js
sha384-HpHXnyEqHVbcY+nua3h7/ajfIrakWJxA3fmIZ9X9kbY45N6V+DPfMtfnLBeYEdCx /languages/css.min.js
sha384-4Wih2Lsfyf2mx5BElP+XAeDUzWqwRfa0VefDGmCF7vCposOAa0r5jaf4jVm4/LBK /languages/dos.js
sha384-6+/BHm9a7L7KFZE/myAKBddEjwfPovVtBzDrEu/6VqocfSqvRMyM+Lf3k9n89yGH /languages/dos.min.js
sha384-g/lhU6FXH73RQL4eFwkPk4CuudGpbHg6cyVZCRpXft3EKCrcQTToBVEDRStjYWQb /languages/http.js
sha384-wt2eEhJoUmjz8wmTq0k9WvI19Pumi9/h7B87i0wc7QMYwnCJ0dcuyfcYo/ui1M6t /languages/http.min.js
sha384-JSUMPR+WT0h/7NlqXi1Al9bVlNT31AeZNpAHttuzu+r02AmxePeqvsZkKqYZf06n /languages/ini.js
sha384-QrHbXsWtJOiJjnLPKgutUfoIrj34yz0+JKPw4CFIDImvaTDQ/wxYyEz/zB3639vM /languages/ini.min.js
sha384-pYIeBYeCE96U9EkPcT4uJjNWyrB1BKB41JIadYJbvmGa5KacaoXtSQOUpBfeyWQX /languages/java.js
sha384-uUg+ux8epe42611RSvEkMX2gvEkMdw+l6xG5Z/aQriABp38RLyF9MjDZtlTlMuQY /languages/java.min.js
sha384-vJxw3XlwaqOQr8IlRPVIBO6DMML5W978fR21/GRI5PAF7yYi2WstLYNG1lXk6j9u /languages/javascript.js
sha384-44q2s9jxk8W5N9gAB0yn7UYLi9E2oVw8eHyaTZLkDS3WuZM/AttkAiVj6JoZuGS4 /languages/javascript.min.js
sha384-dq9sY7BcOdU/6YaN+YmFuWFG8MY2WYJG2w3RlDRfaVvjdHchE07Ss7ILfcZ56nUM /languages/json.js
sha384-RbRhXcXx5VHUdUaC5R0oV+XBXA5GhkaVCUzK8xN19K3FmtWSHyGVgulK92XnhBsI /languages/json.min.js
sha384-UjoANPpyYDKhhXCD7M94TUBIvEg+Yey//mTGwAKIPkAcmpT4QVk8D47YYWumt/ZR /languages/kotlin.js
sha384-vfngjS9mwSs6HkzR9wU3mDDip7sa8TLKAxsuQ9+ncUHU25slHzHOdx/0FWxvbg4I /languages/kotlin.min.js
sha384-S1JDGPScVg8ikNKLZc4CSP0ZxLiJ7bOJMzTLfOzQiCxR6wPqAa+YtauHJXQpc2GV /languages/php.js
sha384-c1RNlWYUPEU/QhgCUumvQSdSFaq+yFhv3VfGTG/OTh8oirAi/Jnp6XbnqOLePgjg /languages/php.min.js
sha384-IHapUcPkNR+7JNsR+qYSVYGCE3Dpzo2//VYWtmGYrw3eQG1RItQ7HYq6aK1Jo/6L /languages/plaintext.js
sha384-ofjxHpechXkaeQipogSyH62tQNaqAwQiuUHOVi4BGFsX5/KectIoxz16f8J/P5U0 /languages/plaintext.min.js
sha384-BW3J/7iREOC3EuqJwzGkDJb6FY9bVvkt70ipieV892fYAp8uReDMiO0/lrUPmkzL /languages/powershell.js
sha384-LWJZQx0dgGhEK7snfNYrQs5K+QKD1sOmE02sOQCz4br9UmqSJDvPLoUVFaUyFnjq /languages/powershell.min.js
sha384-zdZio5RcGiKQJCpe/1IXujPle3bIY8sbmvCabSU5G5GzWAzZtoRZfg9QAQXCL08q /languages/python.js
sha384-IP4vv4Aoh9Lyg8QyzVkAmn2JGoDCpgVHzVSrD3Z+rVyn7+s4wx4pRjv+go3TEwfj /languages/python.min.js
sha384-Xa3MEXJyV9PD/wnbdHTdqvipEl9QqodA35i6Nmw/6wqrvQ585Q8EDfz7f2UCuYpU /languages/r.js
sha384-+z7INDMj7HMs67TuLfoyKa6TUHdTweahANtJ1Spg6uCa8/f1jFUf238jj53TDxmP /languages/r.min.js
sha384-AE7f30oAuQtqmFee9hPd2uoo44ZkyUY2wQL7DjjENhh2wrvS6q4mpxGtAxeCxiRQ /languages/ruby.js
sha384-pFZpTUpdH4YEXSenc9hfKZ4uCv2IQoJQCIlIHpA0fM2cvTVH8LuzQMNcGSRGeJG0 /languages/ruby.min.js
sha384-fwYddFsITuK2bPhi9RuIzwi4PTULEXgtEJsQzTdx97vOS/GHfrk+aNSLxEHgzQa5 /languages/scss.js
sha384-6u+QpCDqQidb5pcO+yBqy0xLJ30x30VlrFvXm8J84LMwGIw9q3U4u+Z9vFXlhB5x /languages/scss.min.js
sha384-KW3ZDReTAemYUfVHvH1MNQ/v6agCYYdMGdMteP/yVV+NetIJeDMx0ruUMTbr/SD3 /languages/shell.js
sha384-PDEMny3uYpCrSKwqVGLAwqCsc9u+9hYXauxVPqO6RXmlxSNKLoRByEBigU5lahmK /languages/shell.min.js
sha384-Dy7I/j0yJlyliWiNrkNqXfxDrbN65q40s3JColgTYZQ7QJa7lcmK0WUL3i00/T51 /languages/sql.js
sha384-8q00eP+tyV9451aJYD5ML3ftuHKsGnDcezp7EXMEclDg1fZVSoj8O+3VyJTkXmWp /languages/sql.min.js
sha384-yZXtQC/OmWoPykosK7vE1nCvV4E/six6+apjNau4JwBkejkea5nP7VBEJJkGnvoF /languages/typescript.js
sha384-ORwtVEfrCZ0gzGacgmfv1wOtxcPIaVfHKwq8dKQjObRwx3qpKjsSg1ldTu1PEgXd /languages/typescript.min.js
sha384-+PuZYFfVX2UQZU2yKt/FsJUZNUPzZWxW7auXltsaecr1xLvzBYF3c5gYoyOs1++x /languages/xml.js
sha384-jgkY4GMNWfQcLLIoP1vg3FWXflDrRhcSXGBW6ONIWC2SOIv5H1Pa57sXs+aomCuZ /languages/xml.min.js
sha384-tB5cwwsX4Ddp7P4d+ZInDb3nt4ihEEglHXoQ18eVLlT7soEn7bfGfABWKIn1l+H2 /languages/yaml.js
sha384-WC56y8OaFPt5Kj2HX6JAumxUYEjQmBDcSTJy2pn/N8g7dg1hKjeNVrJYoxlpeVmz /languages/yaml.min.js
sha384-utb0cjtbzXqWkMRt97OenkYYqgbSrAEdqcJRgUDH8fspATYHCq9QG6F7Vm5+Lu2a /highlight.js
sha384-UAyZa2kQcO5tLBAz3IEPf1/qDKJMU+m9bPI77GIzs6VVYoKtIp5S6eS/iTMkATtj /highlight.min.js
```

