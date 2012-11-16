这是一个用于做进度管理的插件。
是我在工作中，有很多后台的脚本和以及在远程需要执行的程序。
对于他们的进度如何管理是个问题，远程执行的脚本如果用过拉去执行日志的话，是很不靠谱的，因为一旦脚本执行出错，日志后续是后去不到的。
因此我开发了进度管理的插件。
通过http协议上报进度数据，一般在linux可以使用curl工具，python可以使用urllib发送http请求，都比较方便。
前台通过页面查看进度数据。

整个服务是通过django提供http服务。

后续第一版开发完成可以在完成使用文档。

发送进度数据curl命令：curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"execStat":"succ","cmdTypeName": "cmd_ds", "progressId": 1, "progressStat": "start", "remark": "start","progressName":"1.1.1.1"}' http://127.0.0.1:8000
