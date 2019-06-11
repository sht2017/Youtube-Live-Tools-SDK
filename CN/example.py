# 请勿使用该模块及范例对任何YouTube主播/VTuber进行骚扰！！！！！
# 如果查实滥用该模块及范例的行为 将会取得受害人的同意后发起舆论上的声讨 情节严重的将考虑予以起诉
# 注意 这是一个模块引用范例 目的是帮助你更好的理解如何使用该模块
# 作者John Stonty QQ:1844063767 遇到问题欢迎联系

import main #引用模块 当然也可以使用as简化


main.init("vrwSrCr9J4s") #初始化模块 (启动监听服务及浏览器)
# 上行括号->引号内的内容为YouTube直播间ID
# 比如原直播的youtube链接为 www.youtube.com/watch?v=vrwSrCr9J4s 或是 youtu.be/vrwSrCr9J4s
# 那么直播间ID即为vrwSrCr9J4s
# 范例引用的直播间是Yuna Channel(桜美ゆな)的
# 因为24小时配信所以便于调试 请勿滥用！！！

main.sendMessages("こんにちは:)") #在目标直播间发送指定文本
# 注意: Youtube 的实时聊天仅支持单行文本
# 如果要发送多条消息可以重复调用该过程

main.stop() #关闭监听服务及浏览器
# 记得结束时一定要调用该过程！！！
# 否则headless chrome不会自动关闭 这样反复下来会占用过多资源